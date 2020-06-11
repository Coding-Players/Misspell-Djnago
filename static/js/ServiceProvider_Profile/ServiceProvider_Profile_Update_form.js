let FirstPortion_Of_Form = document.getElementById('Main_From_Container_Form_first');
//console.log(FirstPortion_Of_Form);
let SecondPortion_Of_Form = document.getElementById('Main_From_Container_Form_second');
let Next_Section_Btn = document.getElementById('NextSection_Of_Form_InnerContainer');
let Previous_Section_Btn = document.getElementById('PreviousSection_Of_Form_InnerContainer');

Next_Section_Btn.addEventListener('click', function(e){
    e.preventDefault();
    // alert('clicked');
    FirstPortion_Of_Form.classList.add('Main_From_Container_Form_first_Hide');
    SecondPortion_Of_Form.classList.remove('Main_From_Container_Form_second_Hide');
})

Previous_Section_Btn.addEventListener('click', function(e){
    e.preventDefault();
    FirstPortion_Of_Form.classList.remove('Main_From_Container_Form_first_Hide');
    SecondPortion_Of_Form.classList.add('Main_From_Container_Form_second_Hide');
})

// User Profile Image Preview
const inpFile_Profile_pick = document.getElementById("id_SerV_Profile_pick");
const previewContainer_Profile_pick = document.getElementById("SerV_Profile_image_Preview");
const previewImage_Profile_pick = previewContainer_Profile_pick.querySelector(".SerV_Profile_image_preview__image");
const previewDefaultText_Profile_pick = previewContainer_Profile_pick.querySelector(".SerV_Profile_image_preview_default_text");

inpFile_Profile_pick.addEventListener("change", function(){
    const file = this.files[0];

    if (file){
        const reader = new FileReader();

        previewDefaultText_Profile_pick.style.display = "none";
        previewImage_Profile_pick.style.display = "block";
        reader.addEventListener("load", function(){
            previewImage_Profile_pick.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    }
});