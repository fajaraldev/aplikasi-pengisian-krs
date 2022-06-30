from config.db import DBConnection as mydb

class Agenda:
    def __init__(self):
        self.__id= None
        self.__kode_agenda= None
        self.__nama_matakuliah= None
        self.__sks= None
        self.__nama_dosen= None
        self.__hari= None
        self.__kode_ruangan= None
        self.__waktu= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "Kode Agenda:" + self.__kode_agenda + "\n" + "Nama Matakuliah:" + self.__nama_matakuliah + "\n" + "SKS" + self.__sks + "\n" + "Nama Dosen:" + self.__nama_dosen + "\n" + "Hari:" + self.__hari + "\n" + "Kode Ruangan:" + self.__kode_ruangan + "\n" + "Waktu:" + self.__waktu + "\n"
        else:
            return self.__info

    @property
    def id(self):
        return self.__id

    @property
    def kode_agenda(self):
        return self.__kode_agenda

    @kode_agenda.setter
    def kode_agenda(self, value):
        self.__kode_agenda = value

    @property
    def nama_matakuliah(self):
        return self.__nama_matakuliah

    @nama_matakuliah.setter
    def nama_matakuliah(self, value):
        self.__nama_matakuliah = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    @property
    def nama_dosen(self):
        return self.__nama_dosen

    @nama_dosen.setter
    def nama_dosen(self, value):
        self.__nama_dosen = value

    @property
    def hari(self):
        return self.__hari

    @hari.setter
    def hari(self, value):
        self.__hari = value

    @property
    def kode_ruangan(self):
        return self.__kode_ruangan

    @kode_ruangan.setter
    def kode_ruangan(self, value):
        self.__kode_ruangan = value

    @property
    def waktu(self):
        return self.__waktu

    @waktu.setter
    def waktu(self, value):
        self.__waktu = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_agenda,self.__nama_matakuliah,self.__sks,self.__nama_dosen, self.__hari, self.__kode_ruangan, self.__waktu)
        sql="INSERT INTO agenda (kode_agenda,nama_matakuliah,sks,nama_dosen,hari,kode_ruangan,waktu) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_agenda,self.__nama_matakuliah,self.__sks,self.__nama_dosen, self.__hari, self.__kode_ruangan, self.__waktu)
        sql="UPDATE agenda SET kode_agenda=%s, nama_matakuliah=%s, sks=%s, nama_dosen=%s, hari=%s, kode_ruangan=%s, waktu=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKodeAgenda(self, kode_agenda):
        self.conn = mydb()
        val = (self.__kode_agenda,self.__nama_matakuliah,self.__sks,self.__nama_dosen, self.__hari, self.__kode_ruangan, self.__waktu, kode_agenda)
        sql="UPDATE agenda SET kode_agenda=%s, nama_matakuliah=%s, sks=%s, nama_dosen=%s, hari=%s, kode_ruangan=%s, waktu=%s WHERE kode_agenda=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM agenda WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKodeAgenda(self, kode_agenda):
        self.conn = mydb()
        sql="DELETE FROM agenda WHERE kode_agenda='" + str(kode_agenda) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql="SELECT * FROM agenda WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_agenda = self.result[1]
        self.__nama_matakuliah = self.result[2]
        self.__sks = self.result[3]
        self.__nama_dosen = self.result[4]
        self.__hari = self.result[5]
        self.__kode_ruangan = self.result[6]
        self.__waktu = self.result[7]
        self.conn.disconnect
        return self.result

    def getByKodeAgenda(self, kode_agenda):
        a=str(kode_agenda)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM agenda WHERE kode_agenda='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_agenda = self.result[1]
            self.__nama_matakuliah = self.result[2]
            self.__sks = self.result[3]
            self.__nama_dosen = self.result[4]
            self.__hari = self.result[5]
            self.__kode_ruangan = self.result[6]
            self.__waktu = self.result[7]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_agenda = ''
            self.__nama_matakuliah = ''
            self.__sks = ''
            self.__nama_dosen = ''
            self.__hari = ''
            self.__kode_ruangan = ''
            self.__waktu = ''
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM agenda"
        self.result = self.conn.findAll(sql)
        return self.result

'''mhs = agenda()
result = mhs.getAllData()
print(result)'''
