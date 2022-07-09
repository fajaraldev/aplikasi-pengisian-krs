from config.db import DBConnection as mydb

class GlobalVariable:
  def __init__(self):
      self.prodi=[]
      self.matakuliah=[]

      self.__prodi = None

      self.conn = None
      self.affected = None
      self.result = None

  def getAllProdi(self):
      self.conn = mydb()
      sql="SELECT * FROM prodi"
      self.result = self.conn.findAll(sql)
      for x in self.result:
        self.prodi.append(x)

  def getAllMatakuliahByProdi(self,prodi):
      self.conn = mydb()
      sql="SELECT * FROM matakuliah WHERE prodi='" + str(prodi) + "'"
      self.result = self.conn.findAll(sql)
      for x in self.result:
        self.matakuliah.append(x)

  def getAllMatakuliahByProdiAndSemester(self,username,semester):
      self.conn = mydb()
      sql="SELECT m.kode_matakuliah,m.matakuliah,m.sks,m.prodi,m.semester FROM matakuliah AS m WHERE m.prodi=(SELECT prodi FROM mahasiswa WHERE nim='"+ str(username) +"') AND m.semester='" + str(semester) + "'"
      self.result = self.conn.findAll(sql)
      if(self.result!=None):
        self.matakuliah.clear() # reset array matakuliah
        for x in self.result:
          self.matakuliah.append(x)
        self.affected = self.conn.cursor.rowcount
      else:
          self.matakuliah.clear() # reset array matakuliah
          self.affected = 0
      self.conn.disconnect
      return self.result

# prodi="A01"
# semester=4
# # mk.getAllMatakuliahByProdi(prodi,semester)
# mk.getAllMatakuliahByProdiAndSemester(prodi,semester)
