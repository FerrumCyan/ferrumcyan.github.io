function shownew(){
    $(".oldimg").css("display","none");
    $(".renlian").css("display","none");
    $(".newimg").css("display","block");
}

function change(){
    $(".newimg").css("display","none");
    $(".oldimg").css("display","block");
    $(".renlian").css("display","block");
    setTimeout("shownew()",4700);
}