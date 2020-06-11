console.log('This is Full Profile page')

window.onload = function(event){

    // =============================[ This is For Comment Tiggering Section ]===========================
    document.querySelectorAll('.User_Profile_Comment_Target').forEach(ClickCommentBtn =>{

        ClickCommentBtn.addEventListener('click', function(e){
            e.preventDefault();
            let CommentBtnId = this.id;
            let User_Profile_Othere_Dynamic_Content_Container_Hide = document.getElementById('User_Profile_Othere_Dynamic_Content_Container_Hide');
            let User_Profile_MessageBox_Popup_Container = document.getElementById('User_Profile_MessageBox_Popup_Container');

            // ~~~~~~~#~~~~~~~#[ Add Comment Box ]#~~~~~~~#~~~~~~~
            User_Profile_Othere_Dynamic_Content_Container_Hide.classList.add('User_Profile_Othere_Dynamic_Content_Container_Hide');
            User_Profile_MessageBox_Popup_Container.classList.remove('User_Profile_MessageBox_Popup_Container_Hide');


            // ~~~~~~~#~~~~~~~#[ Add PopUp Image In Comment Section ]#~~~~~~~#~~~~~~~
            let PostImage = document.getElementById('NormalPost_Image_'+CommentBtnId).src;
            // console.log(PostImage);
            let NormalPost_Image_Copy = document.querySelector('.NormalPost_Image_Copy_ImageAdd');
            NormalPost_Image_Copy.setAttribute("src", PostImage);


                // ~~~~~~~#~~~~~~~#[ Close Comment Box ]#~~~~~~~#~~~~~~~
                document.querySelectorAll('.Remove_User_Profile_MessageBox_Popup_Container').forEach(RemoveCommentBox =>{

                    RemoveCommentBox.addEventListener('click', function(event){
                        event.preventDefault();
                        User_Profile_MessageBox_Popup_Container.classList.add('User_Profile_MessageBox_Popup_Container_Hide');
                        User_Profile_Othere_Dynamic_Content_Container_Hide.classList.remove('User_Profile_Othere_Dynamic_Content_Container_Hide');

                    })
                });

        })
    });
    event.preventDefault;
}

