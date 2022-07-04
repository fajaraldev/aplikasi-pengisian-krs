from config.db import DBConnection as mydb

prodi=[]
matakuliah=[]

class GlobalVariable:
  def __init__(self):
      self.conn = None
      self.affected = None
      self.result = None

  def getAllProdi(self):
      self.conn = mydb()
      sql="SELECT * FROM prodi"
      self.result = self.conn.findAll(sql)
      for x in self.result:
        prodi.append(x)

  def getAllMatakuliahByProdi(self,prodi):
      self.conn = mydb()
      sql="SELECT * FROM matakuliah WHERE prodi='" + str(prodi) + "'"
      self.result = self.conn.findAll(sql)
      for x in self.result:
        matakuliah.append(x)

  def getAllMatakuliahByProdiAndSemester(self,prodi,semester):
      self.conn = mydb()
      val = (prodi,semester)
      sql="SELECT * FROM matakuliah WHERE prodi=%s AND semester=%s"
      self.result = self.conn.findAllWithConditional(sql,val)
      for x in self.result:
        matakuliah.append(x)

mk = GlobalVariable()
mk.getAllProdi()
prodi="A01"
semester=4
# mk.getAllMatakuliahByProdi(prodi,semester)
mk.getAllMatakuliahByProdiAndSemester(prodi,semester)
