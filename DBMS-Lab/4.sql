CREATE TABLE PARTT
 (
 PNO VARCHAR(6) NOT NULL,
 PNAME VARCHAR(10) ,
 COLOUR VARCHAR(10),
 PRIMARY KEY(PNO)
 );

 CREATE TABLE WAREHOUSE
 (
 WNO VARCHAR(6) NOT NULL,
 WNAME VARCHAR(10),
 CITY VARCHAR(10),
 PRIMARY KEY(WNO)
 );

 CREATE TABLE SHIPMENT
 (
 PNO VARCHAR(6),
 WNO VARCHAR(6),
 QUANTITY NUMBER,
 DATEE DATE ,
 FOREIGN KEY(PNO) REFERENCES PARTT(PNO) ON DELETE CASCADE,
 FOREIGN KEY(WNO) REFERENCES WAREHOUSE(WNO) ON DELETE CASCADE
 );


 INSERT INTO PARTT VALUES('01','ABC','RED');
 INSERT INTO PARTT VALUES('02','DEF','BLUE');
 INSERT INTO PARTT VALUES('03','LMN','GREEN');
 INSERT INTO PARTT VALUES('04','PQR','YELLOW');
 INSERT INTO PARTT VALUES('05','XYZ','PINK');

 INSERT INTO WAREHOUSE VALUES('10','AAA','KUMTA');
 INSERT INTO WAREHOUSE VALUES('20','BBB','MUMBAI');
 INSERT INTO WAREHOUSE VALUES('30','CCC','BANGALORE');
 INSERT INTO WAREHOUSE VALUES('40','DDD','UDUPI');
 INSERT INTO WAREHOUSE VALUES('50','EEE','KARWAR');


 SELECT * FROM PARTT;

 SELECT * FROM WAREHOUSE;

 
 INSERT INTO SHIPMENTS VALUES('01','20','300','28-FEB-2013');
 INSERT INTO SHIPMENTS VALUES('02','30','400','30-JAN-2013');
 INSERT INTO SHIPMENTS VALUES('03','10','00','31-JAN-2013');
 INSERT INTO SHIPMENTS VALUES('04','40','600','31-MARCH-2013');
 INSERT INTO SHIPMENTS VALUES('05','50','100','31-DEC-2013');

 SELECT * FROM SHIPMENTS;


 SELECT WNAME FROM WAREHOUSE
 WHERE WNO IN(SELECT WNO FROM SHIPMENTS WHERE PNO=(SELECT PNO FROM PARTT WHERE COLOUR='RED'));

 SELECT PNO,WNAME
 FROM SHIPMENTS s join WAREHOUSE w
 on(s.WNO=w.WNO);

 SELECT COUNT(PNO),WNO 
 FROM SHIPMENTS 
 GROUP BY WNO;
