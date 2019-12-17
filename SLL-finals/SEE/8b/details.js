window.onload = function() {
  var details = {
    name: "Shyam Singh",
    aadhar: 123632563163123,
    labtests: ["Blood test", "X-ray"]
  };
  var hospitals = {
    name: "Apollo Hospital",
    location: "New Delhi"
  };

  var a = document.getElementById("hospital");
  a.innerHTML = hospitals["name"] + " : " + hospitals["location"];
  var b = document.getElementById("patient");
  b.addEventListener("mouseover", function(e) {
    e.target.style.color = "orange";
    var c = document.getElementById("details");
    c.innerHTML = details["name"] + " : " + details["aadhar"];
    var test = "";
    details["labtests"].forEach(function(a) {
      test += a + "    ";
    });
    var d = document.getElementById("tests");
    d.innerHTML = test;
  });
};
