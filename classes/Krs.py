from config.db import DBConnection as mydb

class Krs:

    def __init__(self):
        self.__id=None
        self.__ajaran=None
        self.__semester=None
        self.__nim=None
        self.__prodi=None
        self.__matakuliah=None
        self.__hari=None
        self.__waktu=None
        self.__ruang=None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def ajaran(self):
        return self.__ajaran

    @ajaran.setter
    def ajaran(self, value):
        self.__ajaran = value

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        self.__semester = value

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value

    @property
    def matakuliah(self):
        return self.__matakuliah

    @matakuliah.setter
    def matakuliah(self, value):
        self.__matakuliah = value

    @property
    def hari(self):
        return self.__hari

    @hari.setter
    def hari(self, value):
        self.__hari = value

    @property
    def waktu(self):
        return self.__waktu

    @waktu.setter
    def waktu(self, value):
        self.__waktu = value

    @property
    def ruang(self):
        return self.__ruang

    @ruang.setter
    def ruang(self, value):
        self.__ruang = value

    def getUserNimAndProdi(self,username):
        self.conn = mydb()
        sql="SELECT nim,prodi FROM mahasiswa WHERE nim='" + str(username) + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[0]
            self.__prodi = self.result[1]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''
            self.__prodi = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def simpan(self):
        self.conn = mydb()
        val = (self.__ajaran,self.__semester,self.__nim,self.__prodi,self.__matakuliah,self.__semester,self.__hari,self.__waktu,self.__ruang)
        sql="INSERT INTO krs (ajaran,semester,nim,prodi,matakuliah,hari,waktu,ruang) VALUES (%s,%s,%s,%s,(SELECT m.kode_matakuliah FROM matakuliah AS m WHERE m.matakuliah=%s AND m.semester=%s),%s,%s,%s)"
        self.affected = self.conn.insertWithConditional(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByIdKrs(self, id):
        self.conn = mydb()
        val = (self.__ajaran,self.__semester,self.__nim,self.__prodi,self.__matakuliah,self.__semester,self.__hari,self.__waktu,self.__ruang, id)
        sql="UPDATE krs SET ajaran=%s, semester=%s, nim=%s, prodi=%s, matakuliah=(SELECT m.kode_matakuliah FROM matakuliah AS m WHERE m.matakuliah=%s AND m.semester=%s), hari=%s, waktu=%s, ruang=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def deleteByIdKrs(self, id):
        self.conn = mydb()
        sql="DELETE FROM krs WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByIdKrs(self, id):
        self.conn = mydb()
        sql="SELECT k.id,k.ajaran,k.semester,m.matakuliah,k.hari,k.waktu,k.ruang FROM krs AS k, matakuliah AS m WHERE id='" + str(id) + "'  AND k.matakuliah=m.kode_matakuliah"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__id = self.result[0]
            self.__ajaran = self.result[1]
            self.__semester = self.result[2]
            self.__matakuliah = self.result[3]
            self.__hari = self.result[4]
            self.__waktu = self.result[5]
            self.__ruang = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:

            self.__id = ''
            self.__ajaran = ''
            self.__semester = ''
            self.__matakuliah = ''
            self.__hari = ''
            self.__waktu = ''
            self.__ruang = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT k.id,k.ajaran,k.semester,m.matakuliah,k.hari,k.waktu,k.ruang FROM krs AS k, matakuliah AS m WHERE k.matakuliah=m.kode_matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result

    def getAllDataByUsername(self,username):
        self.conn = mydb()
        sql="SELECT k.id,k.ajaran,k.semester,m.matakuliah,k.hari,k.waktu,k.ruang FROM krs AS k, matakuliah AS m WHERE k.matakuliah=m.kode_matakuliah AND k.nim='" +str(username)+ "'"
        self.result = self.conn.findAll(sql)
        return self.result
