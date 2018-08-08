see_json = {};
var out_img = $('#img_grid');
var center = $('#center');
var bz = 10 / 29;
var less      =    9 / 21;
var mini      =    9 / 16;
var tiny      =    2 / 3;
var small     =    3 / 4;
var middle    =    1 / 1;
var big       =    4 / 3;
var large     =    3 / 2;
var huge      =    16 / 9;
var massive   =    21 / 9;
var pic_id = $('#pic_id').val();
var media_url = $('#media_url').val();
var pad_screen_w = 766;
var def_grid = $('#grid_name').val();
var layout_diy_w = $('#layout_diy_w').val();
var layout_diy_h = $('#layout_diy_h').val();
var order_by = $('#order_by').val();
function change_col_grid(grid_name) {
$('.col_out').removeClass('wide');
$('.col_out').removeClass(def_grid);
def_grid = grid_name;
$('.col_out').addClass(def_grid);
$('.col_out').addClass('wide');
}
function get_grid_wide(grid_name) {
if (grid_name == 'four') { return four; }
else if (grid_name == 'sixteen'){ return sixteen; }
else if (grid_name == 'eight'){ return eight; }
else if (grid_name == 'two'){ return two; }
else if (grid_name == 'twelve'){ return twelve; }
else if (grid_name == 'six'){ return six; }
else if (grid_name == 'ten'){ return ten; }
}
$('#opt_img_menu').dropdown();
$('#align_menu').dropdown();
$('#layout_grid_menu').dropdown();
var ac_flag = true;
$('.all_choise').click(function() {
if(ac_flag == true){
all_choise(); ac_flag = false; }
setTimeout(function() { ac_flag = true; }, 618);
});
var fc_flag = true;
$('.fan_choise').click(function() {
if(fc_flag == true){
fan_choise(); fc_flag = false; }
setTimeout(function() { fc_flag = true; }, 618);
});
var nc_flag = true;
$('.none_choise').click(function() {
if(nc_flag == true){
none_choise(); nc_flag = false;
}
setTimeout(function() { nc_flag = true; }, 618);
});
$('.hide_bar').click(function() {
change_tool_bar(false);
});
function auto_height(index, img_w, img_h){
var col_out = $('#col_out_'+ index);
col_out.height(col_out.width()/ (img_w/img_h));
}
function go_layout() {
$('#layout_form').attr({'action': layout_url});
$('#layout_form').submit();
}
$('.new').click(function() {
$("#order_by").val('-create_date');
go_layout();
});
$('.old').click(function() {
$("#order_by").val('create_date');
go_layout();
});
$('.max_layout').click(function() {
$("#layout_name").val('max');
go_layout();
});
$('.block_layout').click(function() {
$("#layout_name").val('grid');
$('#grid_name').val('eight');
go_layout();
});
function change_grid_ratio(d_w , d_h) {
$("#layout_name").val('grid');
$('#grid_name').val(def_grid);
$("#layout_diy_w").val(d_w);
$("#layout_diy_h").val(d_h);
go_layout();
}
function show_grid_wide() {
var grid_class = get_grid_class();
$('.'+ grid_class+ ' .icon').removeClass('inverted');
$('.'+ grid_class+ ' .icon').addClass(kouza_ctrl.color_val);
}
function get_grid_class() {
var item_class = null;
if(def_grid == 'four'){
item_class = 'grid_four';
}
else if(def_grid == 'eight'){
item_class = 'grid_eight';
}
else if(def_grid == 'sixteen'){
item_class = 'grid_sixteen';
}
return item_class;
}
function show_grid_ratio(){
var grid_class = get_ratio_class(layout_diy_w/ layout_diy_h);
if(grid_class != null){
$('.'+ grid_class+ ' .icon').removeClass('inverted');
$('.'+ grid_class+ ' .icon').addClass(kouza_ctrl.color_val);
}
else{
$('.diy_grid').html('<i class="ui check '+ kouza_ctrl.color_val +' icon"></i>'+ layout_diy_w+ '&nbsp;/&nbsp;'+ layout_diy_h);
}
}
function get_ratio_class(col_ratio) {
var item_class = null;
if(col_ratio == mini){ return 'grid_9_16'}
else if(col_ratio == tiny){ return 'grid_2_3'}
else if(col_ratio == small){ return 'grid_3_4'}
else if(col_ratio == middle){ return 'grid_1_1'}
else if(col_ratio == big){ return 'grid_4_3'}
else if(col_ratio == large){ return 'grid_3_2'}
else if(col_ratio == huge){ return 'grid_16_9'}
else if(col_ratio == middle){ return 'grid_21_9'}
return item_class;
}
$('#diy_grid').click(function() {
$('#diy_grid_modal').modal('show');
});
$('#ok_diy_grid').click(function() {
$("#layout_name").val('grid');
var d_w = $('#new_diy_w').val();
var d_h = $('#new_diy_h').val();
$("#layout_diy_w").val(d_w);
$("#layout_diy_h").val(d_h);
go_layout();
});
function change_grid_name(grid_name){
$("#grid_name").val(grid_name);
go_layout();
}
function choise(index){
var cover = $('#cover_'+ index);
var i = $.inArray(index, data_list);
if (i == -1){
data_list.push(index);
change_choise_border(cover, true);}
else{
data_list.splice(i, 1);
change_choise_border(cover, false);}
ctrl_bar();
}
function all_choise() {
data_list = $.extend(true, [], all_data_list);
for(var i= 0; i< data_list.length; i++ ){
var cover = $('#cover_'+ data_list[i]);
change_choise_border(cover, true);
}
ctrl_bar();
}
function fan_choise() {
var new_all_list = $.extend(true, [], all_data_list);
for (var i= 0; i< data_list.length; i++ ){
var j = $.inArray(data_list[i], new_all_list);
if (j != -1 ){
new_all_list.splice(j, 1); }
}
for(var i= 0; i< data_list.length; i++ ){
var cover = $('#cover_'+ data_list[i]);
change_choise_border(cover, false);
}
data_list = new_all_list;
for(var i= 0; i< data_list.length; i++ ){
var cover = $('#cover_'+ data_list[i]);
change_choise_border(cover, true);
}
ctrl_bar();
}
function none_choise() {
for(var i= 0; i< data_list.length; i++ ){
var cover = $('#cover_'+ data_list[i]);
change_choise_border(cover, false);
}
data_list = [];
ctrl_bar();
change_viewer(true);
}
function change_choise_border(choise_dom, flag){
if (flag){
choise_dom.addClass('choise_border');}
else{
choise_dom.removeClass('choise_border');}
}
function ctrl_bar() {
var data_length = data_list.length;
if(data_length >= 1){
change_txt(data_length);
change_other($('#align_menu'), true);
change_other($('#layout_grid_menu'), true);
}
else{
change_txt(data_length);
change_other($('#align_menu'), false);
change_other($('#layout_grid_menu'), false);
}
}
function change_tool_bar(flag){
if (flag){
change_dom($('#choise_bar'), flag, 200);
}
else{
change_dom($('#choise_bar'), flag, 400);
}
}
function change_dom(div_dom, flag, tim){
if(tim == 0){
if (flag){
div_dom.attr({'style': ''});
div_dom.stop(true).animate({ opacity: 1 }, tim, function(){
});
}
else{
div_dom.attr({'style': 'display:none'});
div_dom.stop(true).animate({ opacity: 0 }, tim, function(){
});
}
}
else if(tim > 0){
if (flag){
div_dom.attr({'style': ''});
div_dom.stop(true).animate({ opacity: 1 }, tim, function(){
});
}
else{
div_dom.stop(true).animate({ opacity: 0 }, tim, function(){
div_dom.attr({'style': 'display:none'});
});
}
}
}
function change_txt(dl_length){
var change_txt = $('#change_txt');
if(dl_length <= 0){
change_txt.html('未选择任何项目');
}
else{
change_txt.html('已选择&nbsp;'+ dl_length +'&nbsp;个项目');
}
}
function change_other(other_dom, flag){
if(flag){
other_dom.addClass('disabled');
}
else{
other_dom.removeClass('disabled');
}
}
$('#start_choise').click(function () {
    change_viewer(false);
});
$('.cancle').click(function() {
$('.modal').modal('hide');
});
var start_num = 0;
var select_step = 20;
var img_grid = $('#img_grid');
var diy_w = $('#layout_diy_w').val();
var diy_h = $('#layout_diy_h').val();
var conf_url = media_url;
var aiiu_bool = true;
function select_img(s_b, is_reset) {
if(is_reset){
$('#img_grid').empty();
start_num = 0;
}
if(s_b != null){
select_bool = s_b;
}
if(select_bool == true){
select_bool = false;
data = {
'pic_id': pic_id,
'select_flag': 'all',
'start_num': start_num,
'end_num': start_num + select_step
};
$.get(ajax_img_url, data, function(ret) {
var date_list = ret['img_list'];
for(var i= 0; i< date_list.length; i++ ){
show_img(date_list[i]);
}
if (date_list.length < select_step){
select_flag = false;
}
else{
select_bool = true;
aiiu_bool = true;
viewer_bool = true;
}
start_num += select_step;
rail();
});
}
}
function show_img(img){
var index = img.id;
var tiny_img = img.tiny_img;
var less_img = img.less_img;
var full_img = img.full_img;
var has_full = img.has_full;
var w = img.w;
var h = img.h;
var create_date = img.create_date;
var now_img = conf_url + less_img;
var img_html =
'<div class="ui '+ def_grid +' wide column col_out" id="col_out_'+ index +'"' +
'    style="padding: 10px 10px 10px 10px;">' +
'    <div class="cover" id="cover_'+ index +'">' +
'        <div class="img_div" id="img_div_'+ index +'"' +
'            style="">' +
'        </div>' +
'    </div>' +
'</div>';
var img_style =
'background-image: url("'+ now_img +'");' +
'background-position: center center;' +
'background-size: cover;' +
'width: 100%;' +
'height: 100%;';
img_grid.append(img_html);
all_data_list.push(index);
auto_height(index, diy_w, diy_h);
$('#img_div_' + index).attr({'style': img_style});
bind_see(index);
see_json[index] = {
'tiny_img': tiny_img,
'full_img': full_img,
'width': w,
'height': h,
'create_date': create_date
};
}
function rail(){
var last_index = all_data_list[all_data_list.length - 1];
var last_col_div = $('#col_out_' + last_index);
last_col_div.visibility({
onTopVisible: function(calculations) {
if (select_bool){
select_img();
}
},
});
}
var viewer_bool = true;
var is_viewer = true;
function bind_see(index) {
var cover_ = $('#col_out_' + index);
cover_.click(function (){
    if(is_viewer){
        $('.modal').modal('hidden');
        add_img_in_ul();
        if(viewer_bool){
        $('#see_imgs_ul').viewer('update');
        viewer_bool = false;
        }
        $('#see_img_' + index).click();
    }
    else {
        choise(index);
    }
})
}
function change_viewer(flag) {
    if(flag){
        change_tool_bar(false);
        data_list = [];
        ctrl_bar();
    }
    else {
        change_tool_bar(true);
        change_txt(data_list.length);
    }
    is_viewer = flag;
}
function add_img_in_ul(){
if(aiiu_bool){
aiiu_bool = false;
for(key in see_json){
var img = see_json[key];
var image = media_url + img.tiny_img;
var create_date = img.create_date.substring(0, 10) + '&nbsp;' + img.create_date.substring(11, 18);
if(order_by == 'create_date'){
$('#see_imgs_ul').append(
'<li><img id="see_img_'+ key +'" src="'+ image +'"  data-original=' + image + ' alt="' + create_date +'"><li>'
);
}
else{
$('#see_imgs_ul').prepend(
'<li><img id="see_img_'+ key +'" src="'+ image +'" data-original=' + image + ' alt="' + create_date +'"><li>'
);
}
}
}
}
var op = 0;
function open_img_modal(opt_flag) {
var data_length = data_list.length;
if (opt_flag == 'add_img'){
none_choise();
if(op = 0){
$('#add_img_image').click();
op = 1;
}
$('#add_img_modal')
.modal({
closable  : true,
onDeny    : function(){
},
onApprove : function() {
add_img();
}
})
.modal('show');
}
else if(opt_flag == 'del_img'){
if (data_length > 0){
if(data_length == 1){
$('#del_img_p').html(data_length);
$('.del_img_she').html('她'); }
else{
$('#del_img_p').html(data_length);
$('.del_img_she').html('她们'); }
$('#del_img_modal')
.modal({
closable  : true,
onDeny    : function(){
},
onApprove : function() {
del_img(data_list);
}
})
.modal('show');
}
}
}
$('.add_img').click(function() {
open_img_modal('add_img');
});
function add_img() {
var data = new FormData($('#add_img_form')[0]);
console.info(data);
$.ajax({
url : ajax_img_url,
data: data,
type: 'POST',
processData: false,
contentType: false,
cache: false,
beforeSend:function(xhr, settings){
xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val() );
},
success: function (callback) {
if((callback != 'False') | (callback != false)){
select_img(true, true);
}
else{
open_tishi_modal('Delete Imag is Stop ......')
}
},
error: function (callback) {
open_tishi_modal('Server error ......')
}
})
};
$('.del').click(function() {
open_img_modal('del_img');
});
function del_img(d_list) {
var data = d_list.join('_');
for (var i= 0; i< d_list.length; i++){
var stop_del = $('#stop_delete').val();
if((stop_del == true) | (stop_del == 'true')){
return 0;
}
$.ajax({
url: ajax_img_url,
type: 'DELETE',
data: {'del_img_id': d_list[i], 'pic_id': pic_id},
cache: false,
async: true,
beforeSend:function(xhr, settings){
xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val() );
},
success: function (callback) {
if((callback != 'False') | (callback != false)){
var img_col_out = $('#col_out_'+ callback);
img_col_out.attr({'style': 'display:none;'});
}
else{
open_tishi_modal('Delete Imag is Stop ......')
}
},
error: function (callback) {
open_tishi_modal('Server error ......')
}
});
}
data_list = [];
}
function change_edit(flag){
if(flag){
$('#start_choise').removeClass('disabled');
}
else {
$('#start_choise').addClass('disabled');
}
}
if(all_data_list.length >= 1){
change_edit(true);
}
select_img(null, true);
show_grid_wide();
show_grid_ratio();