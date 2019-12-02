set serveroutput on
DECLARE 
prim Number := &Number1;
loopvar Number :=0;
flag Number :=0;

BEGIN
for loopvar in 2..prim-1 loop
if(mod(prim,loopvar)=0) then
flag:=1;
exit;
end if;
end loop;

if(flag=1) then
dbms_output.put_line('Not Prime');
else 
dbms_output.put_line('Prime');
end if;

END;
/
