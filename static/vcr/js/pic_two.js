
/*
    Globel
*/
img_url = '/kuukann/img';
img_list = '';
// Options
var layout_num = 'four';
var align_way = 'down_align';


/*
    Params
*/
var pic_id = $('#pic_id').val();
var media_url = $('#media_url').val();
var pad_screen_w = 766;
var auto_h = 'height: 100%;';
var auto_w = 'width: 100%;';

// DOM
var out_img = $('#out_img'); //图片的最外层
var center = $('#center'); // 中心

// Resize Img
function auto_col(index){
    console.info(index);
    var img_out_col = $('#img_out_col_'+ index);
    var img_in_col = $('#img_in_col_'+ index);
    var img_col = $('#img_col_'+ index);
    var the_img = $('#img_'+ index)
    console.info('ioc_h =', img_out_col.height(), 'iic_h =', img_in_col.height(), 'ic_h =', img_col.height());;
    console.info('img_h =', the_img.height(), '------------------------');
    the_img.attr({
        'style': 'bottom:0;'
    });
}
select_img(pic_id, 'neednt_cg', false);

// 展示img
function show_img (_align_flag) {
    var c_ratio = 272 / 278;
    console.info('img_list =', img_list, '================');
    out_img.empty();
    for (var i= 0; i< img_list.length; i++ ){
        var img = img_list[i].fields;
        var img_index = img.index; // 索引

        var img_html = ''+
            '<div class="ui column img_out_column center aligned" id="img_out_col_'+ img_index +'">' +
                '<div class="ui grid">' +
                    '<div class="ui column img_column" id="img_in_col_'+ img_index +'">' +
                        '<div class="centered aligned" id="img_col_'+ img_index +'">' +
                            '<div class="choise_icon" id="img_col_'+ img_index +'">' +
                                '<i class="square outline icon"></i>' +
                            '</div>' +
                            '<img class="ui fluid image centered the_img" id="img_'+ img_index +'" src="'+ media_url+ img.tiny_img +'">' +
                        '</div>' +
                    '</div>' +
                '</div>' +
            '</div>' +
            '<div class="ui fluid popup fade out the_tooltip" id="img_popup_'+ img_index +'">' +
                img.name
            '</div>';
        out_img.append(img_html);

        // Add popup
        $('#img_col_'+ img_index).popup({
            popup   : $('#img_popup_'+ img_index),
            on      : 'click',
            position: 'bottom center',
        });

        // auto_col(img_index);
    }
}

// 查询图片
function select_img (pic_id, cache_flag, is_sync) {
    $.ajax({
        url: img_url,
        type: 'get',
        data: {'pic_id': pic_id, 'cache_flag': cache_flag},
        datatype: 'json',
        cache: false,
        async: is_sync,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
        },
        success: function (callback) {
            img_list = eval(callback['img_list']);
            show_img(align_way);
        },
        error: function (callback) {
            open_tishi_modal('Server error ......')
        }
    });
}

// 操作菜单
//$('#opt_menu').dropdown();
/*

*/
/* 
    切换布局
*/
var max_layout = 'sixteen';
var mid_layout = 'eight';
var min_layout = 'four';
var bom_layout = 'two';
var plus_params = 'wide';
// DOM
var empty_span = $('#empty_span');
var layout_col = $('.img_out_column');
var img_col = $('.img_column');

// Option
if(window.w > pad_screen_w){
    img_col.addClass('img_column_pc');
}
function layout(_layout_flag) {
    layout_col.removeClass(layout_num).removeClass(plus_params);
    layout_col.addClass(_layout_flag).addClass(plus_params);
    layout_num = _layout_flag;
    if(_layout_flag == max_layout){
        img_col.attr({
            'style': 'padding: 0px 0px 10px 0px;',
        });
        empty_span.css('width', '0px');
    }
    else if(_layout_flag == mid_layout){
        if(window.w > pad_screen_w){
            img_col.attr({
                'style': 'padding: 5px 12px 10px 8px; margin: 0 15px 0 15px',
            });
            empty_span.css('width', '15px');
        }
    }
    else if(_layout_flag == min_layout){
        if(window.w > pad_screen_w){
            img_col.attr({
                'style': 'padding: 5px 12px 10px 8px; margin: 0 15px 0 15px',
            });
            empty_span.css('width', '15px');
        }
    }
    else if(_layout_flag == bom_layout){
        img_col.attr({
            'style': 'padding: 5px 7px 10px 3px; margin: 0 5px 0 5px',
        });
        empty_span.css('width', '0px');
    }
    if(out_img.height() < (window.h- 48)){
        center.height(window.h- 98);
    }
    else{
        center.height($('#pic_con').height());
    }
    $('#footer').removeClass('mr_t_1000');
}
$('#max_layout').click(function() {
    layout(max_layout);
});
$('#mid_layout').click(function() {
    layout(mid_layout);
});
$('#min_layout').click(function() {
    layout(min_layout);
});
$('#bom_layout').click(function() {
    layout(bom_layout);
});
layout(layout_num);


/* 
    增删改
*/
$('.cancle').click(function() {
    $('.modal').modal('hide');
});
function open_img_modal() {
    $('#add_img_modal')
        .modal({
            closable  : true,
            onDeny    : function(){
                console.info('cancle_add_img!!!');
            },
            onApprove : function() {
                //var form_data = new FormData();
                //form_data.append('img_name', $('#add_img_name').val());
                //form_data.append('img_image', $('#add_img_image').val());
                //form_data.append('pic_id', pic_id);
                //opt_img(img_url, $('#add_img_form').serialize(), 'POST', false);
                $('#add_img_form').submit();
            }
        })
        .modal('show');
}

$('#add_img').click(function() {
    open_img_modal();
});
function opt_img(opt_url, form_data, method, is_sync) {
    $.ajax({
        url: opt_url,
        type: method,
        data: form_data,
        datatype: 'text',
        cache: false,
        async: is_sync,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
        },
        success: function (callback) {
            if(callback == 'ok'){
                console.info('layout =', layout_num);
                select_img(pic_id, 'need_cg', false);
            }
        },
        error: function (callback) {
            open_tishi_modal('Server error ......')
        }
    });
}