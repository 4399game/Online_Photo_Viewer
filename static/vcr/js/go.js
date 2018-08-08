
go_in_kuukann = function() {
    location.href = kuukann_url + $('#def_kuukann').val();
}

go_in_pic = function(kuukann_name, pic_name) {
    location.href = kuukann_url + kuukann_name + '/' + pic_name;
}

go_in_s = function(s_name, param){
    if(param != null){
        location.href = kouza_url + s_name + '/' + param;
    }
    else{
        location.href = kouza_url + s_name;
    }
}
