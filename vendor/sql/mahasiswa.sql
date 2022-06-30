-- ----------------------------
-- Table structure for mahasiswa
-- ----------------------------
CREATE TABLE "public"."mahasiswa" (
  "id" serial primary key NOT NULL,
  "nim" varchar(10) NOT NULL,
  "nama" varchar(50) NOT NULL,
  "jk" char(1) NOT NULL,
  "kode_prodi" varchar(10) NOT NULL
);

-- ----------------------------
-- Records of mahasiswa
-- ----------------------------
INSERT INTO "public"."mahasiswa" VALUES (2, '2222', 'Fina Wijaya', 'P', 'IND');
INSERT INTO "public"."mahasiswa" VALUES (3, '1111', 'Ahmad Bajuri', 'L', 'TIF');
