import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Matakuliah import Matakuliah
from classes.Prodi import Prodi
from classes.Krs import Krs
from classes.Users import userInfo
from GlobalVariable import GlobalVariable

qtcreator_file  = "ui/krsUser.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class KrsUserWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnGenerateForm.clicked.connect(self.setNimAndProdi)
        self.txtKodeTransaksi.returnPressed.connect(self.searchData)
        self.btnCariKrs.clicked.connect(self.searchData)
        self.btnCariProdi.clicked.connect(self.searchProdiInfo)
        self.btnCariMatakuliahBySemester.clicked.connect(self.getAllMatakuliah)
        self.btnSimpan.clicked.connect(self.saveData)
        self.btnClear.clicked.connect(self.clearEntry)
        self.btnHapus.clicked.connect(self.deleteData)
        self.btnShowAllData.clicked.connect(self.selectData)

        self.btnCariMk_1.clicked.connect(self.searchMk1)
        self.btnCariMk_2.clicked.connect(self.searchMk2)
        self.btnCariMk_3.clicked.connect(self.searchMk3)
        self.btnCariMk_4.clicked.connect(self.searchMk4)
        self.btnCariMk_5.clicked.connect(self.searchMk5)
        self.btnCariMk_6.clicked.connect(self.searchMk6)
        self.btnCariMk_7.clicked.connect(self.searchMk7)
        self.btnCariMk_8.clicked.connect(self.searchMk8)
        self.btnCariMk_9.clicked.connect(self.searchMk9)

        self.edit_mode=False
        self.btnHapus.setEnabled(False)
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

        # set data to cboKodeProdi form
        for x in g_var.prodi:
          self.cboKodeProdi.addItem(x[0])


    def setNimAndProdi(self):
        try:
            krs = Krs()
            nim=userInfo[1]

            # search process
            result = krs.getProdiByNim(nim)
            a = krs.affected
            if(a>0):
                self.txtNim.setText(result[0])
                self.cboKodeProdi.setCurrentText(result[1])
            else:
                self.txtProdi.setText('')
                self.cboKodeProdi.setCurrentText('')
                self.messagebox("INFO", "Data tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def selectData(self):
        try:
            krs = Krs()
            nim=userInfo[1]

            # Get all
            result = krs.getAllKrsByNim(nim)

            self.gridKrs.setHorizontalHeaderLabels(['Kode Transaksi', 'Tahun Akademik','NIM','Tanggal','Prodi','Semester','MK 1','MK 2','MK 3','MK 4','MK 5','MK 6','MK 7','MK 8','MK 9','Total SKS',])
            self.gridKrs.setRowCount(0)


            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridKrs.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridKrs.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")


    # search data for krs
    def searchData(self):
        try:
            krs = Krs()
            nim=userInfo[1]
            kode_transaksi=self.txtKodeTransaksi.text()

            # search process
            result = krs.getKrsByKodeTransaksiAndNim(kode_transaksi, nim)
            a = krs.affected
            if(a>0):
                self.tampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtTahunAkademik.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # save data for krs
    def saveData(self, MainWindow):
        try:
            krs = Krs()

            kode_transaksi=self.txtKodeTransaksi.text()
            tahun_akademik=self.txtTahunAkademik.text()
            nim=userInfo[1]
            tanggal=self.txtTanggal.date().toString("yyyy-MM-dd")
            prodi=self.cboKodeProdi.currentText()
            semester=self.cboSemester.currentText()
            mk_1=self.cboMk_1.currentText()
            mk_2=self.cboMk_2.currentText()
            mk_3=self.cboMk_3.currentText()
            mk_4=self.cboMk_4.currentText()
            mk_5=self.cboMk_5.currentText()
            mk_6=self.cboMk_6.currentText()
            mk_7=self.cboMk_7.currentText()
            mk_8=self.cboMk_8.currentText()
            mk_9=self.cboMk_9.currentText()
            total_sks=self.txtTotalSks.text()

            if(self.edit_mode==False):
                krs.kode_transaksi=kode_transaksi
                krs.tahun_akademik=tahun_akademik
                krs.nim=nim
                krs.tanggal=tanggal
                krs.prodi=prodi
                krs.semester=semester
                krs.mk_1=mk_1
                krs.mk_2=mk_2
                krs.mk_3=mk_3
                krs.mk_4=mk_4
                krs.mk_5=mk_5
                krs.mk_6=mk_6
                krs.mk_7=mk_7
                krs.mk_8=mk_8
                krs.mk_9=mk_9
                krs.total_sks=total_sks

                if(int(total_sks)>24):
                  self.messagebox("GAGAL", "Total KRS tidak boleh lebih dari 24!")
                else:
                  a = krs.simpan()
                  if(a>0):
                      self.messagebox("SUKSES", "Data KRS Tersimpan")
                  else:
                      self.messagebox("GAGAL", "Data KRS Gagal Tersimpan")

                  self.clearEntry(self)
                  self.selectData()
            elif(self.edit_mode==True):
                krs.tahun_akademik=tahun_akademik
                krs.nim=nim
                krs.tanggal=tanggal
                krs.prodi=prodi
                krs.semester=semester
                krs.mk_1=mk_1
                krs.mk_2=mk_2
                krs.mk_3=mk_3
                krs.mk_4=mk_4
                krs.mk_5=mk_5
                krs.mk_6=mk_6
                krs.mk_7=mk_7
                krs.mk_8=mk_8
                krs.mk_9=mk_9
                krs.total_sks=total_sks

                if(int(total_sks)>24):
                  self.messagebox("ERROR", "Total KRS tidak boleh lebih dari 24!")
                else:
                  a = krs.updateByKodeTransaksi(kode_transaksi)
                  if(a>0):
                      self.messagebox("SUKSES", "Data KRS Diperbarui")
                  else:
                      self.messagebox("GAGAL", "Data KRS Gagal Diperbarui")

                  self.clearEntry(self)
                  self.selectData()
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    # delete data for mahasiswa
    def deleteData(self, MainWindow):
        try:
            krs = Krs()
            kode_transaksi=self.txtKodeTransaksi.text()

            if(self.edit_mode==True):
                a = krs.deleteByKodeTransaksi(kode_transaksi)
                if(a>0):
                    self.messagebox("SUKSES", "Data KRS Dihapus")
                else:
                    self.messagebox("GAGAL", "Data KRS Gagal Dihapus")

                self.clearEntry(self)
                self.selectData()
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def tampilData(self,result):
        self.clearDataCboMk() # reset data cbo matakuliah

        self.txtKodeTransaksi.setText(result[0])
        self.txtTahunAkademik.setText(result[1])
        self.txtNim.setText(result[2])
        self.txtTanggal.setDate(result[3])
        self.cboKodeProdi.setCurrentText(result[4])
        self.cboSemester.setCurrentText(str(result[5]))
        self.cboMk_1.addItem(result[6])
        self.cboMk_1.setCurrentText(result[6])
        self.cboMk_2.addItem(result[7])
        self.cboMk_2.setCurrentText(result[7])
        self.cboMk_3.addItem(result[8])
        self.cboMk_3.setCurrentText(result[8])
        self.cboMk_4.addItem(result[9])
        self.cboMk_4.setCurrentText(result[9])
        self.cboMk_5.addItem(result[10])
        self.cboMk_5.setCurrentText(result[10])
        self.cboMk_6.addItem(result[11])
        self.cboMk_6.setCurrentText(result[11])
        self.cboMk_7.addItem(result[12])
        self.cboMk_7.setCurrentText(result[12])
        self.cboMk_8.addItem(result[13])
        self.cboMk_8.setCurrentText(result[13])
        self.cboMk_9.addItem(result[14])
        self.cboMk_9.setCurrentText(result[14])
        self.txtTotalSks.setText(str(result[15]))
        self.edit_mode=True
        # enable button
        self.btnSimpan.setEnabled(True)
        self.btnSimpan.setStyleSheet("color:white;  background-color : blue")
        self.btnHapus.setEnabled(True)
        self.btnHapus.setStyleSheet("color:white; background-color : red")

    def clearEntry(self, MainWindow):
        self.txtKodeTransaksi.setText('')
        self.txtTahunAkademik.setText('')
        self.txtNim.setText('')
        self.cboKodeProdi.setCurrentText('')
        self.txtProdi.setText('')
        self.cboSemester.setCurrentText('')
        self.clearDataCboMk()
        self.txtTotalSks.setText('')
        self.clearDataCboMk()

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

    def addDataCboMk(self,data):
      self.cboMk_1.addItem(data)
      self.cboMk_2.addItem(data)
      self.cboMk_3.addItem(data)
      self.cboMk_4.addItem(data)
      self.cboMk_5.addItem(data)
      self.cboMk_6.addItem(data)
      self.cboMk_7.addItem(data)
      self.cboMk_8.addItem(data)
      self.cboMk_9.addItem(data)

    def clearDataCboMk(self):
      self.cboMk_1.clear()
      self.cboMk_2.clear()
      self.cboMk_3.clear()
      self.cboMk_4.clear()
      self.cboMk_5.clear()
      self.cboMk_6.clear()
      self.cboMk_7.clear()
      self.cboMk_8.clear()
      self.cboMk_9.clear()

      self.txtMk_1.clear()
      self.txtMk_2.clear()
      self.txtMk_3.clear()
      self.txtMk_4.clear()
      self.txtMk_5.clear()
      self.txtMk_6.clear()
      self.txtMk_7.clear()
      self.txtMk_8.clear()
      self.txtMk_9.clear()

      self.txtSksMk_1.clear()
      self.txtSksMk_2.clear()
      self.txtSksMk_3.clear()
      self.txtSksMk_4.clear()
      self.txtSksMk_5.clear()
      self.txtSksMk_6.clear()
      self.txtSksMk_7.clear()
      self.txtSksMk_8.clear()
      self.txtSksMk_9.clear()

    def searchProdiInfo(self):
        try:
            prd = Prodi()
            kode_prodi=self.cboKodeProdi.currentText()

            # search process
            result = prd.getByKodeProdi(kode_prodi)
            a = prd.affected
            if(a>0):
                self.txtProdi.setText(prd.prodi.strip())
            else:
                self.txtProdi.setText('')
                self.messagebox("INFO", "Data tidak ditemukan")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    # search data matakuliah
    def getAllMatakuliah(self):
        try:
            prodi = self.cboKodeProdi.currentText()
            semester = self.cboSemester.currentText()
            g_var.getAllMatakuliahByProdiAndSemester(prodi, semester)
            self.clearDataCboMk()  # reset data cbo matakuliah
            a = g_var.affected
            if(a>0):
                self.addDataCboMk('')
                # set data to cboKodeProdi form
                for data in g_var.matakuliah:
                  self.addDataCboMk(data[0])
                self.messagebox("INFO", "Berhasil Mendapatkan Daftar Data Matakuliah!")
            else:
                self.messagebox("INFO", "Data Matakuliah tidak tersedia!")

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk1(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_1.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_1.setText(result[0])
                self.txtSksMk_1.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_1.setText('')
                self.txtSksMk_1.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk2(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_2.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_2.setText(result[0])
                self.txtSksMk_2.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_2.setText('')
                self.txtSksMk_2.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk3(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_3.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_3.setText(result[0])
                self.txtSksMk_3.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_3.setText('')
                self.txtSksMk_3.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk4(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_4.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_4.setText(result[0])
                self.txtSksMk_4.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_4.setText('')
                self.txtSksMk_4.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk5(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_5.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_5.setText(result[0])
                self.txtSksMk_5.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_5.setText('')
                self.txtSksMk_5.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk6(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_6.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_6.setText(result[0])
                self.txtSksMk_6.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_6.setText('')
                self.txtSksMk_6.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk7(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_7.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_7.setText(result[0])
                self.txtSksMk_7.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_7.setText('')
                self.txtSksMk_7.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk8(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_8.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_8.setText(result[0])
                self.txtSksMk_8.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_8.setText('')
                self.txtSksMk_8.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def searchMk9(self):
        try:
            mk = Matakuliah()
            kode_matakuliah = self.cboMk_9.currentText()
            result=mk.getMatakuliahAndSksByKodeMatakuliah(kode_matakuliah)
            a = mk.affected
            if(a!=0):
                self.txtMk_9.setText(result[0])
                self.txtSksMk_9.setText(str(result[1]))
            else:
                self.messagebox("INFO", "Matakuliah tidak ditemukan")
                self.txtMk_9.setText('')
                self.txtSksMk_9.setText('')

        except Exception as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    g_var.getAllProdi()
    window = KrsUserWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    g_var = GlobalVariable()
    g_var.getAllProdi()
    window = KrsUserWindow()
