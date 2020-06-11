// console.log('This is User List Page....');
let GetTheUserPostBaseContainer = document.getElementById('User_Profile_Posts_Base_Container');
// User Normal Post Container
let User_Profile_Normal_Posts_Base_Container = document.getElementById('User_Profile_Normal_Posts_Base_Container');
// console.log(GetTheUserPostBaseContainer);
let GetTheUserListContainer = document.getElementById('User_Profile_User_List_Base_Container');
let All_Users_List_Holder_Container = document.getElementById('All_Users_List_Holder_Container');

//console.log(User_Profile_Normal_Posts_Base_Container.children.length);
if (All_Users_List_Holder_Container.children.length != 0){
    GetTheUserPostBaseContainer.style.display = "none";
    GetTheUserListContainer.style.display = "";
}
else if(All_Users_List_Holder_Container.children.length == 0){
    GetTheUserListContainer.style.display = "none";
    GetTheUserPostBaseContainer.style.display = "";
}
