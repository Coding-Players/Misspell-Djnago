window.onload = (function () {
    var cameraStream = null;
    // alert('This page is loaded');
    let Video_Showing_Container = document.getElementById("Video_Showing_Container");
    let Capture_Button_Holder = document.getElementById('Capture_Button_Holder');
    let btnCapture = document.getElementById("btn-capture");
    let btnTryAgain = document.getElementById( "btn-try-again" );
    let Submition_Form = document.getElementById('Profile_Picture_Changing_Form');
    let WhereToUseThe_Picture = document.getElementById('Where_To_Use_This_Picture');
    let Set_Imge  = document.getElementById('UserPost_image_Preview');
    let Beep1 = new Audio();
    Beep1.src = "/media/Default/Sound/button-20.mp3";

    // Streaming Start:
    let mediaSupport = 'mediaDevices' in navigator;

    if (mediaSupport && null == cameraStream) {

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (mediaStream) {

                cameraStream = mediaStream;

                stream.srcObject = mediaStream;

                stream.play();
            })
            .catch(function (err) {

                console.log("Unable to access camera: " + err);
            });
    }
    else {

        alert('Your browser does not support media devices.');

        return;
    }

    // Capturing Image
    btnCapture.addEventListener("click", captureSnapshot);

    function captureSnapshot() {
        Beep1.play();
        if (null != cameraStream) {

            var ctx = capture.getContext('2d');
            var img = new Image();

            ctx.drawImage(stream, 0, 0, capture.width, capture.height);

            img.src = capture.toDataURL("image/png");
            img.width = 720;
            img.height = 480;

            Set_Imge.innerHTML = "";
            Set_Imge.appendChild( img );

        } else {
            alert('Your SnapShot does not work Properly.')
        }

        // This is for Showing Try Again Button
        btnCapture.classList.add('Hide_This');
        btnTryAgain.classList.remove('Hide_This');
        Video_Showing_Container.classList.add('Hide_This')
        Image_Showing_Container.classList.remove('Hide_This')
        WhereToUseThe_Picture.classList.remove('Hide_This');
    }

    // Try again Capture Your Image
    btnTryAgain.addEventListener('click', captureTryAgain);
    function captureTryAgain(){
        // This is for Showing Try Again Button
        btnCapture.classList.remove('Hide_This');
        btnTryAgain.classList.add('Hide_This');
        Video_Showing_Container.classList.remove('Hide_This')
        Image_Showing_Container.classList.add('Hide_This')
        WhereToUseThe_Picture.classList.add('Hide_This');
    }

    // Profile Picture Update Form Submission
    $(document).on('submit', '#Profile_Picture_Changing_Form', function(event){
        event.preventDefault();
        var image = document.getElementById("capture").toDataURL("image/png");
        let Url = this.action;
        let Csrf_token_value = $('input[name="csrfmiddlewaretoken"]').val();

        // Sending the image data to Servers
        $.ajax({
            url: Url,
            type: "POST",
            data: { imageData : image,
                    csrfmiddlewaretoken: Csrf_token_value },
            success:function(){
                WhereToUseThe_Picture.classList.add('Hide_This');
                Capture_Button_Holder.innerHTML = `<p>Your Profile Is Update Success Fully</p>`;
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){
                WhereToUseThe_Picture.classList.add('Hide_This');
                Capture_Button_Holder.innerHTML = `error doing something`;
            }
        });
    });


    // =====================[ Post Page Section ]=====================
    let GoTo_PostCreate = document.getElementById('Create_Post_Target');
    let GoTo_Previous_Page = document.getElementById('Previous_Page_Target');
    let Post_Create_page = document.getElementById('Post_Create_Page');
    let ImageCapture_Page  = document.getElementById('ImageCapture_Page_Inner_Container');
    GoTo_PostCreate.addEventListener('click', function(){
        ImageCapture_Page.classList.add('ImageCapture_Page_Inner_Container_Hide_This');
        Post_Create_page.classList.remove('Hide_This');
    })

    GoTo_Previous_Page.addEventListener('click', function(){
        ImageCapture_Page.classList.remove('ImageCapture_Page_Inner_Container_Hide_This');
        Post_Create_page.classList.add('Hide_This');
    })

    // Profile Picture Update Form Submission
    $(document).on('submit', '#Capture_Normal_Post_Create_Form', function(eve){
        eve.preventDefault();
        var image = document.getElementById("capture").toDataURL("image/png");
        let Url = this.action;
        let Csrf_token_value = $('input[name="csrfmiddlewaretoken"]').val();
        let Post_Subject = $('input[name="subject"]').val();

        // Sending the image data to Servers
        $.ajax({
            url: Url,
            type: "POST",
            data: { imageData : image,
                    subject: Post_Subject,
                    csrfmiddlewaretoken: Csrf_token_value },
            success:function(){
                ImageCapture_Page.classList.remove('ImageCapture_Page_Inner_Container_Hide_This');
                Post_Create_page.classList.add('Hide_This');
                WhereToUseThe_Picture.classList.add('Hide_This');
                Capture_Button_Holder.innerHTML = `<h4>Your Post Uploaded SuccessFully.</h4>`;
            },
            complete:function(){},
            error:function (xhr, textStatus, thrownError){
                ImageCapture_Page.classList.remove('ImageCapture_Page_Inner_Container_Hide_This');
                Post_Create_page.classList.add('Hide_This');
                WhereToUseThe_Picture.classList.add('Hide_This');
                Capture_Button_Holder.innerHTML = `<h4>Something Going Wrong.</h4>`;
            }
        });
    });

})

