-- SQLite
DELETE FROM licence_licencetype;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='licence_licencetype';
INSERT INTO licence_licencetype (name) VALUES ('Microsoft Office'), ('Visual Studio Professional'), ('Resharper standard'), ('Resharper professional'), ('JetBrains'), ('Telerik UI for WPF');

-- SQLite
DELETE FROM licence_licence;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='licence_licence';
