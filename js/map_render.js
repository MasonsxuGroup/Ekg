var map, infobox;
var infoboxTemplate1 =
  '<div class="customInfobox1"><div class="title">{title}</div>{description}{closeBtn}</div>';
var infoboxTemplate2 =
  '<div class="customInfobox2"><div class="title">{title}</div>{description}{closeBtn}</div>';
var infoboxTemplate3 =
  '<div class="customInfobox3"><div class="title">{title}</div>{description}{closeBtn}</div>';
var infoboxTemplate4 =
  '<div class="customInfobox4"><div class="title">{title}</div>{description}{closeBtn}</div>';

function GetMap() {
  map = new Microsoft.Maps.Map("#myMap", {
    // showSearchBar: true,
    center: new Microsoft.Maps.Location(34.75661, 113.649644),
    zoom: 6,
  });
  //Attention!!! Microsoft.Maps.Location(lat, lon)，latitude first,then the longitude
  var point1 = new Microsoft.Maps.Location(30.581084, 114.3162); //武汉市
  var point2 = new Microsoft.Maps.Location(31.209316, 112.410562); //湖北省
  var point3 = new Microsoft.Maps.Location(39.929986, 116.395645); //国家
  var point4 = new Microsoft.Maps.Location(34.976002, 105.124511); //其他省市
  //create infobox information
  var title =
    '<div id="box-top"><h4 style="margin: 0; padding: 0%; font-size: 18px; text-align: center;">Events and Measures</h4></div>';
  description1 =
    '<div id="box-center"><div id="things" style="float: left;">Policies and measures of Wuhan City</div></div>';
  description1 +=
    '<div id="box-bottom"><span id="wuhan_startTime">2019/12/31</span><br><span id="wuhan_events"></span><br><span style="margin-left:2px">影响力：</span><span id="wuhan_influence"></span></div>';

  description2 =
    '<div id="box-center"><span id="things" style="float: left;">Policies and measures of Hubei Province</span></div>';
  description2 +=
    '<div id="box-bottom"><span id="hubei_startTime">2019/12/31</span><br><span id="hubei_events"></span><br><span style="margin-left:2px">影响力：</span><span id="hubei_influence"></span></div> ';

  description3 =
    '<div id="box-center"><span id="things" style="float: left;">Policies and measures of nation</span></div>';
  description3 +=
    "<div id='box-bottom'><span id='nation_startTime'>2019/12/31</span><br><span id='nation_events'>🔺The National Health Commission's expert team arrived in Wuhan to check and verify the situation</span><br><span style='margin-left:2px'>影响力：</span><span id='nation_influence'>59.6</span></div>";

  description4 =
    '<div id="box-center"><span id="things" style="float: left;">Policies and measures of other provinces and cities</span></div>';
  description4 +=
    '<div id="box-bottom"><span id="others_startTime">2019/12/31</span><br><span id="others_events"></span><br><span style="margin-left:2px">影响力：</span><span id="others_influence"></span></div> ';

  //Some HTML to add a close button to the infobox.
  var closeButton1 =
    '<a href="javascript:closeInfobox(1)" class="customInfoboxCloseButton">X</a>';
  var closeButton2 =
    '<a href="javascript:closeInfobox(2)" class="customInfoboxCloseButton">X</a>';
  var closeButton3 =
    '<a href="javascript:closeInfobox(3)" class="customInfoboxCloseButton">X</a>';
  var closeButton4 =
    '<a href="javascript:closeInfobox(4)" class="customInfoboxCloseButton">X</a>';

  infobox1 = new Microsoft.Maps.Infobox(point1, {
    // visible: false, //不展示无数据提示框
    htmlContent: infoboxTemplate1
      .replace("{title}", title)
      .replace("{description}", description1)
      .replace("{closeBtn}", closeButton1),
  });
  //Assign the infobox to a map instance.
  infobox1.setMap(map);

  infobox2 = new Microsoft.Maps.Infobox(point2, {
    htmlContent: infoboxTemplate2
      .replace("{title}", title)
      .replace("{description}", description2)
      .replace("{closeBtn}", closeButton2),

    offset: new Microsoft.Maps.Point(-385, 0),
  });
  //Assign the infobox to a map instance.
  infobox2.setMap(map);

  infobox3 = new Microsoft.Maps.Infobox(point3, {
    htmlContent: infoboxTemplate3
      .replace("{title}", title)
      .replace("{description}", description3)
      .replace("{closeBtn}", closeButton3),
  });
  //Assign the infobox to a map instance.
  infobox3.setMap(map);

  infobox4 = new Microsoft.Maps.Infobox(point4, {
    htmlContent: infoboxTemplate4
      .replace("{title}", title)
      .replace("{description}", description4)
      .replace("{closeBtn}", closeButton4),
  });
  //Assign the infobox to a map instance.
  infobox4.setMap(map);

  //create pushpins
  var pin1 = new Microsoft.Maps.Pushpin(point1, {
    icon: "/img/markerbig_select.png",
  });
  //Add the pushpin to the map
  map.entities.push(pin1);

  var pin2 = new Microsoft.Maps.Pushpin(point2, {
    icon: "/img/marker-icon.png",
  });
  map.entities.push(pin2);

  var pin3 = new Microsoft.Maps.Pushpin(point3, {
    icon: "/img/marker.png",
  });
  map.entities.push(pin3);

  var pin4 = new Microsoft.Maps.Pushpin(point4, {
    icon: "/img/markerbig.png",
  });
  map.entities.push(pin4);

  Microsoft.Maps.Events.addHandler(pin1, "click", function () {
    showInfobox(1);
  });
  Microsoft.Maps.Events.addHandler(pin2, "click", function () {
    showInfobox(2);
  });
  Microsoft.Maps.Events.addHandler(pin3, "click", function () {
    showInfobox(3);
  });
  Microsoft.Maps.Events.addHandler(pin4, "click", function () {
    showInfobox(4);
  });
}
function closeInfobox(n) {
  switch (n) {
    case 1:
      infobox1.setOptions({ visible: false });
      break;
    case 2:
      infobox2.setOptions({ visible: false });
      break;
    case 3:
      infobox3.setOptions({ visible: false });
      break;
    case 4:
      infobox4.setOptions({ visible: false });
      break;
  }
}
function showInfobox(n) {
  switch (n) {
    case 1:
      infobox1.setOptions({ visible: true });
      document.getElementsByClassName("customInfobox1")[0].style.display =
        "block";
      break;
    case 2:
      infobox2.setOptions({ visible: true });
      document.getElementsByClassName("customInfobox2")[0].style.display =
        "block";
      break;
    case 3:
      infobox3.setOptions({ visible: true });
      document.getElementsByClassName("customInfobox3")[0].style.display =
        "block";
      break;
    case 4:
      infobox4.setOptions({ visible: true });
      document.getElementsByClassName("customInfobox4")[0].style.display =
        "block";
      break;
  }
}
