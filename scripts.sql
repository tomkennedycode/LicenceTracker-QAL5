-- SQLite
DELETE FROM licence_licencetype;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='licence_licencetype';
INSERT INTO licence_licencetype (name) VALUES ('Microsoft Office'), ('Visual Studio Professional'), ('Resharper standard'), ('Resharper professional'), ('Resharper ultimate'), ('JetBrains'), ('Telerik UI for WPF'), ('Visual Studio Test Professional'), ('Visio'), ('Tableau');

-- SQLite
DELETE FROM licence_licencestatus;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='licence_licencestatus';
INSERT INTO licence_licencestatus (type) VALUES ('Assigned'), ('Unassigned'), ('Assignment in progress');

-- SQLite
DELETE FROM licence_licence;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='licence_licence';
