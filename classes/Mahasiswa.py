from config.db import DBConnection as mydb

class Mahasiswa:

    def __init__(self):
        self.__nim=None
        self.__nama=None
        self.__prodi=None
        self.__jk=None
        self.__ttl=None
        self.__alamat = None
        self.__email = None
        self.__telepon = None
        self.__kode_wali = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

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

    @property
    def kode_wali(self):
        return self.__kode_wali

    @kode_wali.setter
    def kode_wali(self, value):
        self.__kode_wali = value

    def simpan(self):
        self.conn = mydb()
        # values for table mahasiswa and users, where username and password == nim
        sql_mahasiswa="INSERT INTO mahasiswa (nim, nama, prodi, jk, ttl, alamat, email, telepon,kode_wali) VALUES ('"+str(self.__nim)+"','"+str(self.__nama)+"',(SELECT p.kode_prodi FROM prodi AS p WHERE p.prodi='"+str(self.__prodi)+"'),'"+str(self.__jk)+"','"+str(self.__ttl)+"','"+str(self.__alamat)+"','"+str(self.__email)+"','"+str(self.__telepon)+"','"+str(self.__kode_wali)+"');"
        sql_users="INSERT INTO users (username,password) VALUES ('"+str(self.__nim)+"','"+str(self.__nim)+"');"
        self.affected = self.conn.insertMultipleTable(sql_mahasiswa, sql_users)
        self.conn.disconnect
        return self.affected

    def updateByNim(self, nim):
        self.conn = mydb()
        val = (self.__nama,self.__prodi,self.__jk,self.__ttl,self.__alamat,self.__email,self.__telepon,self.__kode_wali, nim)
        sql="UPDATE mahasiswa SET nama=%s, prodi=(SELECT p.kode_prodi FROM prodi AS p WHERE %s=p.prodi), jk=%s, ttl=%s, alamat=%s, email=%s, telepon=%s, kode_wali=%s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def deleteByNim(self, nim):
        self.conn = mydb()
        sql_mahasiswa="DELETE FROM mahasiswa WHERE nim='" + str(nim) + "'"
        sql_users="DELETE FROM users WHERE username='" + str(nim) + "'"
        self.affected = self.conn.deleteMultipleTable(sql_mahasiswa,sql_users)
        self.conn.disconnect
        return self.affected

    def getByNim(self, nim):
        self.conn = mydb()
        sql="SELECT m.nim,m.nama,p.prodi,m.jk,m.ttl,m.alamat,m.email,m.telepon,m.kode_wali FROM mahasiswa AS m, prodi AS p WHERE nim='" + str(nim) + "' AND m.prodi=p.kode_prodi"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[0]
            self.__nama = self.result[1]
            self.__prodi = self.result[2]
            self.__jk = self.result[3]
            self.__ttl = self.result[4]
            self.__alamat = self.result[5]
            self.__email = self.result[6]
            self.__telepon = self.result[7]
            self.__kode_wali = self.result[8]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__nama = ''
            self.__prodi = ''
            self.__jk = ''
            self.__ttl = ''
            self.__alamat = ''
            self.__email = ''
            self.__telepon = ''
            self.__kode_wali = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT m.nim,m.nama,p.prodi,m.jk,m.ttl,m.alamat,m.email,m.telepon,m.kode_wali FROM mahasiswa AS m, prodi AS p WHERE m.prodi=p.kode_prodi limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
