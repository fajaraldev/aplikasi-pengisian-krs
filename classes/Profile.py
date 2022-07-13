from config.db import DBConnection as mydb

class Profile:

    def __init__(self):
        self.__username=None
        self.__nama=None
        self.__prodi=None
        self.__jk=None
        self.__ttl=None
        self.__alamat = None
        self.__email = None
        self.__telepon = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value

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

    def updateByUsername(self, username):
        self.conn = mydb()
        val = (self.__nama,self.__jk,self.__ttl,self.__alamat,self.__email,self.__telepon, username)
        sql="UPDATE mahasiswa SET nama=%s, jk=%s, ttl=%s, alamat=%s, email=%s, telepon=%s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def getByUsername(self, username):
        self.conn = mydb()
        sql="SELECT m.nim,m.nama,p.prodi,m.jk,m.ttl,m.alamat,m.email,m.telepon FROM mahasiswa AS m, prodi AS p WHERE m.nim='" + str(username) + "' AND m.prodi=p.kode_prodi"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__username = self.result[0]
            self.__nama = self.result[1]
            self.__prodi = self.result[2]
            self.__jk = self.result[3]
            self.__ttl = self.result[4]
            self.__alamat = self.result[5]
            self.__email = self.result[6]
            self.__telepon = self.result[7]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__username = ''
            self.__nama = ''
            self.__prodi = ''
            self.__jk = ''
            self.__ttl = ''
            self.__alamat = ''
            self.__email = ''
            self.__telepon = ''
            self.affected = 0
        self.conn.disconnect
        return self.result
