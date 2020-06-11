console.log('This is Post Create Form');
const inpFile = document.getElementById("id_post_pick");
const previewContainer = document.getElementById("UserPost_image_Preview");
const previewImage = previewContainer.querySelector(".UserPost_image_preview__image");
const previewDefaultText = previewContainer.querySelector(".UserPost_image_preview_default_text");

inpFile.addEventListener("change", function(){
    const file = this.files[0];

    if (file){
        const reader = new FileReader();

        previewDefaultText.style.display = "none";
        previewImage.style.display = "block";
        reader.addEventListener("load", function(){
            previewImage.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    }
});