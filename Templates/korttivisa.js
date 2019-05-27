/* global $ */
$(document).ready(function() {
    
    var x = 0;
    var startingTime = 100;




    function Next()
    {
        ShowQuestions();

        x += 1;

    }
 function ShowQuestions() {


     var show = $('#questioncards' + x).removeClass("hidden");
     var hide = $('#questioncards' + (x - 1)).addClass("hidden");

     $(hide).addClass("hidden");

     $(show).removeClass("hidden");

}

var WrongCount = 0;
var RightCount = 0;

    $(".ansver").click(function() {


        var ansver = $(this).attr("data-vastaus");
        if (ansver === "1") {
            Next();
            $('#images0').removeClass("hidden");
            RightCount += 1;
            $('#lkmr').html(RightCount);
        }
        else {
            Next();
            $('#vaarin').removeClass("hidden");
            WrongCount += 1;
            $('#lkmw').html(WrongCount);
        }
    });


    $("#b1").click(function () {
          Next();
        $('#korttivisa').hide();
         $("#b1").hide();

    });

    
});