//console.log('This is Followers And Following page');

$(document).ready(function() {
// :~~~~~~~~~~~~~:[ This Code is For Like and DisLike A NormalPost ]:~~~~~~~~~~~~~:
    $('.Action_Follow_UnFollow').click(function(e){
        e.preventDefault();
        let SubButton = this;
//        let UserId = $(this).children('input[name$="UserId"]').val(); ( We Use it later...)
        let url = $(this).attr('href');

        //~~~~~~~~~~~~~~~~[ Ajax part Fore Sending Data Without Page-Refresh ]~~~~~~~~~~~~~~~~
        var req = new XMLHttpRequest();
            req.onreadystatechange = function(){
                if (this.readyState == 4 && this.status == 200){
                    if (req.responseText === "False"){
                        SubButton.innerHTML = `<Button class="All_User_List_Container_Inner_Content_Follow_Button">
                        <img src="/static/Images/IconsForFollow_UnFollow/follower.svg" alt="">
                        Follow
                        </Button>`;
                    }
                    else if (req.responseText === "True"){
                        SubButton.innerHTML = `<Button class="All_User_List_Container_Inner_Content_UnFollow_Button">
                        <img src="/static/Images/IconsForFollow_UnFollow/unfollow.svg" alt="">
                        Un Follow
                        </Button>`;
                    }
                }
            };
        req.open("GET", url, true);
        req.send();

    });
});