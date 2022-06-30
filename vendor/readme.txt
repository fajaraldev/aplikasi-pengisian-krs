Folder yang isinya boleh diedit:
1. classes = berisi file class dari setiap tabel
2. config = file local.env berisi koneksi database
3. forms = berisi file py tampilan window untuk memanggil file ui (design)
4. panel = berisi file py untuk memanggil file py dari folder form
5. ui = berisi file ui (design)
6. icons = berisi file gambar (png)

Langkah praktikum:
1. Siapkan tabel di postgresql berikut isinya
2. Buat sebuah class untuk tabel tsb beri nama: Namatabel.py
   cth: Mahasiswa.py (nama sebuah class sengaja huruf awalnya kapital)
3. Desain Form untuk tabel tersebut di Qt Designer
   simpan hasilnya dgn nama : namatabel.ui
   cth: mahasiswa.ui
4. Buat file py untuk memanggil file ui, beri nama : frmNamatabel.py
   cth: frmMahasiswa.py (nama file ini sengaja diawali dengan frm diikuti nama tabelnya 
   dgn diawali nama tabel huruf kapital)

5. Copy ke-3 file diatas dgn ketentuan sbg berikut:
   Nama File      	    Nama Folder
   Mahasiswa.py  	         classes
   mahasiswa.ui		      ui
   frmMahasiswa.py	      forms
   
6. Koneksi database
   Edit file: config/local.env
7. Cari gambar icon di flaticons.com
   simpan file gambar (png) di dalam folder icons, 
   sesuaikan nama filenya sehingga sama dengan nama tabel.
8. Edit file GUI/Icons.py untuk menambahkan icon baru (lihat baris ke-32)

9. Edit file: forms/MainWindow.py untuk menambahkan tombol
   pada Ribbon Menu (lihat bagian # action #)

9. Test Run:
   jalankan file : main.py

Catatan:
Perlu menyiapkan 1 file gambar (png) sebagai icon untuk setiap modul CRUD tabel,
cth: jika Anda membuat CRUD untuk tabel: mahasiswa, matakuliah, dan dosen
maka Anda harus menyiapkan 3 buah file gambar (png) dengan ukuran minimal 64x64 px
sebagai icon dari ke-3 modul tersebut dan simpan di folder icons.

Icon dapat dicari serta di donlot di:
https://www.flaticon.com
