create table books
 (
 ISBN varchar(10),
 Title varchar(10),
 Author varchar(10),
 Publisher varchar(10),
 primary key(ISBN)
 );

 Insert into books values(
 ISBN TITLE AUTHOR PUBLISHER
 001 T1 A1 P1
 002 T2 A2 P2
 003 T3 A3 P3
 004 T4 A4 P4
 005 T5 A5 P5

 create table student1
 (
 usn varchar(10),
name varchar(10),
 sem int,
 dept varchar(3),
 primary key(usn)
 );

 Insert into student1 values(

 SN NAME  SEM DEPT
 111 aaa 3  ISE
 222 bbb 4 CSE
 333 ccc 3  CSE
 444 ddd 4 ISE
 555 eee 4  ISE
);

 create table borrow
 (
 ISBN varchar(10),
 usn varchar(10),
 dates varchar(10),
 foreign key(ISBN) references books(ISBN),
 foreign key(usn) references student1(usn)
);

 Insert into borrow values(

 ISBN  USN DATES
 001 222 1/2/13
002 333 2/2/13
 003 111 3/2/13
 005 444 4/2/13
003 555   5/2/13

 select NAME from student1
 where USN=(select USN from borrow where ISBN='001');

select NAME from student1
 where USN=(select USN from borrow where ISBN=(select ISBN from books where TITLE='T2'));

select count(ISBN) from borrow
 group by USN;


-- MONGODB

>db.createCollection("LIBRARY")

>db.LIBRARY.insert({"ISBN":1122,"TITLE":'datbase',"AUTHOR":'ABC',"PUBLISHER":'selina',"SSN":2015,"date":'2017-05-29'})
>db.LIBRARY.insert({"ISBN":2233,"TITLE":'datbase',"AUTHOR":'DEF',"PUBLISHER":'mcgraw',"SSN":2016,"date":'2017-06-29' })
>db.LIBRARY.insert({"ISBN":3344,"TITLE":'dip',"AUTHOR":'GHI',"PUBLISHER":'gonzalez',"SSN":2017,"date":'2016-06-29' })
>db.LIBRARY.insert({"ISBN":3355,"TITLE":'os',"AUTHOR":'LKB',"PUBLISHER":'pearson',"SSN":2018,"date":'2016-06-01' })

>db.LIBRARY.find({"ISBN":1122},{"SSN":1,_id:0}).pretty()
>db.LIBRARY.find({"TITLE":'datbase'},{"SSN":1,_id:0}).pretty()