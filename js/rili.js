  /**
   * js 生成日历
   */
  var date = new Date(); //创建日期对象
  var nowYear = date.getFullYear(); //获得当前年份
  var nowMonth = date.getMonth() + 1; //获得当前月份
  var nowDay = date.getDate(); //当天   //getDay是一周的第几天，getDate才是日
  // console.log(nowDay)
  var splitString = "-"; //分隔符
  var weekDays = new Array("日", "一", "二", "三", "四", "五", "六"); //星期数组
  var months = new Array(
    "一月",
    "二月",
    "三月",
    "四月",
    "五月",
    "六月",
    "七月",
    "八月",
    "九月",
    "十月",
    "十一月",
    "十二月"
  ); //月份数组
  var lastDays = new Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31); //每个月最后一天是几号

  //  变量保存，存储当前选择的年月
  var checkYear = nowYear;
  var checkMonth = nowMonth;

  //    将选择的日期添加到输入框
  function setInput(selectDay) {
    document.getElementById("txt_calendar").value =
      checkYear + splitString + checkMonth + splitString + selectDay;
  }
    
  //显示控件
  function showDate() {
    createDate(nowYear, nowMonth); //创建日历
    //显示控制位置
    var x = document.getElementById("txt_calendar").offsetLeft;
    var y = document.getElementById("txt_calendar").offsetTop + 22;
    document.getElementById("dateOuter").style.left = x + "px";
    document.getElementById("dateOuter").style.top = y + "px";
    document.getElementById("dateOuter").style.display = "";
  }

  /**
   * 拼接日历框,并且定位日历框
   */
  //    最外层样式
  var outetStyle =
    "display: none;position: absolute;width: 314px;margin-top:10px;border: 1px solid #F7F7F7;border-radius: 5px;background-color: #F7F7F7;color: #4eccc4;padding-bottom: 20px;";
  //    日历外层
  document.write('<div style="' + outetStyle + '" id="dateOuter"></div>');
  //    创建日历样式
  function createDate(thisYear, thisMonth) {
    var createDoc = '<div style="height: 30px;">';
    //当前年月日，点击此处日历自动跳到当前日期
    createDoc +=
      '<p style="width: 100%;height: 30px;text-align: center;color: #999;" onclick="getThisDay()">当前日期 ' +
      nowYear +
      "年" +
      nowMonth +
      "月" +
      nowDay +
      "号";
    //关闭日历显示
    createDoc +=
      '<span id="closeDate" onClick="hidDate()" style="float: right;font-size: 25px;margin: -7px 3px 0 0;cursor: pointer;">×</span></p></div>';
    createDoc += '<div style="margin-bottom: 8px;">';

    //上个月
    createDoc +=
      '<span id="lastMonth" onclick="lastMonthClick()" style="margin: 0 20px 0 25px;cursor:pointer;"><</span>';
    //创建年份下拉框[1900-2099]年
    createDoc +=
      '<select id ="selectYear" class="selectStyle" onchange="changeYearAndMonth()">';
    for (var i = 1900; i <= 2099; i++) {
      createDoc += "<option value=" + i + ">" + i + "</option>";
    }
    createDoc += "</select>年";
    //创建月份下拉框
    createDoc +=
      '<select id ="selectMonth" class="selectStyle" onchange="changeYearAndMonth()">';
    for (var i = 1; i <= 12; i++) {
      createDoc += "<option value=" + i + ">" + i + "</option>";
    }
    createDoc += "</select>月";
    //下一月
    createDoc +=
      '<span id="nextMonth" onClick="nextMonthClick()" style="float: right;margin-right: 25px;cursor:pointer;">></span></div>';
    //创建星期
    createDoc += '<div class="everyWeekDay">';
    for (var i = 0; i < weekDays.length; i++) {
      if (weekDays[i] == "日" || weekDays[i] == "六") {
        createDoc +=
          '<span class="weekday" style="color:red;">' + weekDays[i] + "</span>";
      } else {
        createDoc += '<span class="weekday">' + weekDays[i] + "</span>";
      }
    }
    createDoc += "</div>";
    // 创建每天天数
    createDoc += '<div class="everyDay"><div class="marginTop">'; //日期样式DIV
    var thisWeek = getThisWeekDay(thisYear, thisMonth, 1); //算出当前年月1号是星期几
    /*
     * 如果当前不是星期天,创建空白日期占位
     * 若是星期天，则循环输出当月天数
     * 待修改优化，后期改为变色的前一个月日期
     */
    if (thisWeek != 0) {
      for (var i = 0; i < thisWeek; i++) {
        createDoc += '<span class="days"></span>';
      }
    }

    //循环输出当月天数
    //getThisMonthDay()获取当月天数
    for (var i = 1; i < getThisMonthDay(thisYear, thisMonth) + 1; i++) {
      if (thisYear == nowYear && thisMonth == nowMonth && i == nowDay) {
        if (
          getThisWeekDay(thisYear, thisMonth, i) == 6 ||
          getThisWeekDay(thisYear, thisMonth, i) == 0
        ) {
          //今天是周末
          createDoc +=
            '<span onclick="setInput(' +
            i +
            ')" class="days" style="background-color:#4eccc4;color:#FFFFFF;cursor:pointer;">' +
            i +
            "</span>";
        } else {
          createDoc +=
            '<span onClick="setInput(' +
            i +
            ')" class="days" style="background-color:#4eccc4;color:#FFFFFF;cursor:pointer;">' +
            i +
            "</span>";
        }
      } else {
        //周末变为红色
        if (
          getThisWeekDay(thisYear, thisMonth, i) == 6 ||
          getThisWeekDay(thisYear, thisMonth, i) == 0
        ) {
          createDoc +=
            '<span id="weekends" onClick="setInput(' +
            i +
            ')" class="days" onmouseover="mouseOver(this);" onmouseout="mouseOut(this)" style="color:red;cursor:pointer;">' +
            i +
            "</span>";
        } else {
          createDoc +=
            '<span onClick="setInput(' +
            i +
            ')" class="days" onmouseover="mouseOver(this);" onmouseout="mouseOut(this)" style="cursor:pointer;">' +
            i +
            "</span>";
        }
      }
      //星期六换行
      if (getThisWeekDay(thisYear, thisMonth, i) == 6) {
        createDoc += "</tr>";
      }
    }
    createDoc += "</div></div>";
    //将创建好的控件字符串添加到div中
    document.getElementById("dateOuter").innerHTML = createDoc;
    //默认选择当前年份
    document.getElementById("selectYear").value = thisYear;
    //默认选择当前月
    document.getElementById("selectMonth").value = thisMonth;
  }

  //跳转到当前日
  function getThisDay() {
    checkYear = nowYear;
    checkMonth = nowMonth;
    createDate(checkYear, checkMonth);
  }

  //上一个月
  function lastMonthClick() {
    //若当前是1月份，年份减一，月份变为12
    if (checkMonth == 1) {
      checkYear = checkYear - 1;
      checkMonth = 12;
    } else {
      checkMonth = checkMonth - 1;
    }
    //创建当前月份日期
    createDate(checkYear, checkMonth);
  }

  //下一月
  function nextMonthClick() {
    //若当前是12月份，年份加1，月份变为1
    if (checkMonth == 12) {
      checkYear = checkYear + 1;
      checkMonth = 1;
    } else {
      checkMonth = checkMonth + 1;
    }
    //创建当前月份日期
    createDate(checkYear, checkMonth);
  }

  //年月下拉框
  function changeYearAndMonth() {
    checkYear = document.getElementById("selectYear").value;
    checkMonth = document.getElementById("selectMonth").value;
    createDate(checkYear, checkMonth);
  }

  //判断是否为闰年
  function isLeapYear(year) {
    var isLeap = false;
    if (0 == year % 4 && (year % 100 != 0 || year % 400 == 0)) {
      //闰年可以被4整除且不能被100整除，或者能整除400
      isLeap = true;
    }
    return isLeap;
  }

  //获取某月份的总天数
  function getThisMonthDay(year, month) {
    var thisDayCount = lastDays[month - 1]; //获取当前月份的天数
    if (month == 2 && isLeapYear(year)) {
      //若当前月份为2月，并且是闰年，天数加1
      thisDayCount++;
    }
    return thisDayCount;
  }

  //计算某天是星期几
  function getThisWeekDay(year, month, date) {
    //将年月日创建Date对象，返回当前星期几
    var thisDate = new Date(year, month - 1, date);
    return thisDate.getDay();
  }

  //鼠标移进时
  function mouseOver(obj) {
    if (obj.id == "weekends") {
      //若为周末，边框样式为红色
      obj.style.border = "1px solid red";
    } else {
      obj.style.border = "1px solid #4eccc4";
    }
  }
  //鼠标移出时，边框恢复原色
  function mouseOut(obj) {
    obj.style.border = "1px solid #F7F7F7";
  }

  //关闭日期选择框
  function hidDate() {
    document.getElementById("dateOuter").style.display = "none";
  }

  //控制键盘操作，左右控制月份，空格返回当前日期
  document.onkeydown = function (e) {
    /*
     * 浏览器兼容性
     * ie的document对象有一个all属性，它的里面存放了页面的所有标签，而其它浏览器是没有的，所以在ie中，事件对象的传播会绑定在全局的windows上，所以ie浏览器肯定是都支持window.event
     * firefox只支持事件对象作为参数传入，而这又恰恰是ie6/ie7/ie8所无法实现的，所以可以成功的区分这两类
     * ie9/chrome/opera/safari，则两种方式都支持
     * var e = event?event||window.event可以保证各浏览器的兼容的
     */
    var thisEvent = e || window.event;
    var keyCode = thisEvent.keyCode || thisEvent.which;
    //若控件是隐藏状态
    if (document.getElementById("dateOuter").style.display == "none") {
      return false;
    }
    switch (keyCode) {
      case 32: //空格，返回当前日期
        getThisDay();
        break;
      case 27: //Esc，关闭日历插件
        hidDate();
        break;
      case 37: //left，向左
        lastMonthClick();
        break;
      case 39: //right，向右
        nextMonthClick();
        break;
    }
  };
  /*模拟windows7日历 鼠标滑轮滚动翻页*/
  var direct;
  var scrollFunc = function (e) {
    //浏览器兼容
    var thisEvent = e || window.event;
    //IE,Opera,Chrome,safari
    if (thisEvent.wheelDelta) {
      direct = thisEvent.wheelDelta;
    } else if (thisEvent.detail) {
      //Firefox
      direct = thisEvent.detail;
    }
    //如果控件是隐藏状态
    if (document.getElementById("dateOuter").style.display == "none") {
      return false;
    }
    /*
     * Firefox 接收 +3 和 -3
     * 其他浏览器接收 +120 和-120
     * 其中+数表示鼠标向上滑动，-数表示向下滑动
     */
    //向上滑动，调用上一个月
    if (direct == "120" || direct == "3") {
      lastMonthClick();
      //向下滑动，调用下一个月
    } else if (direct == "-120" || direct == "-3") {
      nextMonthClick();
    }
  };

  //注册监听事件
  if (document.addEventListener) {
    if (myBrowser() == "FF") {
      //Firefox,DOMMouseScroll滚动事件只有Firefox适用
      document.addEventListener("DOMMouseScroll", scrollFunc, false);
    } else {
      //Chrome,360,safari,Opera适用mousewheel滚动事件
      document.addEventListener("mousewheel", scrollFunc, false);
    }
  } else {
    //兼容IE，测试IE8可以兼容
    document.onmousewheel = scrollFunc;
  }

  //判断浏览器类型
  function myBrowser() {
    var userAgent = navigator.userAgent; //取得浏览器的userAgent字符串
    var isOpera = userAgent.indexOf("Opera") > -1;
    if (isOpera) {
      return "Opera";
    } //判断是否Opera浏览器
    if (userAgent.indexOf("Firefox") > -1) {
      return "FF";
    } //判断是否Firefox浏览器
    if (userAgent.indexOf("Chrome") > -1) {
      return "Chrome";
    }
    if (userAgent.indexOf("Safari") > -1) {
      return "Safari";
    } //判断是否Safari浏览器
    if (
      userAgent.indexOf("compatible") > -1 &&
      userAgent.indexOf("MSIE") > -1 &&
      !isOpera
    ) {
      return "IE";
    } //判断是否IE浏览器
    if (userAgent.indexOf("Trident") > -1) {
      return "Edge";
    } //判断是否Edge浏览器
  }
