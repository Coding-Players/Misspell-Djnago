window.onload = function(event){
        // =============================[ This is For Showing More Details Of an User ]===========================
    let User_Profile_More_Details_Link = document.getElementById('User_Profile_More_Details_Link');
//    console.log(User_Profile_More_Details_Link)
    User_Profile_More_Details_Link.addEventListener('click', function(e){
        let User_Profile_Deatis_Holder_Container_Hide = document.getElementById('User_Profile_Deatis_Holder_Container_Hide');
        User_Profile_Deatis_Holder_Container_Hide.classList.toggle('User_Profile_Deatis_Holder_Container_Hide');
        if (User_Profile_More_Details_Link.innerHTML === "More") {
            User_Profile_More_Details_Link.innerHTML = "Less";
            User_Profile_More_Details_Link.style = 'color: red';
        } else {
            User_Profile_More_Details_Link.innerHTML = "More";
            User_Profile_More_Details_Link.style = 'color: #159AC4;';
        }
    });
    event.preventDefault();

    // =============================[ This is For Comment Tiggering Section ]===========================
    document.querySelectorAll('.User_Profile_Comment_Target').forEach(ClickCommentBtn =>{

        ClickCommentBtn.addEventListener('click', function(e){
            e.preventDefault;
            let CommentBtnId = this.id;
//            console.log(CommentBtnId);
            let User_Profile_Othere_Dynamic_Content_Container_Hide = document.getElementById('User_Profile_Othere_Dynamic_Content_Container_Hide');
            let User_Profile_MessageBox_Popup_Container = document.getElementById('User_Profile_MessageBox_Popup_Container');

            // ~~~~~~~#~~~~~~~#[ Add Comment Box ]#~~~~~~~#~~~~~~~
            User_Profile_Othere_Dynamic_Content_Container_Hide.classList.add('User_Profile_Othere_Dynamic_Content_Container_Hide');
            User_Profile_MessageBox_Popup_Container.classList.remove('User_Profile_MessageBox_Popup_Container_Hide');


            // ~~~~~~~#~~~~~~~#[ Add PopUp Image In Comment Section ]#~~~~~~~#~~~~~~~
            let PostImageLink = document.getElementById('NormalPost_Image_'+CommentBtnId);
            if (PostImageLink != null){
                // console.log(PostImage);
                PostImage = PostImageLink.src;
                let NormalPost_Image_Copy = document.querySelector('.NormalPost_Image_Copy_ImageAdd');
                NormalPost_Image_Copy.setAttribute("src", PostImage);
            }


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

     //  ========================[ This is for alerting Confirmation Delete Box ]======================
    document.querySelectorAll('.Delete_The_NormalPost').forEach(ClickPostDeleteBtn =>{

    ClickPostDeleteBtn.addEventListener('click', function(e){
        if (this.classList != ""){

            let Profile_Page_User_Action_Confirmation_Container = document.getElementById('Profile_Page_User_Action_Confirmation_Container');
            Profile_Page_User_Action_Confirmation_Container.classList.remove('Profile_Page_User_Action_Confirmation_Container_Hide');

            // If the User isn't Sure then we do this
            let ProfilePage_Confirmation_NoteSure_Button = document.querySelector('.ProfilePage_Confirmation_NoteSure_Button');
            ProfilePage_Confirmation_NoteSure_Button.addEventListener('click', function(e){
                Profile_Page_User_Action_Confirmation_Container.classList.add('Profile_Page_User_Action_Confirmation_Container_Hide');
            });

            // If the User isn't Sure then we do this
            let ProfilePage_Confirmation_Sure_Button = document.querySelector('.ProfilePage_Confirmation_Sure_Button');
            ProfilePage_Confirmation_Sure_Button.addEventListener('click', function(e){
                Profile_Page_User_Action_Confirmation_Container.classList.add('Profile_Page_User_Action_Confirmation_Container_Hide');
            });
        }

        });

    });



};

