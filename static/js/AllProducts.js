window.onload = function(event){

    document.querySelectorAll('.HomeCard_Bargain_TiggerButton').forEach(ClickBargain =>{

        ClickBargain.addEventListener('click', function(e){
        // alert('Hello world');
        // data = this.id; //In This Way We Can Select an Id
        // console.log(data);

            let HomeCard_Holders_MessageBox_body_MainContainer = document.querySelector(".HomeCard_Holders_MessageBox_body_MainContainer");
            HomeCard_Holders_MessageBox_body_MainContainer.classList.remove('HomeCard_Holders_MessageBox_body_MainContainer_Hide');

            let Close_HomeCard_Message_Box = document.querySelector('.Close_HomeCard_Message_Box');
            Close_HomeCard_Message_Box.addEventListener('click', function(e){
                HomeCard_Holders_MessageBox_body_MainContainer.classList.add('HomeCard_Holders_MessageBox_body_MainContainer_Hide');
            });
            e.preventDefault;

    })
    event.preventDefault;
});



}

