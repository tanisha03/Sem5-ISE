window.onload = function() {
  var authors = [
    {
      name: "John",
      country: "USA",
      story: "The Lost World",
      year: "1999"
    },
    {
      name: "Green",
      country: "Australia",
      story: "Fault in our Stars",
      year: "2010"
    },
    {
      name: "Paulo",
      country: "USA",
      story: "Alchemist",
      year: "1999"
    },
    {
      name: "Khalid",
      country: "Afghanistan",
      story: "The Kite Runner",
      year: "2005"
    }
  ];
  authors.forEach(function(item, index) {
    console.log(item);
    if (index < 2) {
      listElemet = document.createElement("tr");
      la = document.createElement("td");
      la.innerHTML = item.name;
      listElemet.appendChild(la);
      la = document.createElement("td");
      la.innerHTML = item.country;
      listElemet.appendChild(la);
      la = document.createElement("td");
      la.innerHTML = item.story;
      listElemet.appendChild(la);
      la = document.createElement("td");
      la.innerHTML = item.year;
      listElemet.appendChild(la);
      console.log(listElemet);
      document.getElementById("menu").appendChild(listElemet);
    } else {
      ab = document.createElement("div");
      ab.innerHTML =
        item.name +
        "   " +
        item.country +
        "   " +
        item.story +
        "   " +
        item.year;
      document.getElementById("a3").appendChild(ab);
    }
  });
};
