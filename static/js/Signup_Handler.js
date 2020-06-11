
// ==============[ This section is for Password In SignUp Form ]=================
var Password_Visibility = document.getElementById("Password_icon_In_S");
var Input_password = document.getElementById("id_password");
let password = true;

// This is for SignUp Form Password Hide and show
Password_Visibility.addEventListener('click', function(){
    if (password){
        Input_password.setAttribute('type', 'text');
        Password_Visibility.innerHTML = `
        <img src="/static/Images/IconsForHome/SignUpIcons/visibility.svg" alt="VisibleIcon">
        `;
    }else{
        Input_password.setAttribute('type', 'password');
        Password_Visibility.innerHTML = `
        <img src="/static/Images/IconsForHome/SignUpIcons/invisible.svg" alt="InvisibleIcon">
        `;

    }
    password =! password;
})

// This section is for ConfirmPassword Hide and show
var Confirm_Password_Visibility = document.getElementById("ConfirmPassword_icon_In_S");
var Confirm_Input_password = document.getElementById("id_re_password");
Confirm_Password_Visibility.addEventListener('click', function(){
    if (password){
        Confirm_Input_password.setAttribute('type', 'text');
        Confirm_Password_Visibility.innerHTML = `
        <img src="/static/Images/IconsForHome/SignUpIcons/visibility.svg" alt="VisibleIcon">
        `;
    }else{
        Confirm_Input_password.setAttribute('type', 'password');
        Confirm_Password_Visibility.innerHTML = `
        <img src="/static/Images/IconsForHome/SignUpIcons/invisible.svg" alt="InvisibleIcon">
        `;

    }
    password =! password;
})




