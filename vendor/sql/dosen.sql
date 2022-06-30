
DROP TABLE IF EXISTS "public"."dosen";
CREATE TABLE "public"."dosen" (
  "iddosen" serial primary key NOT NULL,
  "kode_dosen" varchar(10) NOT NULL,
  "nama" varchar(20) NOT NULL,
  "jk" char(1) NOT NULL,
  "email" varchar(30) NOT NULL
);

--
-- Dumping data for table `dosen`
--

INSERT INTO "public"."dosen" VALUES
(1, '001', 'Baharudin, M.Kom', 'L', 'baharudin@gmail.com');
