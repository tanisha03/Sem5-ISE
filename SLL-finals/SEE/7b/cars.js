window.onload = function() {
  var teslaModels = [
    {
      model: "modelS",
      name: "Model S",
      price: 69200,
      year: 2016
    },
    {
      model: "modelX",
      name: "Model X",
      price: 83700,
      year: 2017
    },
    {
      model: "model3",
      name: "Model 3",
      price: 35000,
      year: 2017
    }
  ];

  teslaModels.forEach(function(item, index) {
    listElemet = document.createElement("th");
    listElemet.id = item.model;
    listElemet.innerHTML = item.name;
    document.getElementById("menu").appendChild(listElemet);
  });

  teslaModels.forEach(function(item, index) {
    var elem = document.getElementById(item.model);
    elem.onmouseover = function() {
      document.getElementById("data-table").removeAttribute("hidden");
      document.getElementById("model").innerHTML = item.name;
      document.getElementById("price").innerHTML = item.price;
      document.getElementById("year").innerHTML = item.year;
    };
  });
};
