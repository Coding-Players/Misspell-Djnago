$(document).ready(function() {

    //  ========================[ For All Normal-Post Comment Purpose ]======================
    $('.Load_NormalPost_Comments').click(function(e) {
        e.preventDefault(); // stops the default action of clicking on the link

    //  ========================[ This is for Displaying The Posts ]======================
        let NormalPost_DisplayId = (this.id);
        var pageToLoad = $(this).attr('href'); // gets the href of the clicked link
        alert(pageToLoad);
        $('.posts_Comments_Display_section').load(pageToLoad);

        // This section refresh the Comment Display content After 5 second
//        function reloadCommentBox(){
//            $('#Normla_Posts_Comments_'+NormalPost_DisplayId).load(pageToLoad, function(){
////                $(this).unwrap();
//            }); // loads the remote page into the content div without refresh
//        }
//        reloadCommentBox();
//        setInterval(function(){
//            reloadCommentBox()
//        }, 5000);


    //  ========================[ This is for Creating The Posts ]======================
        if (this.classList != ""){
            $(document).on('submit', '#NormalPost_From_Submit_Holder_'+NormalPost_DisplayId, function(event){
                event.preventDefault();

                let NormalComments = $('#NormalComment_NormalPost_'+NormalPost_DisplayId).val();
                let NormalPostIds = $('#NormalPostId_NormalPost_'+NormalPost_DisplayId).val();
                if (NormalPostIds != ""){
                    let Csrf_token_val = $('input[name="csrfmiddlewaretoken"]').val();

            //~~~~~~~~~~~~~~~~[ Ajax part Fore Sending Data Without Page-Refresh ]~~~~~~~~~~~~~~~~
                    $.ajax({
                        url:"/Account/Create_comment",
                        type: "POST",
                        data: {NormalComment: NormalComments,
                                NormalPostId: NormalPostIds,
                                csrfmiddlewaretoken:Csrf_token_val
                                },
                        success:function(){
                            $('#NormalComment_NormalPost_'+NormalPost_DisplayId).val("");
                            $('#Normla_Posts_Comments_'+NormalPost_DisplayId).load(pageToLoad);


                        },
                        complete:function(){},
                        error:function (xhr, textStatus, thrownError){
                            alert("error doing something");
                        }
                    });
                }
                else{
                    alert('enter Your Comment Please');
                }
            });
        }
    // ~~~~~~~~~~~~~~~~~~[ That part Handeling the Comment Post How many Times ]~~~~~~~~~~~~~~~~~~
        let Normpost_Displaying_object = document.getElementById(NormalPost_DisplayId);
        Normpost_Displaying_object.classList.remove('Load_NormalPost_Comments');

    });

//  ========================[ Only For User Normal Post-Reply/Comment Purpose ]======================
    $('.Load_NormalPost_Only_User_Comments').click(function(e) {
        e.preventDefault(); // stops the default action of clicking on the link

    //  ========================[ This is for Displaying The Posts ]======================
        let NormalPost_DisplayId = (this.id);
        var pageToLoad = $(this).attr('href'); // gets the href of the clicked link
        $('#Normla_Posts_Comments_'+NormalPost_DisplayId).load(pageToLoad); // loads the remote page into the content div without refresh


    //  ========================[ This is for Creating The Posts ]======================
        if (this.classList != ""){
            $(document).on('submit', '#NormalPost_From_Submit_Holder_'+NormalPost_DisplayId, function(event){
                event.preventDefault();

                let NormalComments = $('#NormalComment_NormalPost_'+NormalPost_DisplayId).val();
                let NormalPostIds = $('#NormalPostId_NormalPost_'+NormalPost_DisplayId).val();
                if (NormalPostIds != ""){
                    let Csrf_token_val = $('input[name="csrfmiddlewaretoken"]').val();

            //~~~~~~~~~~~~~~~~[ Ajax part Fore Sending Data Without Page-Refresh ]~~~~~~~~~~~~~~~~
                    $.ajax({
                        url:"/Account/Create_comment",
                        type: "POST",
                        data: {NormalComment: NormalComments,
                                NormalPostId: NormalPostIds,
                                csrfmiddlewaretoken:Csrf_token_val
                                },
                        success:function(){
                            $('#NormalComment_NormalPost_'+NormalPost_DisplayId).val("");
                            $('#Normla_Posts_Comments_'+NormalPost_DisplayId).load(pageToLoad);


                        },
                        complete:function(){},
                        error:function (xhr, textStatus, thrownError){
                            alert("error doing something");
                        }
                    });
                }
                else{
                    alert('enter Your Comment Please');
                }
            });
        }
    // ~~~~~~~~~~~~~~~~~~[ That part Handeling the Comment Post How many Times ]~~~~~~~~~~~~~~~~~~
        let Normpost_Displaying_object = document.getElementById(NormalPost_DisplayId);
        Normpost_Displaying_object.classList.remove('Load_NormalPost_Only_User_Comments');

    });



});
