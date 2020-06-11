//console.log('This is Delete And Like page');

$(document).ready(function() {

// :~~~~~~~~~~~~~:[ This Code is For Delete A Post ]:~~~~~~~~~~~~~:
    $('.Delete_The_NormalPost').click(function(e){
        e.preventDefault();
//        alert(this.action);

        // :~~~~~~~:This Section is too important For inserting Link Value:~~~~~~~:
        $('#ProfilePage_Confirmation_Sure_Button').prop("value", this.action);
//        console.log($('#ProfilePage_Confirmation_Sure_Button'));
        $('#Targeting_FadeOut_Div').prop("value", this.id);
    });

    $('#ProfilePage_Confirmation_Sure_Button').click(function(e){
        e.preventDefault();
        console.log(this.value);
        url = this.value;
        Targeting_FadeOut_Div_Value = $('#Targeting_FadeOut_Div').val();
        let Csrf_token_val = $('input[name="csrfmiddlewaretoken"]').val();
//        alert(Targeting_FadeOut_Div_Value);
        $.ajax({
            url:url,
            type: "POST",
            data: {
                csrfmiddlewaretoken:Csrf_token_val
            },
        });
        $('#Target_FadeOut_This_Dive_'+Targeting_FadeOut_Div_Value).fadeOut(1000);
    });

// :~~~~~~~~~~~~~:[ This Code is For Like and DisLike A NormalPost ]:~~~~~~~~~~~~~:
    $('.Normal_Post_Like_Dislike_Action').click(function(e){
        e.preventDefault();
        let LikeButton_id = (this.id);
        let newText = this.parentNode.children[0];
        let url = $(this).attr('href');

        var req = new XMLHttpRequest();
        req.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200){
//                 alert(req.responseText);
                 let like_dislike_data = (eval(req.responseText));
                 let totalLikes_DisLike = (like_dislike_data[0].likes);
                if (like_dislike_data[0].liked === "False"){
                    let Dislike_Button_Image = document.getElementById(LikeButton_id);
                    newText.innerHTML = `Likes:${totalLikes_DisLike}`;
                    Dislike_Button_Image.innerHTML = `<img src="/static/Images/IconForPosts/LikeIcon.svg">`;
                }
                else if (like_dislike_data[0].liked === "True"){
                    let Like_Button_Image = document.getElementById(LikeButton_id);
                    newText.innerHTML = `Likes:${totalLikes_DisLike}`;
                    Like_Button_Image.innerHTML = `<img src="/static/Images/IconForPosts/DisLikeIcon.svg">`;
                }
            }
        };
        req.open("GET", url, true);
        req.send();
    });
});

