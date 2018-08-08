// 菜单
$('#station_acc').accordion();
$('#bt_btn').dropdown();
if(window.w < pro_screen_w){
    $('#bt_btn').removeClass('basic');
}

// 还原相册
var sb_flag = true;
function station_back(index, station_flag, img_count){
    var station_item = $('#station_item_'+ index);
    var station_pic_num = $('#station_pic_num');
    var station_img_num = $('#station_img_num');
    if(sb_flag){
        sb_flag = false;
        $.ajax({
            url: station_url + station_flag,
            type: 'PUT',
            data: {'station_id': index},
            cache: false,
            async: true,
            beforeSend:function(xhr, settings){
                xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
            },
            success: function (callback) {
                if (callback == 'pic') {
                    station_item.attr({'style': 'display:none;'});
                    var pic_num = station_pic_num.html();
                    pic_num -= 1;
                    station_pic_num.html(pic_num);
                    var img_num = station_img_num.html();
                    img_num -= img_count;
                    station_img_num.html(img_num);
                }
                sb_flag = true
            },
            error: function (callback) {
                open_tishi_modal('Server error ......');
                sb_flag = true
            }
        });
    }
}

// URL 跳转
function go_station_in(param){
    location.href = station_url + param;
}

// 查询图片
var media_url = $('#media_url').val();
var imgs_grid = $('#imgs_grid');
var select_flag = true;
var start_num = 0;
var bt_btn_top = $('#bt_btn').offset().top;
function select_img(){
    if(select_flag){
        select_flag = false;
        $.get(ajax_station_url, {'station_flag': 'img', 'start_num': start_num, 'end_num': start_num+ select_step}, function (ret) {
            var has_data = eval(ret['has_data']);
            if ((has_data == 'True') | (has_data == true)){
                var data_list = eval(ret['data_list']);
                var date_list = eval(ret['date_list']);
                show_img(data_list, date_list);
                start_num += select_step;
                select_flag = true;
                if (date_list.length < select_step){
                    select_flag = false;
                }
            }
            else{
                select_flag = false;
                msg = '没有更多内容了';
                var msg_html = 
                '<div style="height: 15px;"></div>' +
                '<div class="ui horizontal divider">'+ msg +'</div>' +
                '<div style="height: 15px;"></div>';
                $('#msg_div').html(msg_html);
            }
        });
    }
}
function show_img(data_list, date_list) {
    for (var i= 0; i< date_list.length; i ++){
        var img = data_list[i];
        var date = date_list[i];
        var img_id = data_list[i].id;
        var tiny_img = data_list[i].tiny_img;
        
        var p = get_date(date['date_flag'], date['date_value']);
        //p = date['date_value']
        // p = '<i class="circular icon the_day_i">'+ p +'</i>';
        var img_html = 
        '<div class="ui four wide column" id="col_div_'+ img_id +'" style="padding: 10px 10px;">' +
        '    <div class="cover" id="cover_'+ img_id +'">' +
        '        <div class="img_div" id="img_div_'+ img_id +'">' +   
        '        </div>' +
        '        <div class="the_day_l" id="day_l_'+ img_id +'"></div>' +
        '    </div>' +
        '</div>';
        var img_style = 
        'background-image: url("'+ media_url + tiny_img +'");' +
        'background-position: center center;' +
        'background-size: cover;' +
        'width: 100%;' +
        'height: 100%;';

        imgs_grid.append(img_html);

        var img_div = $('#img_div_'+ img_id);
        img_div.attr({'style': img_style});

        var col_div = $('#col_div_'+ img_id);
        col_div.height(col_div.width());
        choise(img_id);
        all_data_list.push(img_id);
    }
    var last_id = all_data_list[all_data_list.length - 1];
    var last_col_div = $('#col_div_'+ last_id);
    last_col_div.visibility({
        onTopVisible: function(calculations) {
            if (select_flag){
                select_img();
            }
        },
    });
}
function get_date(date_flag, date_value){
    date_html = ' days';
    if (date_flag == 'hour'){
        date_html = ' hours';
    }
    else if (date_flag == 'minute'){
        date_html = ' minus';
    }
    return date_value + date_html;
}
function change_col_div(index){
}
if(web_ctrl.page_flag == 'img'){
    select_img();
}
/*
    搜索
*/
$('#search_icon').on('click', function () {
    go_search('s_s_input');
});
function go_search (search_input){
    var search_value = $('#'+ search_input).val();
    flag = web_ctrl.page_flag;
    if(web_ctrl.page_flag == 'search'){
        flag = $('#search_flag').val();
    }
    var url = option_url + search_url + search_value + '/' + flag;
    location.href = url;
}
/*
    更改界面
*/
var s_pic_num = $('#station_pic_num');
var s_img_num = $('#station_img_num');
var search_icon = $('#search_icon');
if (web_ctrl.page_flag == 'pic'){
    s_pic_num.addClass(kouza_ctrl.color_val);
    s_pic_num.addClass('left');
    s_pic_num.addClass('pointing');
    $('#menu_pic_a').addClass('active');
}
else if (web_ctrl.page_flag == 'img'){
    s_img_num.addClass(kouza_ctrl.color_val);
    s_img_num.addClass('left');
    s_img_num.addClass('pointing');
    $('#menu_img_a').addClass('active');
}
else if (web_ctrl.page_flag == 'search'){
    search_icon.addClass(kouza_ctrl.color_val);
    //$('#menu_search_a').addClass('active');
}

/*
    选择
*/
// 改变选中
function change_bar(flag) {
    if(flag){
        $('#choise_bar').attr({'style': 'visibility: visible'});
    }else {
        $('#choise_bar').attr({'style': 'visibility: hidden'});
    }
}
// 反选
function fan_choise() {
    var new_all_list = $.extend(true, [], all_data_list); // 深拷贝
        for (var i= 0; i< data_list.length; i++ ){
        var j = $.inArray(data_list[i], new_all_list);
        if (j != -1 ){
         new_all_list.splice(j, 1);
        }
    }
    for(var i= 0; i< data_list.length; i++ ){
        change_choise_bar(data_list[i], false);
    }
    data_list = new_all_list;
    for(var i= 0; i< data_list.length; i++ ){
        change_choise_bar(data_list[i], true);
    }
}
// 取消选中
function none_choise() {
    for(var i= 0; i< data_list.length; i++ ){
         change_choise_bar(data_list[i], false);
    }
    data_list = [];
}
$('.fan_choise').click(function () {
    fan_choise();
});
/*
    调整
 */
function change_grid(value) {
    if(window.w < pad_screen_w){
        for(var i= 0; i< all_data_list.length; i ++){

            var col_div = $('#col_div_' + all_data_list[i]);
            col_div.removeClass('four');
            col_div.removeClass('wide');
            col_div.addClass(value);
            col_div.addClass('wide');
            console.info(i)
        }
    }
}