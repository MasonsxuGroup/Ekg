// timeClick(); //时间轴点击事件

// function timeClick() {
//   var timer;
//   var cnt = 5,
//     index, //定义li选中状态时的索引
//     $timeUl = $(".time-line"),
//     $timeLi = $(".time-line li"),
//     lenCount = $timeLi.length - 1; //去除第一个按钮li标签的长度
//   var normal = []; //存放正常的索引
//   // var lx = []; //存储与时间匹配的时间类型（policy.type）
//   var truei = []; //存储与时间匹配的index
//   //点击播放时间轴事件
//   $timeUl.on("click", ".time-play", function () {
//     $(this).removeClass("time-play").addClass("time-pause");
//     index = Number($timeUl.find("li.active").attr("data-index")); //将字符串强制转换为数字类型
//     timer = setInterval(function () {
//       //判断当前索引的位置，如果在最后一位则从第一个时间点开始，反之则按顺序播放
//       if (lenCount == index + 1) {
//         $timeUl.find("li:eq('" + lenCount + "')").removeClass("active");
//         $timeUl.find("li:eq(1)").addClass("active");
//       } else {
//         // console.log(22)
//         $(".time-line li.active")
//           .next()
//           .addClass("active")
//           .siblings() //选择除本身以外的其他同级元素,,
//           .removeClass("active");
//       }
//       $timeLi.each(function () {
//         if ($(this).hasClass("active")) {
//           index = Number($(this).attr("data-index")); //字符串转换为数字类型，索引从0开始
//           normal.push(index);

//           //用来判断是否正常轮播
//           if (normal.length > 1) {
//             let ds1 = normal[normal.length - 1];
//             let ds2 = normal[normal.length - 2]; //这里注意，normal不是数组，不能使用arr[-1]取最后一个值
//             if (ds1 == ds2 + 1) {
//               cnt += 1;
//               // console.log("n");
//             }
//             if (ds2 == 5 && ds1 == 0) {
//               cnt += 1;
//               // console.log('nn')
//             }
//             //以上都是正常轮播

//             //接下来是非正常时逻辑
//             if (ds1 > ds2 && ds1 - ds2 != 1) {
//               console.log("1111");
//               console.log(normal);
//               cnt = cnt + ds1 - ds2;
//             }
//             if (ds1 < ds2 && ds2 - ds1 != 5) {
//               console.log("2222");
//               console.log(normal);
//               cnt = cnt + ds1 - ds2;
//             }
//             if (ds1 == ds2) {
//               cnt = cnt;
//             }
//           } else {
//             cnt += 1;
//           }
//           // console.log(normal)
//           // console.log(cnt)
//           //添加圆点底下显示的数据
//           axios.get("/date.json").then((res) => {
//             var json = res.data.startTime;
//             // console.log(json[6])
//             if (index == 0 && cnt > 10) {
//               //判断是否是第二次循环播放，并且是否播放到第一个点
//               document.getElementById("0").innerHTML = json[cnt - 5];
//               document.getElementById("1").innerHTML = json[cnt - 4];
//               document.getElementById("2").innerHTML = json[cnt - 3];
//               document.getElementById("3").innerHTML = json[cnt - 2];
//               document.getElementById("4").innerHTML = json[cnt - 1];
//               document.getElementById("5").innerHTML = json[cnt];
//             }
//             active = document.getElementsByClassName("active");
//             // console.log(active);
//             act = active[0].innerText;
//             // console.log(act);
//             document.getElementById("rr5").innerHTML = act;
//             document.getElementById("r5").innerHTML = act;
//             document.getElementById("rr1").innerHTML = act;
//             document.getElementById("r1").innerHTML = act;
//             axios.get("/policy.json").then((res) => {
//               var policy = res.data;
//               //     // console.log(policy);
//               for (i in policy) {
//                 // console.log(policy[i].startTime)
//                 // let stTime = policy[i].startTime
//                 if (act == policy[i].startTime) {
//                   // console.log(1111111);
//                   // console.log(policy[i].name);
//                   console.log(act);
//                   truei.push(i);
//                   // let leixing = policy[i].type;
//                   // lx.push(leixing);
//                   // console.log(lx);
//                   console.log(truei);
//                 }
//               }
//               while (truei.length>0) {
//                 for (j in truei) {
//                   k = Number(truei[j]);
//                   let lx = policy[k].type;
//                   if (lx == "国家政策和举措") {
//                     //特别注意，javascript不能使用if...in...语句判断元素是否在数组里
//                     console.log(1);
//                     document.getElementById("rr6").innerHTML = policy[k].name;
//                     document.getElementById("rr7").innerHTML =
//                       "影响力：" + policy[k].value;
//                   } else {
//                     // document.getElementById("rr5").innerHTML = act;
//                     document.getElementById("rr6").innerHTML = "";
//                     document.getElementById("rr7").innerHTML = "";
//                   }
//                   if (lx == "武汉市政策和举措") {
//                     console.log(2);
//                     document.getElementById("r6").innerHTML = policy[k].name;
//                     document.getElementById("r7").innerHTML =
//                       "影响力：" + policy[k].value;
//                   } else {
//                     document.getElementById("r6").innerHTML = "";
//                     document.getElementById("r7").innerHTML = "";
//                   }
//                   if (lx == "湖北省政策和举措") {
//                     console.log(3);
//                     document.getElementById("rr2").innerHTML = policy[k].name;
//                     document.getElementById("rr3").innerHTML =
//                       "影响力：" + policy[k].value;
//                   } else {
//                     // document.getElementById("rr1").innerHTML = act;
//                     document.getElementById("rr2").innerHTML = "";
//                     document.getElementById("rr3").innerHTML = "";
//                   }
//                   if (lx == "其他省市政策和举措") {
//                     console.log(4);
//                     document.getElementById("r2").innerHTML = policy[k].name;
//                     document.getElementById("r3").innerHTML =
//                       "影响力：" + policy[k].value;
//                   } else {
//                     document.getElementById("r2").innerHTML = "";
//                     document.getElementById("r3").innerHTML = "";
//                   }
//                   // 匹配一个删除一个。如act == 2020/1/1时，truei == [1,2],再遍历truei,匹配信息至每一个提示框里
//                   // 匹配完一个删除数组对应的i值
//                   console.log("truei--");
//                   truei.splice(0, 1);
//                   console.log(truei);
//                 }
//               }
//             });
//           });
//           // console.log(json)
//         }
//       });
//     }, 1000);
//   });

//   //点击暂停按钮事件
//   $(".time-line").on("click", ".time-pause", function () {
//     $(this).removeClass("time-pause").addClass("time-play");
//     clearInterval(timer); //清除定时器
//   });

//   //点击某个时间点时触发事件
//   $timeLi.not(":first-child").click(function () {
//     // var index = $(this).data("index");
//     // abnormal.push(index)
//     // console.log(abnormal.length)
//     $(this).addClass("active").siblings().removeClass("active");
//     // clearInterval(timer);//清除定时器
//   });
// }
