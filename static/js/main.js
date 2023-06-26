(function ($) {
    "use strict";

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 40) {
            $('.navbar').addClass('sticky-top');
        } else {
            $('.navbar').removeClass('sticky-top');
        }
    });
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
    });

    $("#input-file").on('change',function(){
        var fileName = $("#input-file").val();
        $(".upload-name").val(fileName);
    });

    $(document).ready(function(){            
        var now = new Date();
        var year = now.getFullYear();
        var mon = (now.getMonth() + 1) > 9 ? ''+(now.getMonth() + 1) : '0'+(now.getMonth() + 1); 
        var day = (now.getDate()) > 9 ? ''+(now.getDate()) : '0'+(now.getDate());           
        //년도 selectbox만들기               
        for(var i = 1900 ; i <= year ; i++) {
            $('#year').append('<option value="' + i + '">' + i + '년</option>');    
        }
    
        // 월별 selectbox 만들기            
        for(var i=1; i <= 12; i++) {
            var mm = i > 9 ? i : "0"+i ;            
            $('#month').append('<option value="' + mm + '">' + mm + '월</option>');    
        }
        
        // 일별 selectbox 만들기
        for(var i=1; i <= 31; i++) {
            var dd = i > 9 ? i : "0"+i ;            
            $('#day').append('<option value="' + dd + '">' + dd+ '일</option>');    
        }
        $("#year  > option[value="+year+"]").attr("selected", "true");        
        $("#month  > option[value="+mon+"]").attr("selected", "true");    
        $("#day  > option[value="+day+"]").attr("selected", "true");       
      
    })
    
})(jQuery);

var imgTarget = $('.preview-image .upload-hidden');

imgTarget.on('change', function(){
    var parent = $(this).parent();
    parent.children('.upload-display').remove();

    if(window.FileReader){
        //image 파일만
        if (!$(this)[0].files[0].type.match(/image\//)) return;
        
        var reader = new FileReader();
        reader.onload = function(e){
            var src = e.target.result;
            parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img src="'+src+'" class="upload-thumb"></div></div>');
        }
        reader.readAsDataURL($(this)[0].files[0]);
    }

    else {
        $(this)[0].select();
        $(this)[0].blur();
        var imgSrc = document.selection.createRange().text;
        parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img class="upload-thumb"></div></div>');

        var img = $(this).siblings('.upload-display').find('img');
        img[0].style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(enable='true',sizingMethod='scale',src=\""+imgSrc+"\")";        
    }
});



$(function(){ 

    $("button").click(function(){
      $(".modal").fadeIn();
    });
    
    $(".modal_content").click(function(){
      $(".modal").fadeOut();
    });
    
  });