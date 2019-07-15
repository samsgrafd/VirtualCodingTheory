
/* global $ */
$(document).ready(function() {
    
    var x = 0;
    
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

var inputStrBin = "";
var file = "static/outbin.txt";
var successFile = "succes.txt";
var propability = 1;
var current = "";
var i = 0;
var binaryCount = 0;

function addToSucceed(){
inputStrBin = 'static/outbins.txt';
f = open(inputStrBin,'w');

current = '';

probability();

$(function(){

file = inputStrBin;

});
}



function probability(){
for (i in inputStrBin) {

    binaryCount += 1;
}
    current += i;

    binaryCount +=1;

propability = propability/binaryCount;

console.log("this is propability:" + propability)
 
 
  
if(propability < 0.5)
{
    file +="successFile";
    return true;
}
else{

    file +="Probability error";
    return false;
}

}


var WrongCount = 0;
var RightCount = 0;

$('#b2').click(function(){

download(file);

});


$(".ansver").click(function() {
        
        probability();     
        var ansver = $(this).attr("data-vastaus");
        if (ansver === "1") {
            Next();
            $('#images0').removeClass("hidden");
            RightCount += 1;
            $('#lkmr').html(RightCount);
            addToSucceed();
        }
        else {
            Next();
            $('#vaarin').removeClass("hidden");
            WrongCount += 1;
            $('#lkmw').html(WrongCount);
           
        }
    
     
    });
    


function download(file){
    

    var a = document.createElement('a');
    data = file;
if (window.URL && window.Blob && ('download' in a) && window.atob) {
    // Do it the HTML5 compliant way
    var blob = data;
    var url = blob;
    a.href = url;
    a.download = download.file;
    a.click();
    window.URL.revokeObjectURL(url);
   return file;
}
}
    
    $("#b1").click(function () {
          Next();
        $('#korttivisa').hide();
         $("#b1").hide();


    });

    
});