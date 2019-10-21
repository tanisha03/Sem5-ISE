create table e(ssn varchar(6),name varchar(10),deptno int, primary key(ssn));

create table p (projectno varchar(10),projectarea varchar(20),primary key(projectno));

create table a(usn varchar(6),projectno varchar(10),foreign key(usn)references e(ssn),foreign key(projectno)references p(projectno));


insert into e values('01','abc',10);
insert into e values('02','xyz',20);
insert into e values('03','pqr',30);
insert into e values('04','lmn',40);


insert into p values('100','database');
insert into p values('200','network');
insert into p values('300','android');
insert into a values('01','100');


insert into a values('02','200');
insert into a values('03','300');
insert into a values('01','200');

select * from e;
 
select * from p;
  
select * from a;
  
select ssn from e where ssn=(select usn from a where projectno=(select projectno from p where projectarea='database'));
  
select count(ssn),deptno from e group by deptno;
  
update a set projectno='200' where usn='03';
select * from a;
