from config.db import DBConnection as mydb

prodi = []

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

mk = GlobalVariable()
mk.getAllProdi()
