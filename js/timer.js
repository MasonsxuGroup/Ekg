var count = 0;
function btnControl() {
  ++count;
  if (count % 2 === 1) {
    $(".btn-control").removeClass("btn-play").addClass("btn-pause"); //点击次数为单时，播放
    document.getElementsByClassName("heatMapTimer")[0].style.visibility =
      "visible";
    // timeClick();
    // console.log(2);
  } else {
    $(".btn-control").removeClass("btn-pause").addClass("btn-play"); //点击次数为双时，暂停
    document.getElementsByClassName("heatMapTimer")[0].style.visibility =
      "hidden";
  }
}

function timeClick() {
  var cnt = 5;
  var play_cnt = 0;
  var timer;
  var index; //定义li选中状态时的索引
  $timeUl = $(".time-line");
  $timeLi = $(".time-line li");
  lenCount = $timeLi.length - 1; //去除第一个按钮li标签的长度
  var normal = []; //存放正常的索引
  //点击播放时间轴事件
  $timeUl.on("click", ".time-play", function () {
    if (play_cnt === 0) {
      $(this).removeClass("time-play").addClass("time-pause");
      index = Number($timeUl.find("li.active").attr("data-index")); //将字符串强制转换为数字类型
      timer = setInterval(function () {
        //判断当前索引的位置，如果在最后一位则从第一个时间点开始，反之则按顺序播放
        if (lenCount == index + 1) {
          $timeUl.find("li:eq('" + lenCount + "')").removeClass("active");
          $timeUl.find("li:eq(1)").addClass("active");
        } else {
          $(".time-line li.active")
            .next()
            .addClass("active")
            .siblings() //选择除本身以外的其他同级元素,,
            .removeClass("active");
        }
        $timeLi.each(function () {
          if ($(this).hasClass("active")) {
            index = Number($(this).attr("data-index")); //字符串转换为数字类型，索引从0开始
            normal.push(index); //获取当前active的点的索引并存入normal
            //用来判断是否正常轮播
            if (normal.length >= 2) {
              let ds1 = normal[normal.length - 1];
              let ds2 = normal[normal.length - 2]; //这里注意，js不能使用arr[-1]取最后一个值
              /*正常播放：如果倒数第一个数比倒数第二个数多1，
                或者倒数第一个为0（也即是第一个），倒数第二个数为5（也即是最后一个）
                都视为正常播放
               */
              if (ds1 == ds2 + 1 || (ds2 == 5 && ds1 == 0)) {
                cnt += 1;
              }
              /*非正常播放：正常播放时，用户点击了某一个点*/
              if (
                (ds1 > ds2 && ds1 - ds2 != 1) ||
                (ds1 < ds2 && ds2 - ds1 != 5)
              ) {
                cnt = cnt + ds1 - ds2;
              }
              //如果点击正在播放的点
              if (ds1 == ds2) {
                cnt = cnt;
              }
            } else {
              cnt += 1; //当播放点不足两个的时候
            }
          }
        });
        //添加圆点底下显示的数据
        axios.get("../data_pro_ed.json").then((res) => {
          let origin_data = res.data;
          let temp_type = []; //声明一个数组,用来存储同一时间，哪些['type']字段有数据
          // console.log(document.getElementById("time_0"));
          for (let i = 0; i < origin_data.length; i++) {
            try {
              if (index === 0 && cnt > 10 && cnt - 4 <= origin_data.length) {
                //index===0 => 播放到第一个点，cnt>10=>过了第一次循环播放
                //判断是否是第二次循环播放，并且是否播放到第一个点
                document.getElementById("time_0").innerHTML =
                  origin_data[cnt - 5]["startTime"];
                document.getElementById("time_1").innerHTML =
                  origin_data[cnt - 4]["startTime"];
                document.getElementById("time_2").innerHTML =
                  origin_data[cnt - 3]["startTime"];
                document.getElementById("time_3").innerHTML =
                  origin_data[cnt - 2]["startTime"];
                document.getElementById("time_4").innerHTML =
                  origin_data[cnt - 1]["startTime"];
                document.getElementById("time_5").innerHTML =
                  origin_data[cnt]["startTime"];
              }
            } catch (e) {
              console.log(e);
              //处理播放完时多余的点（也即没有数据的点）
              console.log(cnt);
              update_i = origin_data.length - cnt + 5; //求出从第update_i个点开始没有数据
              for (let j = update_i; j < 6; j++) {
                update_id = "time_" + j; //绑定i标签用
                update_class = "data_index_" + j; //绑定li标签用
                document.getElementById(update_id).style.visibility = "hidden";
                document.getElementsByClassName(
                  update_class
                )[0].style.visibility = "hidden"; //注意getElementsByClassName的用法，它返回的是一个集合
              }
            }
            if (cnt === origin_data.length + 4) {
              //播放完
              $(".time-btn").removeClass("time-pause").addClass("time-play"); //时间轴播放按钮样式转换
              play_cnt = 1;
              clearInterval(timer); //清除定时器
            }

            active = document.getElementsByClassName("active");
            act = active[0].innerText;
            document.getElementById("wuhan_startTime").innerHTML = act;
            document.getElementById("hubei_startTime").innerHTML = act;
            document.getElementById("nation_startTime").innerHTML = act;
            document.getElementById("others_startTime").innerHTML = act; //向提示跨里第一个span添加"startTime"
            if (act === origin_data[i]["startTime"]) {
              document.getElementById("wuhan_events").innerHTML = "";
              document.getElementById("wuhan_influence").innerHTML = "";
              document.getElementById("hubei_events").innerHTML = "";
              document.getElementById("hubei_influence").innerHTML = "";
              document.getElementById("nation_events").innerHTML = "";
              document.getElementById("nation_influence").innerHTML = "";
              document.getElementById("others_events").innerHTML = "";
              document.getElementById("others_influence").innerHTML = ""; //重写数据
              let events_data = origin_data[i]["events"];
              for (let j in events_data) {
                temp_type.push(events_data[j]["type"]);
                let measure_data = events_data[j]["measure"];
                for (let k in measure_data) {
                  console.log(typeof k);
                  if (
                    events_data[j]["type"] ===
                    "Policies and measures of Wuhan City"
                  ) {
                    //当天有武汉数据则写入，并且提示框显示
                    document.getElementsByClassName(
                      "customInfobox1"
                    )[0].style.display = "block";
                    document.getElementById("wuhan_events").innerHTML +=
                      "🔺" + measure_data[k].name; //   \x0A => \n 换行
                    document.getElementById("wuhan_influence").innerHTML +=
                      measure_data[k].value + "\xa0\xa0\xa0\xa0"; // \xa0 => ' ' 空格
                  }
                  if (
                    temp_type.indexOf("Policies and measures of Wuhan City") ===
                    -1
                  ) {
                    //没有数据隐藏
                    document.getElementsByClassName(
                      "customInfobox1"
                    )[0].style.display = "none";
                  }
                  if (
                    events_data[j]["type"] ===
                    "Policies and measures of Hubei Province"
                  ) {
                    document.getElementsByClassName(
                      "customInfobox2"
                    )[0].style.display = "block";
                    document.getElementById("hubei_events").innerHTML +=
                      "🔺" + measure_data[k].name;
                    document.getElementById("hubei_influence").innerHTML +=
                      measure_data[k].value + "\xa0\xa0\xa0\xa0";
                  }
                  if (
                    temp_type.indexOf(
                      "Policies and measures of Hubei Province"
                    ) === -1
                  ) {
                    document.getElementsByClassName(
                      "customInfobox2"
                    )[0].style.display = "none";
                  }
                  if (
                    events_data[j]["type"] === "Policies and measures of nation"
                  ) {
                    document.getElementsByClassName(
                      "customInfobox3"
                    )[0].style.display = "block";
                    document.getElementById("nation_events").innerHTML +=
                      "🔺" + measure_data[k].name; //\xa0==>空格
                    document.getElementById("nation_influence").innerHTML +=
                      measure_data[k].value + "\xa0\xa0\xa0\xa0";
                  }
                  if (
                    temp_type.indexOf("Policies and measures of nation") === -1
                  ) {
                    document.getElementsByClassName(
                      "customInfobox3"
                    )[0].style.display = "none";
                  }
                  if (
                    events_data[j]["type"] ===
                    "Policies and measures of other provinces and cities"
                  ) {
                    document.getElementsByClassName(
                      "customInfobox4"
                    )[0].style.display = "block";
                    document.getElementById("others_events").innerHTML +=
                      "🔺" + measure_data[k].name;
                    document.getElementById("others_influence").innerHTML +=
                      measure_data[k].value + "\xa0\xa0\xa0\xa0";
                  }
                  if (
                    temp_type.indexOf(
                      "Policies and measures of other provinces and cities"
                    ) === -1
                  ) {
                    document.getElementsByClassName(
                      "customInfobox4"
                    )[0].style.display = "none";
                  }
                }
              }
              temp_type.splice(0, temp_type.length);
            }
          }
        });
      }, 500);
    } else if (play_cnt === 1) {
      //播放完后play_cnt = 1
      window.location.reload(); //重新加载页面
    }
  });

  //点击暂停按钮事件
  $(".time-line").on("click", ".time-pause", function () {
    $(this).removeClass("time-pause").addClass("time-play");
    clearInterval(timer); //清除定时器
  });

  //点击某个时间点时触发事件
  $timeLi.not(":first-child").click(function () {
    $(this).addClass("active").siblings().removeClass("active");
  });
}
