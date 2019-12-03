DECLARE 
num1 Number:=0;
num2 Number:=1;
cnt Number:=6;
sum1 Number:=0;

BEGIN
dbms_output.put_line(num1);
dbms_output.put_line(num2);
while cnt!=0 loop
sum1 := num1 + num2;
dbms_output.put_line(sum1);
num1 := num2;
num2 := sum1;
cnt := cnt-1;
end loop;

END;
/
