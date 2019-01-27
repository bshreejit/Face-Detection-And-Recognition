--
-- File generated with SQLiteStudio v3.2.1 on Sun Aug 12 21:43:14 2018
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: detectionInfo
CREATE TABLE detectionInfo (Id INTEGER, Name VARCHAR2 (50), Post VARCHAR2 (50), Faculty VARCHAR2 (50), emailId VARCHAR2 (70));
INSERT INTO detectionInfo (Id, Name, Post, Faculty, emailId) VALUES (1, 'Shreejit', 'Student', 'BCt', 'bshreejit@gmail.com');

-- Table: peopleInfo
CREATE TABLE peopleInfo (Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR2 (50) NOT NULL, Post VARCHAR2 (50), Faculty VARCHAR2 (50), emailId VARCHAR2 (70), Address VARCHAR2 (70), "Contact Number" NUMERIC (50));
INSERT INTO peopleInfo (Id, Name, Post, Faculty, emailId, Address, "Contact Number") VALUES (1, 'Shreejit', 'Student', 'BCt', 'bshreejit@gmail.com', NULL, NULL);
INSERT INTO peopleInfo (Id, Name, Post, Faculty, emailId, Address, "Contact Number") VALUES (3, 'Younesh', 'CEO', 'BCT', 'you@gmail.com', NULL, NULL);
INSERT INTO peopleInfo (Id, Name, Post, Faculty, emailId, Address, "Contact Number") VALUES (4, 'aayesha', 'student', 'bct', 'abc@gmail.com', NULL, NULL);
INSERT INTO peopleInfo (Id, Name, Post, Faculty, emailId, Address, "Contact Number") VALUES (5, 'Bibek Khadka', 'Student', 'BCT', 'Bebeck1996@gmail.com', NULL, NULL);
INSERT INTO peopleInfo (Id, Name, Post, Faculty, emailId, Address, "Contact Number") VALUES (31, 'Richa', 'Student', 'BCT', 'richa@gmail.com', NULL, NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
