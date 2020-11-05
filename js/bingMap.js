var map, infobox;
var infoboxTemplate =
  '<div class="customInfobox"><div class="title">{title}</div>{description}</div>';

function GetMap() {
  map = new Microsoft.Maps.Map("#myMap", {
    // showSearchBar: true,
    center: new Microsoft.Maps.Location(30.446109, 114.906618),
    zoom: 10,
  });
  //Attention!!! Microsoft.Maps.Location(lat, lon)，latitude first,then the longitude
  var point1 = new Microsoft.Maps.Location(30.581084, 114.3162); //Wuhan
  var point2 = new Microsoft.Maps.Location(30.216127, 115.050683); //Huangshi

  //create infobox information
  var title1 =
    '<div id="box-top"><h4 style="margin: 0; padding: 0%; font-size: 18px; text-align: center;">Events and Measures</h4></div>';
  description1 =
    '<div id="box-center"><div id="things" style="float: left;">Policies and measures of Wuhan City</div></div>';
  description1 +=
    '<div id="box-bottom"><span id="r1">Wuhan announced the closure of the city</span><br><span id="r2">Two new hospitals, Huoshenshan and Leishenshan, were built two new hospitals</span></div>';

  var title2 =
    '<div id="box-top"><h4 style="margin: 0; padding: 0%; font-size: 18px; text-align: center;">Events and Measures</h4></div>';
  description2 =
    '<div id="box-center"><span id="things" style="float: left;">Policies and measures of Huangshi City</span></div>';
  description2 +=
    '<div id="box-bottom"><span id="r5">Suggest that Huangshi announces the closure of the city</span><br><span id="r6">Suggest building new hospitals in Huangshi</span></div> ';

  //Some HTML to add a close button to the infobox.
  var closeButton1 =
    '<a href="javascript:closeInfobox1()" class="customInfoboxCloseButton">X</a>';
  var closeButton2 =
    '<a href="javascript:closeInfobox2()" class="customInfoboxCloseButton">X</a>';

  infobox1 = new Microsoft.Maps.Infobox(point1, {
    // showPointer: true,
    // showCloseButton: true,
    // visible: false
    htmlContent:
      infoboxTemplate
        .replace("{title}", title1)
        .replace("{description}", description1) + closeButton1,
    // offset: new Microsoft.Maps.Point(0, -150)
  });
  //Assign the infobox to a map instance.
  infobox1.setMap(map);

  infobox2 = new Microsoft.Maps.Infobox(point2, {
    htmlContent:
      infoboxTemplate
        .replace("{title}", title2)
        .replace("{description}", description2) + closeButton2,
    // showPointer: true,
    // showCloseButton: true,
    // offset: new Microsoft.Maps.Point(0, -150)
  });
  //Assign the infobox to a map instance.
  infobox2.setMap(map);

  //create pushpins
  var pin1 = new Microsoft.Maps.Pushpin(point1, {
    icon: "/img/markerbig_select.png",
    // color: 'red',
    // anchor: new Microsoft.Maps.Point(12, 39),  //similar to offset
  });
  //Add the pushpin to the map
  map.entities.push(pin1);

  var pin2 = new Microsoft.Maps.Pushpin(point2, {
    icon: "/img/marker-icon.png",
    // anchor: new Microsoft.Maps.Point(12, 39),
  });
  map.entities.push(pin2);

  Microsoft.Maps.Events.addHandler(pin1, "click", function () {
    showInfobox1("pushpinClick");
  });
  Microsoft.Maps.Events.addHandler(pin2, "click", function () {
    showInfobox2("pushpinClick");
  });
}
function closeInfobox1() {
  infobox1.setOptions({ visible: false });
}
function closeInfobox2() {
  infobox2.setOptions({ visible: false });
}

function showInfobox1() {
  infobox1.setOptions({ visible: true });
}
function showInfobox2() {
  infobox2.setOptions({ visible: true });
}
