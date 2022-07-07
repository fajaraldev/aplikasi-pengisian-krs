from config.db import DBConnection as mydb

class GlobalVariable:
  def __init__(self):
      self.prodi=[]
      self.matakuliah=[]

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

  def getAllMatakuliahByProdiAndSemester(self,prodi,semester):
      self.conn = mydb()
      val = (prodi,semester)
      sql="SELECT * FROM matakuliah WHERE prodi=%s AND semester=%s"
      self.result = self.conn.findAllWithConditional(sql,val)
      for x in self.result:
        self.matakuliah.append(x)

  def setCurrentUser(self,username,password):
      val = (prodi,semester)
      self.conn = mydb()
      sql="SELECT u.username,u.password,r.role_name FROM users AS u, roles AS r WHERE username=%s AND password=%s AND u.role_id=r.role_id"

# prodi="A01"
# semester=4
# # mk.getAllMatakuliahByProdi(prodi,semester)
# mk.getAllMatakuliahByProdiAndSemester(prodi,semester)
