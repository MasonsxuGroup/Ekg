var map, infobox;
var infoboxTemplate =
  '<div class="customInfobox"><div class="title">{title}</div>{description}</div>';

function GetMap() {
  map = new Microsoft.Maps.Map("#myMap", {
    // showSearchBar: true,
    center: new Microsoft.Maps.Location(31.042611, 112.21733),
    zoom: 8,
  });
  //Attention!!! Microsoft.Maps.Location(lat, lon)，latitude first,then the longitude
  var point1 = new Microsoft.Maps.Location(31.2093161, 112.410562); //湖北省政策和举措
  var point2 = new Microsoft.Maps.Location(29.6368353, 109.6591744); //湖北省社会关注问题

  //create infobox information
  var title =
    '<div id="box-top"><h4 style="margin: 0; padding: 0%; font-size: 18px; text-align: center;">Events and Measures</h4></div>';

  description1 =
    '<div id="box-center"><span id="things" style="float: left;">Policies and measures of Hubei Province</span></div>';
  description1 +=
    '<div id="box-bottom"><span id="r1">Three leaders of the Hubei Provincial Red Cross were held accountable</span><br><span id="r2">Key users: CCTV news</span></div>';

//   var title2 =
//     '<div id="box-top"><h4 style="margin: 0; padding: 0%; font-size: 18px; text-align: center;">事件及措施</h4></div>';
  description2 =
    '<div id="box-center"><div id="things" style="float: left;">Social Concerns in Hubei Province</div></div>';
  description2 +=
    '<div id="box-bottom"><span id="r5">The use of materials by the Hubei Red Cross Society raises doubts</span><br><span id="r6">Key users: CCTV news</span></div>';

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
        .replace("{title}", title)
        .replace("{description}", description1) + closeButton1,
    // offset: new Microsoft.Maps.Point(0, -150)
  });
  //Assign the infobox to a map instance.
  infobox1.setMap(map);

  infobox2 = new Microsoft.Maps.Infobox(point2, {
    htmlContent:
      infoboxTemplate
        .replace("{title}", title)
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
