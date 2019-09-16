 function divisibleby37(){
                var num1 = document.getElementById("firstnumber").value;
                if(num1%3===0 || num1%7===0)
                document.getElementById("result").innerHTML = "Yes";
                else
                document.getElementById("result").innerHTML = "No";
            }
