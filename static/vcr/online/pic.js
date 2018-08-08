
var kuukann_id = $('#kuukann_id').val();
var media_url = $('#media_url').val();
$('#kuukann_menu .item').tab();
$('.pic_edit_menu') .dropdown();
function select_pic() {
data = {
'kuukann_id': kuukann_id,
'select_flag': 'all'
};
$.get(ajax_pic_url, data, function (ret) {
show_pic(ret);
});
}
function show_pic(pic_list) {
for(var i= 0; i< pic_list.length; i ++){
var pic = pic_list[i];
var index = pic.id;
var name = pic.name;
var image = pic.image;
var create_date = pic.create_date;
}
}
select_pic();
function open_add_pic_modal() {
$('#add_pic_modal').modal({
onApprove : function() {
add_pic();
}
}).modal('show');
}
function add_pic(){
var imgsrc = $('#add_pic_image_2').attr('src');
form_data = new FormData();
form_data.append('pic_name', $('#add_pic_name').val());
form_data.append('kuukann_name', $('#kuukann_name').val());
form_data.append('pic_image', dataURLtoBlob(imgsrc))
blob_upload(ajax_pic_url, form_data, 'Photo album create failed !!!');
}
function open_edit_pic_modal(pic_id) {
$.get(ajax_pic_url, {'pic_id': pic_id, 'select_flag': 'one'}, function (ret){
var id = ret['id'];
var name = ret['name'];
var image = ret['image'];
$('#edit_pic_id').val(id);
$('#edit_pic_name').val(name);
$('#edit_pic_image_2').attr({ 'src': media_url + image });

$("#edit_pic_modal").modal({
onApprove : function() {
edit_pic();
}
}).modal('show');
});
}
var edit_bool = true;
function edit_pic() {
var image = $('#edit_pic_image').val();
var name = $('#edit_pic_name').val();
if((image == undefined) | (image == null) | image == ''){
if(edit_bool == true){
edit_bool = false;
data = {
'pic_id': $('#edit_pic_id').val(),
'pic_name': name
}
$.ajax({
url: ajax_pic_url,
data: data,
type: 'PUT',
dataType: 'json',
cache: false,
beforeSend:function(xhr, settings){
xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val() );
},
success: function (callback) {
if ((callback != 'False') | (callback != false)) {
console.info(callback);
var index = data['pic_id'];
var name = callback['name'];
$('#pic_name_' + index).html(name);
edit_bool = true;
}
else{
open_tishi_modal('Photo album delete failed !!!')
}
},
error: function (callback) {
open_tishi_modal('Server error ......')
}
});
}
}
else{
if(edit_bool == true){
edit_bool = false;
var imgsrc = $('#edit_pic_image_2').attr('src');
form_data = new FormData();
form_data.append('pic_id', $('#edit_pic_id').val());
form_data.append('pic_name', $('#edit_pic_name').val());
form_data.append('pic_image', dataURLtoBlob(imgsrc));
var web_pic_url = kuukann_url + $('#kuukann_name').val() + '/' + $('#edit_pic_name').val();
$.ajax({
url: web_pic_url,
type: 'POST',
data: form_data,
processData: false,
contentType: false,
cache: false,
beforeSend:function(xhr, settings){
xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
},
success: function (callback) {
if ((callback != 'False') | (callback != false)) {
var index = callback['id'];
var image = callback['image'];
var name = callback['name'];
$('#pic_name_' + index).html(name);
$('#the_img_' + index).attr({'src': media_url + image});
}
else{
open_tishi_modal('Photo album edit failed !!!');
}
edit_bool = true;
},
error: function (callback) {
open_tishi_modal('Server error ......')
}
});
}
}
}
function open_del_pic_modal(pic_id) {
var dl_length = data_list.length;
$('#del_pic_name').html(dl_length);
$('#del_pic_modal')
.modal('setting', 'transition', 'vertical flip')
.modal({
closable  : false,
onDeny    : function(){
$('#del_pic_modal').modal('hide');
},
onApprove : function() {
del_pic();
}
})
.modal('show');
}
function del_pic(){
var pic_id_l = data_list.join('_');
data = {
'pic_id': pic_id_l,
'kuukann_id': kuukann_id,
};
$.ajax({
url: ajax_pic_url,
type: 'DELETE',
data: data,
cache: false,
async: true,
beforeSend:function(xhr, settings){
xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val() );
},
success: function (callback) {
if ((callback != 'False') | (callback != false)) {
console.info(callback);
var callback = eval(callback['pic_id_l']);
for(var i= 0; i< callback.length; i ++){
$('#col_' + callback[i]).attr({'style': 'display: none'})
}
}
else{
open_tishi_modal('Photo album delete failed !!!')
}
},
error: function (callback) {
open_tishi_modal('Server error ......')
}
});
};
blob_upload = function (url, form_data, error_text) {
$.ajax({
url: url,
type: 'POST',
data: form_data,
processData: false,
contentType: false,
cache: false,
beforeSend:function(xhr, settings){
xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());
},
success: function (callback) {
if ((callback != 'False') | (callback == false)) {
location.reload();
}
else{
open_tishi_modal(error_text);
}
},
error: function (callback) {
open_tishi_modal('Server error ......')
}
});
};
var choise_bar = $('#choise_bar');
$('.none').click(function () {
none_choise();
change_dom(choise_bar ,false, 0);
change_dom($('.add_pic') ,true, 0);
});
$('.fan').on('click', function () {
alert(data_list);
fan_choise();
});
function none_choise() {
for(var i= 0; i< data_list.length; i++ ){
change_pic_bg(data_list[i], false);
}
data_list = [];
}
$('.edit').click(function () {
open_edit_pic_modal(data_list[0]);
});
$('.del').click(function () {
open_del_pic_modal();
});
function fan_choise() {
var new_all_list = $.extend(true, [], all_data_list);
for (var i= 0; i< data_list.length; i++ ){
var j = $.inArray(data_list[i], new_all_list);
if (j != -1 ){
new_all_list.splice(j, 1); }
}
for(var i= 0; i< data_list.length; i++ ){
change_pic_bg(data_list[i], false);
}
data_list = new_all_list;
for(var i= 0; i< data_list.length; i++ ){
change_pic_bg(data_list[i], true);
}
choise_ctrl();
}
show_num()