from config.db import DBConnection as mydb

class Krs:

    def __init__(self):
        self.__kode_transaksi=None
        self.__tahun_akademik=None
        self.__nim=None
        self.__tanggal=None
        self.__prodi=None
        self.__semester=None
        self.__mk_1=None
        self.__mk_2=None
        self.__mk_3=None
        self.__mk_4=None
        self.__mk_5=None
        self.__mk_6=None
        self.__mk_7=None
        self.__mk_8=None
        self.__mk_9=None
        self.__total_sks=None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def kode_transaksi(self):
        return self.__kode_transaksi

    @kode_transaksi.setter
    def kode_transaksi(self, value):
        self.__kode_transaksi = value

    @property
    def tahun_akademik(self):
        return self.__tahun_akademik

    @tahun_akademik.setter
    def tahun_akademik(self, value):
        self.__tahun_akademik = value

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value

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

    @property
    def mk_1(self):
        return self.__mk_1

    @mk_1.setter
    def mk_1(self, value):
        self.__mk_1 = value

    @property
    def mk_2(self):
        return self.__mk_2

    @mk_2.setter
    def mk_2(self, value):
        self.__mk_2 = value

    @property
    def mk_3(self):
        return self.__mk_3

    @mk_3.setter
    def mk_3(self, value):
        self.__mk_3 = value

    @property
    def mk_4(self):
        return self.__mk_4

    @mk_4.setter
    def mk_4(self, value):
        self.__mk_4 = value

    @property
    def mk_5(self):
        return self.__mk_5

    @mk_5.setter
    def mk_5(self, value):
        self.__mk_5 = value

    @property
    def mk_6(self):
        return self.__mk_6

    @mk_6.setter
    def mk_6(self, value):
        self.__mk_6 = value

    @property
    def mk_7(self):
        return self.__mk_7

    @mk_7.setter
    def mk_7(self, value):
        self.__mk_7 = value

    @property
    def mk_8(self):
        return self.__mk_8

    @mk_8.setter
    def mk_8(self, value):
        self.__mk_8 = value

    @property
    def mk_9(self):
        return self.__mk_9

    @mk_9.setter
    def mk_9(self, value):
        self.__mk_9 = value

    @property
    def total_sks(self):
        return self.__total_sks

    @total_sks.setter
    def total_sks(self, value):
        self.__total_sks = value

    # user
    def getProdiByNim(self,nim):
        self.conn = mydb()
        sql="SELECT nim,prodi FROM mahasiswa WHERE nim='" + str(nim) + "'"
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
        val = (self.__kode_transaksi,self.__tahun_akademik,self.__nim,self.__tanggal,self.__prodi,self.__semester,self.__mk_1,self.__mk_2,self.__mk_3,self.__mk_4,self.__mk_5,self.__mk_6,self.__mk_7,self.__mk_8,self.__mk_9,self.__total_sks)
        sql="INSERT INTO krs (kode_transaksi,tahun_akademik,nim,tanggal,prodi,semester,mk_1,mk_2,mk_3,mk_4,mk_5,mk_6,mk_7,mk_8,mk_9,total_sks) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def updateByKodeTransaksi(self, kode_transaksi):
        self.conn = mydb()
        val = (self.__tahun_akademik,self.__nim,self.__tanggal,self.__prodi,self.__semester,self.__mk_1,self.__mk_2,self.__mk_3,self.__mk_4,self.__mk_5,self.__mk_6,self.__mk_7,self.__mk_8,self.__mk_9,self.__total_sks,kode_transaksi)
        sql="UPDATE krs SET tahun_akademik=%s,nim=%s,tanggal=%s,prodi=%s,semester=%s,mk_1=%s,mk_2=%s,mk_3=%s,mk_4=%s,mk_5=%s,mk_6=%s,mk_7=%s,mk_8=%s,mk_9=%s,total_sks=%s WHERE kode_transaksi=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def deleteByKodeTransaksi(self, kode_transaksi):
        self.conn = mydb()
        sql="DELETE FROM krs WHERE kode_transaksi='" + str(kode_transaksi) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    # admin
    def getKrsByKodeTransaksi(self, kode_transaksi):
        self.conn = mydb()
        sql="SELECT * FROM krs WHERE kode_transaksi=" + str(kode_transaksi)
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_transaksi = self.result[0]
            self.__tahun_akademik = self.result[1]
            self.__nim = self.result[2]
            self.__tanggal = self.result[3]
            self.__prodi = self.result[4]
            self.__semester = self.result[5]
            self.__mk_1 = self.result[6]
            self.__mk_2 = self.result[7]
            self.__mk_3 = self.result[8]
            self.__mk_4 = self.result[9]
            self.__mk_5 = self.result[10]
            self.__mk_6 = self.result[11]
            self.__mk_7 = self.result[12]
            self.__mk_8 = self.result[13]
            self.__mk_9 = self.result[14]
            self.__total_sks = self.result[15]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_transaksi = ''
            self.__tahun_akademik = ''
            self.__nim = ''
            self.__tanggal = ''
            self.__prodi = ''
            self.__semester = ''
            self.__mk_1 = ''
            self.__mk_2 = ''
            self.__mk_3 = ''
            self.__mk_4 = ''
            self.__mk_5 = ''
            self.__mk_6 = ''
            self.__mk_7 = ''
            self.__mk_8 = ''
            self.__mk_9 = ''
            self.__total_sks = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    # user
    def getKrsByKodeTransaksiAndNim(self, kode_transaksi, nim):
        self.conn = mydb()
        sql="SELECT * FROM krs WHERE kode_transaksi='" + str(kode_transaksi) + "' AND nim='"+ str(nim) +"'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_transaksi = self.result[0]
            self.__tahun_akademik = self.result[1]
            self.__nim = self.result[2]
            self.__tanggal = self.result[3]
            self.__prodi = self.result[4]
            self.__semester = self.result[5]
            self.__mk_1 = self.result[6]
            self.__mk_2 = self.result[7]
            self.__mk_3 = self.result[8]
            self.__mk_4 = self.result[9]
            self.__mk_5 = self.result[10]
            self.__mk_6 = self.result[11]
            self.__mk_7 = self.result[12]
            self.__mk_8 = self.result[13]
            self.__mk_9 = self.result[14]
            self.__total_sks = self.result[15]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_transaksi = ''
            self.__tahun_akademik = ''
            self.__nim = ''
            self.__tanggal = ''
            self.__prodi = ''
            self.__semester = ''
            self.__mk_1 = ''
            self.__mk_2 = ''
            self.__mk_3 = ''
            self.__mk_4 = ''
            self.__mk_5 = ''
            self.__mk_6 = ''
            self.__mk_7 = ''
            self.__mk_8 = ''
            self.__mk_9 = ''
            self.__total_sks = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    # user
    def getAllKrsByNim(self,nim):
        self.conn = mydb()
        sql="SELECT * FROM krs WHERE nim='" +str(nim)+ "'"
        self.result = self.conn.findAll(sql)
        return self.result

    # admin
    def getAllKrs(self):
        self.conn = mydb()
        sql="SELECT * FROM krs limit 100"
        self.result = self.conn.findAll(sql)
        return self.result
