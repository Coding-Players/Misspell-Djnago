// ===============================[ Notification Section If Success or Un-success ]==================================

let Cancel_Notification_Messages = document.getElementById("Cancil_Notification_message");
if (Cancel_Notification_Messages != null){
    Cancel_Notification_Messages.addEventListener('click', function(e){
        let ShowNotiFication_Messages = document.getElementById("Notification_Message");
        ShowNotiFication_Messages.classList.add('Notification_Message_DisplayNone');

    });
};

let Auto_Hide_Notification_message = document.getElementById("Notification_Message");
if (Auto_Hide_Notification_message != null){
    setTimeout(function(){
        Auto_Hide_Notification_message.classList.add('Notification_Message_DisplayNone');
    }, 8000);
}