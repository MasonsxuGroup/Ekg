//获取id
function my$(id) {
    return document.getElementById(id);
}

$(document).ready(function () {
    my$('things').onclick=function() {
        // alert('ok')
        
        // document.getElementById('box-bottom').innerHTML=''
        // console.log(my$('box-bottom'))
        axios.get('/userdata.json').then((res) => {
            var json = res.data;
            var r1 = '';    //startTime
            var r2 = '';    //name
            var r3 = '';    //value
            var r4 = '';    //用作处理数据
            // console.log(json)
            for (var i = 0; i < json.length; i++) {
                // console.log(json[i].value)
                r4 = json[0].startTime;

                if (r4.substring(6, 7) != '/') {
                    r1 = r4.substring(0, 10)
                }
                else {
                    r1 = r4.substring(0, 9);     //substring--javascript的字符串切片方式
                    // console.log('ok')
                };

                r2 = json[0].name;

                r3 = '影响力：' + json[0].value;

                //数据就位，
            }
            // console.log(r1)
            var r11 = document.getElementById('r1')
            r11.innerHTML = r1
            var r22 = document.getElementById('r2')
            r22.innerHTML = r2
            var r33 = document.getElementById('r3')
            r33.innerHTML = r3
        })
        contentHtmls = '<span id="r1"></span><br><span id="r2"></span><br><span id="r3"></span><br>'
        document.getElementById('box-bottom').innerHTML=contentHtmls
        console.log(my$('box-bottom'))
    }

    my$('treasures').onclick = function(){
        htmls = 'hxzlq'
        document.getElementById('box-bottom').innerHTML=htmls
    }
    
});
