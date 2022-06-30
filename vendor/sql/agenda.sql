DROP TABLE IF EXISTS "public"."agenda";
CREATE TABLE "public"."agenda" (
  "id" serial primary key NOT NULL,
  "kode_agenda" varchar(10) NOT NULL,
  "nama_matakuliah" varchar(20) NOT NULL,
  "sks" varchar(11) NOT NULL,
  "nama_dosen" varchar(20) NOT NULL,
  "hari" varchar(10) NOT NULL,
  "kode_ruangan" varchar(10) NOT NULL,
  "waktu" varchar(10) NOT NULL
);

--
-- Dumping data for table `agenda`
--


INSERT INTO "public"."agenda" VALUES (2, '01', 'PBO 2', 3, 'Andrew', 'Senin', '2020', '10:45');
