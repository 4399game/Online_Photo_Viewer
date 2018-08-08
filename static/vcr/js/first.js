$(function(){
    open_Kouza_sidebar = function() {
        $('#kouza_sidebar')
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle')
        ;
    };
    open_kouza_dropdown = function() {
        $('#kouza_dropdown')
            .dropdown({
                action: 'hide',
                onChange: function(value, text, $selectedItem) {
                    console.info('Kouza_dropdown!!!');
                }
            })
        ;
    };
    open_top_dropdown = function() {
        $('#top_dropdown')
            .dropdown({
                action: 'hide',
                onChange: function(value, text, $selectedItem) {
                    console.info('top_dropdown!!!');
                }
            })
        ;
    }
});
// User Cnenter Href
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