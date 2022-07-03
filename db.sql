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

CREATE TABLE mahasiswa (
  nim VARCHAR(10) PRIMARY KEY NOT NULL,
  nama VARCHAR(30) NOT NULL,
  prodi VARCHAR(5) NOT NULL REFERENCES prodi(kode_prodi),
  jk CHAR(1) NOT NULL,
  ttl VARCHAR(30),
  alamat VARCHAR(30),
  email VARCHAR(30),
  telepon VARCHAR(15)
);

CREATE TABLE krs (
  id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  ajaran VARCHAR(10) NOT NULL,
  semester CHAR(1) NOT NULL,
  nim VARCHAR(10) NOT NULL REFERENCES mahasiswa(nim),
  prodi VARCHAR(5) NOT NULL REFERENCES prodi(kode_prodi),
  matakuliah VARCHAR(5) NOT NULL REFERENCES matakuliah(kode_matakuliah),
  hari VARCHAR(10),
  waktu VARCHAR(10),
  ruang CHAR(3)
);
