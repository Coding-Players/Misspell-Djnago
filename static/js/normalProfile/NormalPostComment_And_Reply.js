$(document).ready(function() {
    //  ========================[ For All Normal-Post Comment Purpose ]======================
    $('.Load_NormalPost_Comments').click(function(e) {
        e.preventDefault();
//        alert('clicked');

        //  ========================[ This is for Displaying The Posts ]======================
        let NormalPost_DisplayId = (this.id);
        let Post_Value = $('#Value_PostId_'+NormalPost_DisplayId).val();
        var pageToLoad = $(this).attr('href'); // gets the href of the clicked link
//        alert(NormalPost_DisplayId);
        $('.posts_Comments_Display_section').load(pageToLoad);
        $('#NormalPost_Submition_Form_Textarea').val("");
        $('#Normalr_post_Comments_Id_Get_Here').val(Post_Value);
        $('#Normalr_post_Comments_Id_Get_HereNewUrl').val(pageToLoad);
    });

    //  ========================[ For All Normal-Post Reply Purpose ]======================
    $('.Load_NormalPost_Reply').click(function(e) {
        e.preventDefault();

        //  ========================[ This is for Displaying The Posts ]======================
        let myNormalPost_DisplayId = (this.id);
//        alert(myNormalPost_DisplayId);
        let Reply_Value = $('#Value_PostId_'+myNormalPost_DisplayId).val();
        var pageToLoad = $(this).attr('href'); // gets the href of the clicked link
//        alert(myNormalPost_DisplayId);
        $('.posts_Comments_Display_section').load(pageToLoad);
        $('#NormalPost_Submition_Form_Textarea').val("");
        $('#Normalr_post_Comments_Id_Get_Here').val(Reply_Value);
        $('#Normalr_post_Comments_Id_Get_HereNewUrl').val(pageToLoad);
    });


    //  ========================[ For Submitting Comments And Reply ]======================
    $(document).on('submit', '#NormalPost_Submition_Form', function(event){
         event.preventDefault();
         let NormalComments = $('#NormalPost_Submition_Form_Textarea').val();
         let NormalPostIds = $('#Normalr_post_Comments_Id_Get_Here').val();
         let Csrf_token_val = $('input[name="csrfmiddlewaretoken"]').val();
         if(NormalComments != ""){
//            alert(NormalComments);
           //~~~~~~~~~~~~~~~~[ Ajax part Fore Sending Data Without Page-Refresh ]~~~~~~~~~~~~~~~~
            $.ajax({
                url:"/Account/Create_comment",
                type: "POST",
                data: {NormalComment: NormalComments,
                        NormalPostId: NormalPostIds,
                        csrfmiddlewaretoken: Csrf_token_val
                        },
                success:function(){
//                    alert('comment Created');
                    let NewTergatedUrl = $('#Normalr_post_Comments_Id_Get_HereNewUrl').val();
//                    alert(NewTergatedUrl);
                    $('.posts_Comments_Display_section').load(NewTergatedUrl);
                    $('#NormalPost_Submition_Form_Textarea').val("");

                },
                complete:function(){},
                error:function (xhr, textStatus, thrownError){
                    alert("error doing something");
                }
            });

         }
         else{
            alert('This Fields is Empty');
         }
    });

});

