/*
    图片自适应
*/
auto_img_func = function (father_div_id, img_id, def_h) {
    var img_div = $(father_div_id);
    var img = $(img_id);
    var img_style = '' +
        'width: 100%;' +
        'height: ' + def_h + 'px;' +
        'background: url("'+ img.attr('src') +'") repeat;' +
        'background-position: 60% 36%;' +
        'background-size: cover;';
    img_div.attr({'style': img_style, });
    console.info(img.attr('src'));
}

// File/Blob 转换为DataURL
fb_to_dataUrl = function(obj, cb){
    console.info(obj);
    var a = new FileReader();
    a.onload = function (e){
        console.info(e.target.result);
        cb(e.target.result);
    }
    console.info(a);
    a.readAsDataURL(obj);
}

// DataUrl 转 Image
dataUrl_to_Image = function (durl){
    var img = new Image();
    img.src = durl;
    return img;
}

// Blob 转 Image
blob_to_Image = function(blob, cb){
    fb_to_dataUrl(blob, function(dataurl){
        var img = new Image();
        img.src = dataurl;
        cb(img);
    });
}

// 读取图片: 从文本框中读取图片，显示在img中
loadImg = function(form_id, showImg_id) {
    //获取文件
    var file = $(form_id).find("input")[0].files[0];
    //创建读取文件的对象
    var reader = new FileReader();
    //创建文件读取相关的变量
    var imgFile;
    //为文件读取成功设置事件
    reader.onload=function(e) {
        imgFile = e.target.result;
        $(showImg_id).attr('src', imgFile);
    };
    //正式读取文件
    reader.readAsDataURL(file);
}

/* 工具方法：dataURL(base64字符串)转换为Blob对象（二进制大对象） */
//data:image/png;base64,iVBORw0KGgoAAAANSUhEUg......
function dataURLtoBlob(dataurl) {
    var arr = dataurl.split(',');
    var mime = arr[0].match(/:(.*?);/)[1];// 结果：   image/png
    // console.log("arr[0]====" + JSON.stringify(arr[0]));//   "data:image/png;base64"
    // console.log("arr[0].match(/:(.*?);/)====" + arr[0].match(/:(.*?);/));// :image/png;,image/png
    // console.log("arr[0].match(/:(.*?);/)[1]====" + arr[0].match(/:(.*?);/)[1]);//   image/png
    var bstr = atob(arr[1].replace(/\s/g, ''));
    var n = bstr.length;
    var u8arr = new Uint8Array(n);
    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new Blob([u8arr], {type: mime});//值，类型
}


// 文件转 base64 编码
function $_(id) {
    return document.getElementById(id);
}
function gen_base64(file_input_id) {
    var file = $_('file_input_id').files[0];
    r = new FileReader();
    r.onload = function(){
        return r.result;
    }
    r.readAsDataURL(file);
}

// 获取文件上传框的文件绝对路径
getObjectURL = function(node) {
    var imgURL = "";
    try {
        var file = null;
        if (node.files && node.files[0]) {
            file = node.files[0];
        } else if (node.files && node.files.item(0)) {
            file = node.files.item(0);
        }
        //Firefox 因安全性问题已无法直接通过input[file].value 获取完整的文件路径
        try {
            //Firefox7.0
            imgURL = file.getAsDataURL();
            //alert("//Firefox7.0"+imgRUL);
        } catch (e) {
            //Firefox8.0以上
            imgURL = window.URL.createObjectURL(file);
            //alert("//Firefox8.0以上"+imgRUL);
        }
    } catch (e) {      //这里不知道怎么处理了，如果是遨游的话会报这个异常
        //支持html5的浏览器,比如高版本的firefox、chrome、ie10
        if (node.files && node.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                imgURL = e.target.result;
            };
            reader.readAsDataURL(node.files[0]);
        }
    }
    return imgURL;
}

/*
    压缩图片
*/
