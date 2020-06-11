let messageBoxDisplay = document.getElementById('message_box_Disppaly_Conatainer');
let Scroll_Ydiraction_Container = document.getElementById('Scroll_Ydiraction_Container');
console.log(Scroll_Ydiraction_Container.scrollHeight);
messageBoxDisplay.scrollTop = (Scroll_Ydiraction_Container.scrollHeight - messageBoxDisplay.clientHeight) + 5;

$(document).ready(function() {
    setInterval(function(){
        $('#Scroll_Ydiraction_Container').load(location.href + " #Scroll_Ydiraction_Container");

        messageBoxDisplay.scrollTop = (Scroll_Ydiraction_Container.scrollHeight - messageBoxDisplay.clientHeight) + 5;

    }, 2000);

//    $("#Scroll_Ydiraction_Container").fadeOut(500).fadeIn(500);
});