// 定义图片尺寸变量
var s_less = 200
var s_mini = 436
var s_tiny = 816
var s_small = 1366
var s_middle = 2166
var s_big = 3286
var s_large = 4446
var s_huge = 5666
var s_massive = 7266

// 打开提示模态框
function open_tishi_modal(tishi_txt){
    $('#tishi_txt').empty();
    $('#tishi_txt').html(tishi_txt)
    $('#tishi_modal')
    .modal('setting', 'transition', 'fade')
    .modal('show')
}
// 打开看图框
function see_modal (flag, tim){
    // 显示看图框
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

// 看图 Viewer
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
// 打开相册剪裁模态框
var j = 0
open_cropper_modal = function(file_input_id, end_show_img_id, ratio, modal_id) {
    var start_show_id = '#cropper_start_img'
    
    var file_obj = document.getElementById(file_input_id);
    var img_src = getObjectURL(file_obj);
    $(start_show_id).attr("src", img_src);//将图片的src变为获取到的路径
    // 打开模态框
    $('#cropper_modal')
        .modal('setting', 'closable', false)
        .modal({
            closable  : false,
            onApprove : function() {
                var cas = $(start_show_id).cropper("getCroppedCanvas");//找死了
                // 在此地进行图片压缩
                var quality = img_comp(cas);
                var imgsrc = cas.toDataURL("image/jpeg", quality);//这里转成base64 image，img的src可直接使用
                $('#'+ end_show_img_id).attr("src", imgsrc);
                $(modal_id).modal('show');
            }
        })
        .modal('show');

    // Cropper
    var cropper_w = $('#cropper_modal').width()- 55;
    var cropper_h = $(window).height()- 150;
    start_cropper(start_show_id, end_show_img_id, ratio, cropper_w, cropper_h);
    if(j == 1){
        $(start_show_id).cropper('replace', img_src, false );
    }j = 1
}


// 使用 阈值 进行图片压缩
function img_comp(img_file) {
    var i_w = img_file.width
    var i_h = img_file.height
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

// 照片剪裁
start_cropper = function(start_img_id, end_img_id, ratio, cropper_w, cropper_h) {
    'use strict';
    var cropper_image = $(start_img_id);
    var box_w = ratio* 100;
    var box_h = ratio/ 100;
    cropper_image.cropper({
        aspectRatio: ratio,
        preview: end_img_id, // 指定 显示 截图的容器

        guides: false, // 显示 在裁剪框中的虚线。def: True
        center: true, // 初始时裁剪框位于图片正中心。def: True
        highlight: true, // 在裁剪框上方显示白色的区域(突出裁剪框)。def: True
        background: true, // 显示容器的网格背景。（就是后面的马赛克）。def: True
        autoCropArea: 0.8, // 定义自动裁剪面积大小(百分比)和图片进行对比。def: 0.8

        minContainerWidth: cropper_w, // 容器的最小宽度。def: 200
        minContainerHeight: cropper_h, // 容器的最小高度。def: 100
        minCropBoxWidth: box_w, // 裁剪层的最小宽度。def: 0
        minCropBoxHeight: box_h, // 裁剪层的最小高度。def: 0

        movable: true, // 是否允许 可以移动后面的图片。def: True
        rotatable: true, // 是否允许 旋转图像。def: True
        scalable: true, //是否允许 缩放图像。def: True
        zoomable: true, // 是否允许 放大图像。def: True
        zoomOnTouch: true, // 是否可以通过拖动触摸来放大图像。def: True
        zoomOnWheel: true, // 是否可以通过移动鼠标来放大图像。def: True

        cropBoxMovable: true, // 是否通过拖拽来移动剪裁框。def True
        cropBoxResizable: true, // 是否通过拖动来调整剪裁框的大小。def True
        toggleDragModeOnDblclick: false, // 当点击两次时可以在“crop”和“move”之间切换拖拽模式。def: True

        ready: null, // 插件准备完成执行的函数（只执行一次）。def: null
        cropstart: null, // 剪裁框开始移动执行的函数。def: null
        cropmove: null, // 剪裁框移动时执行的函数。def: null
        cropend: null, // 剪裁框移动结束执行的函数。def: null
        crop: null, // 剪裁框发生变化执行的函数。def: null
        zoom: null, // 剪裁框缩放的时候执行的函数。def: null
        crop: function(event) {
            
        }
    });
    // Get the Cropper.js instance after initialized
    var cropper = cropper_image.data('cropper');

    // 使用按钮 移动 图片
    $("#move_left").on("click", function () {
        cropper_image.cropper('move', -10, 0); // offset-x: 1px
    })
    $("#move_right").on("click", function () {
        cropper_image.cropper('move', 10, 0);// offset-y: -1px
    })
    $("#move_up").on("click", function () {
        cropper_image.cropper('move', 0, -10); // offset-x: 1px
    })
    $("#move_down").on("click", function () {
        cropper_image.cropper('move', 0, 10);// offset-y: -1px
    })
    // 使用按钮 旋转 图片
    $("#rotate_90").on('click', function () {
        cropper_image.cropper('rotate', 90); // 顺时针 45度
    })
    // 使用按钮 翻转 图片
    var s_x_f = 0;
    var s_y_f = 0;
    $('#scale_x').on('click', function () {
        if(s_x_f == 0){
            cropper_image.cropper('scaleX', -1); // 水平
            s_x_f = 1;
        }
        else{
            cropper_image.cropper('scaleX', 1); // 水平
            s_x_f = 0;
        }
    })
    $('#scale_y').on('click', function () {
        if(s_y_f == 0){
            cropper_image.cropper('scaleY', -1); // 水平
            s_y_f = 1;
        }
        else{
            cropper_image.cropper('scaleY', 1); // 水平
            s_y_f = 0;
        }
    })
    
    // 恢复为初始状态，剪裁框数据要重新设置
    $("#reset_cropper").on("click", function () {
        cropper_image.cropper('reset');
    })
    // 清除剪裁框
    //$("#close_cropper").on("click", function () {
    //    cropper_image.cropper('clear');
    //})
    // 退出剪裁模式
    //$("#close_cropper").on("click", function () {
        //cropper_image.cropper('destroy');
    //s})
}