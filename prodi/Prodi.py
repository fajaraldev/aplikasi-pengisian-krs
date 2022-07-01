from config.db import DBConnection as mydb

class Prodi:

    def __init__(self):
        self.__kode_prodi=None
        self.__prodi=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def kode_prodi(self):
        return self.__kode_prodi

    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value

    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_prodi,self.__prodi)
        sql="INSERT INTO prodi (kode_prodi,prodi) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def updateByKodeProdi(self, kode_prodi):
        self.conn = mydb()
        val = (self.__prodi, kode_prodi)
        sql="UPDATE prodi SET prodi=%s WHERE kode_prodi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def deleteByKodeProdi(self, kode_prodi):
        self.conn = mydb()
        sql="DELETE FROM prodi WHERE kode_prodi='" + str(kode_prodi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByKodeProdi(self, kode_prodi):
        self.conn = mydb()
        sql="SELECT * FROM prodi WHERE kode_prodi='" + str(kode_prodi) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_prodi = self.result[0]
            self.__prodi = self.result[1]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_prodi = ''
            self.__prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM prodi limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
