// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

function arabic(){
    document.getElementById('hebrew').innerHTML = 'يعمل مشروع نيفاشوت على نشر الوعي بمجال الصحة النفسية في المجال العام من خلال الأحداث الثقافية والفن والخطاب. ويشجع مشروع نيفاشوت على اتخاذ إجراءات مهمة على مدار العام ، من أجل تغيير الخطاب الحالي وزيادة الوعي العام بأهمية التعامل مع المعضلة. لكل من الأشخاص الذين يعانون من مشاكل نفسية ، سواء بالنسبة لمن حولهم (أفراد الأسرة والأصدقاء) ، ولكل واحد منا - حتى نتعلم كيف نتصرف ونشارك ونطلب المساعدة في أوقات الأزمات دون أن نخجل من وصمه عار. 
بمبادرة من "نفشوت" يقام "أسبوع صنع النفوس" كل عام - أسبوع كامل يقوم فيه النشطاء في مجالات الفن والروح بخلق لقاءات في المجال العام تساهم فيه.
 من اجل توعية الجمهور بمجال الصحة النفسية والأشخاص الذين يواجهون صعوبات في هذا المجال. تقام خلال الأسبوع العديد من الفعاليات المتنوعة ، كل ذلك بمبادرة من المنظمات والأماكن وخاصة الأشخاص الذين يشاركوننا  في اهداف متشابهه :
 رفع مستوى الوعي العام في عالم الصحة النفسية ، وتقليل وصمة العار تجاه الأشخاص الذين يتعاملون مع الأمراض العقلية.
 بدأ "أسبوع صنع النفوس" كمبادرة مقدسية ، وخلال العامين الأولين جرت الأحداث في منطقة عامة في القدس. في عام 2020 ، بسبب التباعد الاجتماعي والقيود حول الوباء
 جرت الأحداث في مكان عام خارجاً في القدس. في عام 2020 ، وبسبب التباعد الاجتماعي والقيود المحيطة بوباء كورونا ، توسع النشاط جغرافيا وكانت الأحداث في الغالب افتراضية. أدت هذه القفزة إلى حقيقة أن أسبوع نيفاشوت يقام اليوم في جميع أنحاء البلاد مع وجود مراكز في الشمال والجنوب والوسط وبالطبع في القدس. 
نعتقد أنه من خلال المواجهات الإنسانية التي تنطوي على الفن والإبداع والخطاب ، سيكون من الممكن الوصول إلى قلوب كثيرة. نؤمن بأن نشر الوعي في مجال الصحة النفسية مسؤولية علينا جميعًا تجاه المجتمع الذي نعيش فيه وتجاه الأفراد الذين يتكونون منه.'
}

// owl carousel slider js
var owl = $('.project_carousel').owlCarousel({
    loop: false,
    margin: 15,
    center: true,
    startPosition: 2,
    autoplay: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    autoplayHoverPause: true,
    responsive: {
        0: {
            center: false,
            items: 1,
            margin: 0
        },
        769: {
            items: 2,
        },
        992: {
            center: true,
            items: 3
        }
    }
})


// owl.owlcarousel2_filter

$('.owl-filter-bar').on('click', '.item', function (e) {
    var $items = $('.owl-filter-bar a')
    var $item = $(this);
    var filter = $item.data('owl-filter')
    $items.removeClass("active");
    $item.addClass("active");
    owl.owlcarousel2_filter(filter);

    e.preventDefault();
})
/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}