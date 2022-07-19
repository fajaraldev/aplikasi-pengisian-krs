from config.db import DBConnection as mydb

class Dosen:

    def __init__(self):
        self.__nidn=None
        self.__nama=None
        self.__jk=None
        self.__ttl=None
        self.__alamat = None
        self.__email = None
        self.__telepon = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def nidn(self):
        return self.__nidn

    @nidn.setter
    def nidn(self, value):
        self.__nidn = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def ttl(self):
        return self.__ttl

    @ttl.setter
    def ttl(self, value):
        self.__ttl = value

    @property
    def alamat(self):
        return self.__alamat

    @alamat.setter
    def alamat(self, value):
        self.__alamat = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def telepon(self):
        return self.__telepon

    @telepon.setter
    def telepon(self, value):
        self.__telepon = value

    def simpan(self):
        self.conn = mydb()
        val=(self.__nidn,self.__nama,self.__jk,self.__ttl,self.__alamat,self.__email,self.__telepon)
        sql="INSERT INTO dosen (nidn, nama, jk, ttl, alamat, email, telepon) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def updateByNidn(self, nidn):
        self.conn = mydb()
        val = (self.__nama,self.__jk,self.__ttl,self.__alamat,self.__email,self.__telepon, nidn)
        sql="UPDATE dosen SET nama=%s, jk=%s, ttl=%s, alamat=%s, email=%s, telepon=%s WHERE nidn=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def deleteByNidn(self, nidn):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE nidn='" + str(nidn) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByNidn(self, nidn):
        self.conn = mydb()
        sql="SELECT nidn,nama,jk,ttl,alamat,email,telepon FROM dosen WHERE nidn='" + str(nidn) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nidn = self.result[0]
            self.__nama = self.result[1]
            self.__jk = self.result[2]
            self.__ttl = self.result[3]
            self.__alamat = self.result[4]
            self.__email = self.result[5]
            self.__telepon = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nidn = ''
            self.__nama = ''
            self.__jk = ''
            self.__ttl = ''
            self.__alamat = ''
            self.__email = ''
            self.__telepon = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT nidn,nama,jk,ttl,alamat,email,telepon FROM dosen limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
