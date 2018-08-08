
function open_kouza_dropdown() {
$('#kouza_dropdown')
.dropdown({
action: 'hide',
onChange: function(value, text, $selectedItem) {
}
});
}
function open_top_dropdown() {
$('#top_dropdown')
.dropdown({
action: 'hide',
onChange: function(value, text, $selectedItem) {
}
});
}
$('#station').click(function() {
go_s('station');
});
$('#style').click(function() {
go_s('style');
});
$('#safe').click(function() {
go_s('safe');
});
$('#setting').click(function() {
go_s('setting');
});