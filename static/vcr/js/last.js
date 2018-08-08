// 改变颜色
$('.color').addClass(kouza_ctrl.color_val);


// Page监听
if(web_ctrl.page_flag == 'index'){
    $('#center').height(window.h + 30);
}

// 模态框事件
$('.cancle').click(function(){
    $('.modal').modal('hidden');
})
