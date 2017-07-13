var main=function(){$('.icon-menu').click(function(){
$('.menu').animate({left:"0px"},200).addClass('open');
$('body').animate({left:"285px"},200);});
$('.icon-close').click(function()
{$('.menu').animate({left:"-285px"},200).removeClass('open');
$('body').animate({left:"0px"},200);});};
$(document).ready(main);

    function customRadio(radioName){
        var radioButton = $('input[name="'+ radioName +'"]');
        $(radioButton).each(function(){
            $(this).wrap( "<span class='custom-radio'></span>" );
            if($(this).is(':checked')){
                $(this).parent().addClass("selected");
            }
        });
        $(radioButton).click(function(){
            if($(this).is(':checked')){
                $(this).parent().addClass("selected");
            }
            $(radioButton).not(this).each(function(){
                $(this).parent().removeClass("selected");
            });
        });
    }
    $(document).ready(function (){
        customRadio("browser");
        customRadio("search-engine");            
        customRadio("confirm");
    })