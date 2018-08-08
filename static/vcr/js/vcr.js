//全局变量
window.w = $(window).width();
window.h = $(window).height();
pro_screen_w = 1020;
pad_screen_w = 759;

// 栅格宽度
var one = $('#use .one').width();
var two = $('#use .two').width();
var three = $('#use .three').width();
var four = $('#use .four').width();
var five = $('#use .five').width();
var six = $('#use .six').width();
var seven = $('#use .seven').width();
var eight = $('#use .eight').width();
var nine = $('#use .nine').width();
var ten = $('#use .ten').width();
var eleven = $('#use .eleven').width();
var twelve = $('#use .twelve').width();
var thirteen = $('#use .thirteen').width();
var fourteen = $('#use .fourteen').width();
var fifteen = $('#use .fifteen').width();
var sixteen = $('#use .sixteen').width();
var wide = 'wide';
// URL
var kuukann_url = '/域/';
var kouza_url = '/メリー/';
var option_url = '/する/';
var ajax_kuukann = '/けんじゃた/';
var layout_url = ajax_kuukann + 'layout';
var search_url = 'ルマスター/';
var station_url = kouza_url + 'ゴミはこ/';
var ajax_pic_url = ajax_kuukann + 'pic';
var ajax_img_url = ajax_kuukann + 'pic/img'
var ajax_station_url = option_url + 'station';
var ajax_style_url = option_url + 'style';

// 有用参数
var select_step = 48;
var media_url = $('#media_url').val();
// 用户信息
var is_shen = false;
/*
    合并 Go.js
*/
function go_in_kuukann() {
    location.href = kuukann_url + $('#def_kuukann').val();
}
function go_in_pic(kuukann_name, pic_name) {
    location.href = kuukann_url + kuukann_name + '/' + pic_name;
}
function go_in_s(s_name, param){
    if(param != null){
        location.href = kouza_url + s_name + '/' + param;
    }
    else{
        location.href = kouza_url + s_name;
    }
}
/*
    合并 func.js
*/
function auto_img_func(father_div_id, img_id, def_h) {
    var img_div = $(father_div_id);
    var img = $(img_id);
    var img_style = '' +
        'width: 100%;' +
        'height: ' + def_h + 'px;' +
        'background: url("'+ img.attr('src') +'") repeat;' +
        'background-position: 60% 36%;' +
        'background-size: cover;';
    img_div.attr({'style': img_style, });
}
function fb_to_dataUrl(obj, cb){
    var a = new FileReader();
    a.onload = function (e){
        cb(e.target.result);
    }
    a.readAsDataURL(obj);
}
 function dataUrl_to_Image(durl){
    var img = new Image();
    img.src = durl;
    return img;
}
function blob_to_Image(blob, cb){
    fb_to_dataUrl(blob, function(dataurl){
        var img = new Image();
        img.src = dataurl;
        cb(img);
    });
}
function loadImg(form_id, showImg_id) {
    var file = $(form_id).find("input")[0].files[0];
    var reader = new FileReader();
    var imgFile;
    reader.onload=function(e) {
        imgFile = e.target.result;
        $(showImg_id).attr('src', imgFile);
    };
    reader.readAsDataURL(file);
}
function dataURLtoBlob(dataurl) {
    var arr = dataurl.split(',');
    var mime = arr[0].match(/:(.*?);/)[1];
    var bstr = atob(arr[1].replace(/\s/g, ''));
    var n = bstr.length;
    var u8arr = new Uint8Array(n);
    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new Blob([u8arr], {type: mime});
}
function $_(id) {
    return document.getElementById(id);
}
function gen_base64(file_input_id) {
    var file = $_('file_input_id').files[0];
    r = new FileReader();
    r.onload = function(){
        return r.result;
    };
    r.readAsDataURL(file);
}
function getObjectURL(node) {
    var imgURL = "";
    try {
        var file = null;
        if (node.files && node.files[0]) {
            file = node.files[0];
        } else if (node.files && node.files.item(0)) {
            file = node.files.item(0);
        }
        try {
            imgURL = file.getAsDataURL();
        } catch (e) {
            imgURL = window.URL.createObjectURL(file);
        }
    } catch (e) {
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
    合并 tool.js

var s_less = 200;
var s_mini = 436;
var s_tiny = 816;
var s_small = 1366;
 */
var s_middle = 2166;
var s_big = 3286;
var s_large = 4446;
//var s_huge = 5666;
var s_massive = 7266;

function open_tishi_modal(tishi_txt){
    $('#tishi_txt').empty();
    $('#tishi_txt').html(tishi_txt);
    $('#tishi_modal')
    .modal('setting', 'transition', 'fade')
    .modal('show')
}
function see_modal (flag, tim){
    if (flag){
        $('#see_modal').fadeIn(tim, function(){
            $('#see_modal').attr({ 'style': ''});
            $('#see_img').animate({ opacity: 1 },tim, function(){ });
        });
    }
    else{
        $('#see_img').animate({ opacity: 0 },tim, function(){ });
        $('#see_modal').fadeOut(tim, function(){
            $('#see_modal').attr({ 'style': 'display:none'});
        });
    }
}
function see_viewer() {
    var imgs = $('#see_imgs_ul');
    var options = {
        url: 'data-original',
        viewed: function (e) {
            this.viewer('zoomTo', 1.5);
        }
    };
    imgs.viewer(options);
}
var j = 0;
function open_cropper_modal(file_input_id, end_show_img_id, ratio, modal_id) {
    var start_show_id = '#cropper_start_img';

    var file_obj = document.getElementById(file_input_id);
    var img_src = getObjectURL(file_obj);
    $(start_show_id).attr("src", img_src);
    $('#cropper_modal')
        .modal('setting', 'closable', false)
        .modal({
            closable  : false,
            onApprove : function() {
                var cas = $(start_show_id).cropper("getCroppedCanvas");
                var quality = img_comp(cas);
                var imgsrc = cas.toDataURL("image/jpeg", quality);
                $('#'+ end_show_img_id).attr("src", imgsrc);
                $(modal_id).modal('show');
            }
        })
        .modal('show');
    var cropper_w = $('#cropper_modal').width()- 55;
    var cropper_h = $(window).height()- 150;
    start_cropper(start_show_id, end_show_img_id, ratio, cropper_w, cropper_h);
    if(j == 1){
        $(start_show_id).cropper('replace', img_src, false );
    }j = 1
};
function img_comp(img_file) {
    var i_w = img_file.width;
    var i_h = img_file.height;
    var quality = 1.0;
    if ((s_big> i_w) && (i_w > s_middle)) {
        quality = 0.8
    }
    else if ((s_large > i_w) && (i_w >= s_big)){
        quality = 0.6
    }
    else if ((s_massive > i_w) && (i_w >= s_large)){
        quality = 0.4
    }
    else if (i_w > s_massive){
        quality = 0.2
    }
    return quality
}
function start_cropper(start_img_id, end_img_id, ratio, cropper_w, cropper_h) {
    'use strict';
    var cropper_image = $(start_img_id);
    var box_w = ratio* 100;
    var box_h = ratio/ 100;
    cropper_image.cropper({
        aspectRatio: ratio,
        preview: end_img_id,
        guides: false,
        autoCropArea: 0.8,
        minContainerWidth: cropper_w,
        minContainerHeight: cropper_h,
        minCropBoxWidth: box_w,
        minCropBoxHeight: box_h,
        toggleDragModeOnDblclick: false,
    });
    var cropper = cropper_image.data('cropper');
    $("#move_left").on("click", function () {
        cropper_image.cropper('move', -10, 0);
    });
    $("#move_right").on("click", function () {
        cropper_image.cropper('move', 10, 0);
    });
    $("#move_up").on("click", function () {
        cropper_image.cropper('move', 0, -10);
    });
    $("#move_down").on("click", function () {
        cropper_image.cropper('move', 0, 10);
    });
    $("#rotate_90").on('click', function () {
        cropper_image.cropper('rotate', 90);
    });
    var s_x_f = 0;
    var s_y_f = 0;
    $('#scale_x').on('click', function () {
        if(s_x_f == 0){
            cropper_image.cropper('scaleX', -1);
            s_x_f = 1;
        }
        else{
            cropper_image.cropper('scaleX', 1);
            s_x_f = 0;
        }
    });
    $('#scale_y').on('click', function () {
        if(s_y_f == 0){
            cropper_image.cropper('scaleY', -1);
            s_y_f = 1;
        }
        else{
            cropper_image.cropper('scaleY', 1);
            s_y_f = 0;
        }
    });
    $("#reset_cropper").on("click", function () {
        cropper_image.cropper('reset');
    })
}