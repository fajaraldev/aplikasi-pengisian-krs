from config.db import DBConnection as mydb

class Matakuliah:

    def __init__(self):
        self.__kode_matakuliah=None
        self.__matakuliah=None
        self.__sks=None
        self.__prodi=None
        self.__semester=None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def kode_matakuliah(self):
        return self.__kode_matakuliah

    @kode_matakuliah.setter
    def kode_matakuliah(self, value):
        self.__kode_matakuliah = value

    @property
    def matakuliah(self):
        return self.__matakuliah

    @matakuliah.setter
    def matakuliah(self, value):
        self.__matakuliah = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        self.__semester = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_matakuliah,self.__matakuliah,self.__sks,self.__prodi,self.__semester)
        sql="INSERT INTO matakuliah (kode_matakuliah, matakuliah, sks, prodi, semester) VALUES (%s,%s,%s,(SELECT p.kode_prodi FROM prodi AS p WHERE %s=p.prodi),%s)"
        self.affected = self.conn.insertWithConditional(sql,val)
        self.conn.disconnect
        return self.affected

    def updateByKodeMatakuliah(self, kode_matakuliah):
        self.conn = mydb()
        val = (self.__matakuliah,self.__sks,self.__prodi,self.__semester, kode_matakuliah)
        sql="UPDATE matakuliah SET matakuliah=%s, sks=%s, prodi=(SELECT p.kode_prodi FROM prodi AS p WHERE %s=p.prodi), semester=%s WHERE kode_matakuliah=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def deleteByKodeMatakuliah(self, kode_matakuliah):
        self.conn = mydb()
        sql="DELETE FROM matakuliah WHERE kode_matakuliah='" + str(kode_matakuliah) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByKodeMatakuliah(self, kode_matakuliah):
        self.conn = mydb()
        sql="SELECT m.kode_matakuliah, m.matakuliah, m.sks, p.prodi, m.semester FROM matakuliah AS m, prodi AS p WHERE kode_matakuliah='" + str(kode_matakuliah) + "'  AND m.prodi=p.kode_prodi"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_matakuliah = self.result[0]
            self.__matakuliah = self.result[1]
            self.__sks = self.result[2]
            self.__prodi = self.result[3]
            self.__semester = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_matakuliah = ''
            self.__matakuliah = ''
            self.__sks = ''
            self.__prodi = ''
            self.__semester = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT m.kode_matakuliah, m.matakuliah, m.sks, p.prodi, m.semester FROM matakuliah AS m, prodi AS p WHERE m.prodi=p.kode_prodi ORDER BY m.semester ASC"
        self.result = self.conn.findAll(sql)
        return self.result
