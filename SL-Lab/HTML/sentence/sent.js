function find(){
    var str1 = document.getElementById('input').value
    var listtxt = str1.split(" ")
    var max = 0
    listtxt.forEach(function (item, index) {
        if(item.length>max)
        max = item.length
      });
      document.getElementById('res').innerHTML = max
}
