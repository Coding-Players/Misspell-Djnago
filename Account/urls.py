from django.urls import path
# from Account.views import *
from . import views
from Account.views import NormalProfileView, NormalProfileUpdateView, ServiceProviderProfileUpdateView,\
    NormalPostCreateView, UserNormalPostList


urlpatterns = [
    path('SignUp/', views.SignUp, name='SignUp'),
    path('Login/', views.handleLogin, name='LogIn'),
    path('Logout/', views.handleLogout, name='LogOut'),

    # =========================[ Normal Profile Objects Section ]=======================
    path('profile/<int:pk>/', NormalProfileView.as_view(), name='UserProfile'),
    path('UpdateProfile/<int:pk>/', NormalProfileUpdateView.as_view(), name="NormalProfileUpdate"),

    # =========================[ Normal Profile Objects Section ]=======================
    path('MyPost/', UserNormalPostList.as_view(), name="MY_Post"),
    path('Normal_Post_create/<int:pk>/', NormalPostCreateView.as_view(), name='Normal_Post_create'),
    path('DeleteNormalPost/<int:pk>/', views.normal_post_delete, name='Delete_Normal_Post'),
    path('Normal_Post_Like_Dislike/<int:pk>/', views.normalpost_like_dislike, name='Normal_Post_Like_Dislike'),
    path('Create_comment', views.create_normalPost_comment, name='Creating_NormalPost_Comment'),
    path('List_comment/<int:pk>', views.normal_post_comment_list, name='NormalPost_Comment_List'),

    # =========================[ All Users List Section ]=======================
    path('Users_lists/', views.user_list, name='All_Users_List'),
    path('user_follow_un_follow/<int:pk>', views.user_follow_un_follow, name='Follow_UnFollow'),
    path('Requested_user_friends_list/<int:pk>', views.followers_and_following_list, name='Friends_list'),

    # =========================[ Here We show Users Followers, Following List ]=======================
    path('create_chat/<int:pk>', views.chat_son_chat, name="Create_Chat"),


    # =========================[ Here We show Users Followers, Following List and User Details ]=======================
    path('Requested_user_Details/<int:pk>',
         views.all_user_details_according_to_request, name='All_User_Details_page'),

    # =========================[ Capturing Image Through the WebCam ]=======================
    path('CaptureYourImage', views.change_picture_by_capturing, name='Capture_Your_Image'),
    path('CaptureNormalPost', views.create_post_by_capturing, name='Capture_Create_Normal_Post'),

    # =========================[ Service Provider Profile Objects Section ]=======================
    path('ServiceProvider_Profile_Update/<int:pk>/', ServiceProviderProfileUpdateView.as_view(),
         name="ServiceProvider_Profile_Update"),

    # =========================[ Distributor Profile Objects Section ]=======================
    path('Distributor_Profile_Update/<int:pk>/',
         views.distributor_profile_update, name='Distributor_Profile_Update'),
]

