function check(x) {
  var grade = "";
  if (x >= 90) grade = "S+";
  else if (x >= 80) grade = "S";
  else if (x >= 70) grade = "A";
  else if (x >= 60) grade = "B";
  else if (x >= 50) grade = "C";
  else if (x >= 40) grade = "D";
  else grade = "F";
  return grade;
}
function grad() {
  var a = Number(document.getElementById("gra1").value);
  var b = Number(document.getElementById("gra2").value);
  var c = Number(document.getElementById("gra3").value);
  g = check(a);
  console.log(g);
  document.getElementById("res1").innerHTML = "Sub1:  "+g;
  g = check(b);
  console.log(g);

  document.getElementById("res2").innerHTML = "Sub2:  "+g;
  g = check(c);
  console.log(g);

  document.getElementById("res3").innerHTML = "Sub3:  "+g;
}
