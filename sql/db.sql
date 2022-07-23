CREATE TABLE users (
  user_id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  role_id SMALLINT(1) NOT NULL REFERENCES roles(role_id),
  username VARCHAR(30) UNIQUE NOT NULL,
  password VARCHAR(50) NOT NULL
);

CREATE TABLE roles(
  role_id SMALLINT(1) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  role_name VARCHAR(30) NOT NULL
);

CREATE TABLE prodi (
  kode_prodi VARCHAR(5) PRIMARY KEY NOT NULL,
  prodi VARCHAR(30) NOT NULL
);

CREATE TABLE matakuliah (
  kode_matakuliah VARCHAR(5) PRIMARY KEY NOT NULL,
  matakuliah VARCHAR(30) NOT NULL,
  sks SMALLINT(1) NOT NULL,
  prodi VARCHAR(5) NOT NULL REFERENCES prodi(kode_prodi),
  semester SMALLINT(1) NOT NULL
);

CREATE TABLE dosen (
  nidn VARCHAR(10) PRIMARY KEY NOT NULL,
  nama VARCHAR(30) NOT NULL,
  jk CHAR(1) NOT NULL,
  ttl VARCHAR(30),
  alamat VARCHAR(30),
  email VARCHAR(30),
  telepon VARCHAR(15)
);

CREATE TABLE mahasiswa (
  nim VARCHAR(10) PRIMARY KEY NOT NULL,
  nama VARCHAR(30) NOT NULL,
  prodi VARCHAR(5) NOT NULL REFERENCES prodi(kode_prodi),
  jk CHAR(1) NOT NULL,
  ttl VARCHAR(30),
  alamat VARCHAR(30),
  email VARCHAR(30),
  telepon VARCHAR(15),
  kode_wali VARCHAR(10) NOT NULL REFERENCES dosen(nidn),
);

CREATE TABLE krs (
  kode_transaksi VARCHAR(11) PRIMARY KEY NOT NULL,
  tahun_akademik VARCHAR(10) NOT NULL,
  nim VARCHAR(10) NOT NULL REFERENCES mahasiswa(nim),
  tanggal DATE NOT NULL,
  prodi VARCHAR(5) NOT NULL REFERENCES prodi(kode_prodi),
  semester SMALLINT(1) NOT NULL,
  mk_1 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_2 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_3 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_4 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_5 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_6 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_7 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_8 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  mk_9 VARCHAR(5) REFERENCES matakuliah(kode_matakuliah),
  total_sks SMALLINT(2) NOT NULL
);
