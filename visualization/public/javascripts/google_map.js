$(function() {

  function getmap(filename) {
    $.getJSON('json/'+filename, function(data) {    
      var zoom = 5.5;
      var center = new google.maps.LatLng(35.937143,127.558612);
      var mapOptions = {
        zoom: zoom,
        center: center,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      }
      var map = new google.maps.Map(document.getElementById('map'), mapOptions);

      var keys = Object.keys(data)
      var marker

      for (i=0; i<keys.length; i++) {
        var geo = data[keys[i]]["data"]["city"]["geo"]
        if (geo == null) continue
        marker = new google.maps.Marker({
          map: map,
          position: new google.maps.LatLng(geo[0], geo[1]),
          icon: pinSymbol(data[keys[i]]["data"]["aqi"]),
        })
      }
      
    })
  }
  getmap('201912170621_dict.txt');
  
  $(".move").click(function() {
    getmap("201912170650_dict.txt");
  });
  $(".prev").click(function() {
    getmap('201912170621_dict.txt');
  });

  function pinSymbol(aqi) {
    if (aqi >= 300) color = '#7F0024'
    else if (aqi >= 270) color = '#720056'
    else if (aqi >= 230) color = '#670099'
    else if (aqi >= 200) color = '#BE0066'
    else if (aqi >= 170) color = '#CD0033'
    else if (aqi >= 130)  color = '#FF6933'
    else if (aqi >= 100)  color = '#FF9933'
    else if (aqi >= 70) color = '#FFC433'
    else if (aqi >= 30) color = '#FFDE33'
    else color = '#079161'
    return {
        path: 'M 100, 100 m -75, 0 a 75,75 0 1,0 150,0 a 75,75 0 1,0 -150,0',
        fillColor: color,
        fillOpacity: 1,
        strokeColor: color,
        strokeWeight: 0,
        scale: 0.07,
    };
  }
   

  // google.maps.event.addListener(marker, 'click', function() {
  //   // move~
  // })

});