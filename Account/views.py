import json
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Account.AccountForm import RegistrationForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import TemplateView, RedirectView, ListView
from Account.models import NormalProfile, ServiceProviderProfile, DistributorProfile, NormalPosts, NormalPostComment,\
    LikeDislike, FollowersFollowing, ChatWithFriends
# from Account.AccountForm import ServiceProviderProfileForm, DistributorProfileForm
from django.utils.decorators import method_decorator

# :~~~~~~~~~~:[This Belows are For Image Processing Purpose ]:~~~~~~~~~~:
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import time, base64


# _________________________________________________________________________
#                      Account Creation Of An User
# _________________________________________________________________________
def SignUp(request):
    """
    ~~~~~~~~~: By This Part of Code We Handle An User SignUp Section :~~~~~~~~~
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        # Get the post parameters
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        users_data = User.objects.all()
        for data in users_data:
            if data.email == email:
                messages.error(request, 'Please User Other Email-Id!')
                return redirect('/Account/SignUp/')
            if data.username == username:
                messages.error(request, 'Please User Other User Name!')
                return redirect('/Account/SignUp/')

        if not username.isalnum():
            messages.error(request, 'UserName only contains Character and Numbers ')
            return redirect('/Account/SignUp/')

        if first_name == username:
            messages.error(request, 'User Name and Full Name Should be unique.')
            return redirect('/Account/SignUp/')

        if len(username) > 14 or len(username) < 5:
            messages.error(request, 'Your UserName should be 5 to 14 character')
            return redirect('/Account/SignUp/')

        # Password should be equal to retype password
        if password != re_password:
            messages.error(request, 'Your 2nd password do not mach')
            return redirect('/Account/SignUp/')
        if len(password) > 40 or len(password) < 8:
            messages.error(request, 'Password contains 8 to 40 number, char. and Symbols')
            return redirect('/Account/SignUp/')

        if form.is_valid():
            # get model object data from form here
            user = form.save(commit=False)

            # Cleaned(normalized) data
            password = form.cleaned_data['password']

            #  User set_password here
            user.set_password(password)
            form.save()
            messages.success(request, f"{first_name} Your Account has been created Successfully.\nPlease Login ")
            return redirect('/Account/Login/')
    else:
        form = RegistrationForm()
    return render(request, 'Account/SignUp.html', {'form': form})


def handleLogin(request):
    """
    ~~~~~~~~~: A User Can LogIn through this section :~~~~~~~~~
    """

    if request.method == 'POST':
        username = request.POST['Login_username']
        password = request.POST['Login_password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{user.normalprofile.name} You are successfully Logged In")
            return HttpResponseRedirect(f"/Account/profile/{request.user.normalprofile.id}/")

        else:
            messages.error(request, 'Invalid credential! please try again.')
            return redirect('/Account/Login/')
    return render(request, "Account/Login.html")


@login_required(login_url='LogIn')
def handleLogout(request):
    """
    ~~~~~~~~~: LogOut an User form this website :~~~~~~~~~
    """
    logout(request)
    messages.success(request, f"You are success fully logout")
    return redirect("/")


# ___________________________________________________________________________________
# =============================[ Normal Profile Update ]=============================
# ___________________________________________________________________________________
@login_required(login_url='LogIn')
# ===[ This Section is Just For Test Case We Must Remove it Later ]===
def Test_page(request, pk):
    normal_prfile_datas = NormalProfile.objects.filter(user=request.user)
    Service_provider_datas = ServiceProviderProfile.objects.filter(user=request.user)
    return render(request, 'templates/NormalProfile_Update_.html')


# User Profile Update Section
@method_decorator(login_required, name='dispatch')
class NormalProfileUpdateView(UpdateView):
    """
    ~~~~~~~~~: This Section is Help Us to Update An User Normal Profile :~~~~~~~~~
    """
    model = NormalProfile
    template_name = 'Account/Profile/profileUpdate.html'
    fields = ["name",
              "age",
              "address",
              "status",
              "phone_no",
              "description",
              "gender",
              "profile_pick",
              "profile_Background_pic"]

    def form_valid(self, form):
        self.object = form.save()
        self.object = self.request.user.normalprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"{self.request.user.normalprofile.name} you successfully Update your Profile")
        return f"/Account/profile/{self.request.user.id}/"


# =============================[ Capture An Image Through WebCam ]=============================
@login_required(login_url='LogIn')
def change_picture_by_capturing(request):
    if request.method == 'POST':
        image_data = request.POST.get('imageData')  # get image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  # Image data
        myfile = "profile-" + time.strftime("%Y%m%d-%H%M%S") + "." + ext  # filename
        fs = FileSystemStorage()
        # filename = fs.save(myfile, data) This is the basic example how ot save this file
        req_user = NormalProfile.objects.get(user=request.user)
        req_user.profile_pick = fs.save("Profile/images/"+myfile, data)
        req_user.save()
        return HttpResponse("okay")
    return render(request, 'Account/CaptureImage/CaptureImage_WebCam.html')


# _________________________________________________________________________
#                   This is Profile Section Of An User
# _________________________________________________________________________
@method_decorator(login_required, name='dispatch')
class NormalProfileView(TemplateView):
    model = NormalProfile
    template_name = 'Account/Profile/Profile.html'

    def get(self, request, *args, **kwargs):
        """
        According to this function We Fetch data from the data base ordering by reverse Id :~~~~~~~~~
        here (N_post = Normal profile posts) :~~~~~~~~~
        (my_post_lists > refer fetching all post from the data base :~~~~~~~~~
        """
        normal_post_lists = NormalPosts.objects.all().order_by("-id")
        norma_post_likes = []
        for post in normal_post_lists:
            is_liked = LikeDislike.objects.filter(normal_post=post, liked_by=request.user)
            if is_liked:
                norma_post_likes.append(post)
        return render(request, self.template_name, {
            'normal_post_lists': normal_post_lists,
            'norma_post_likes': norma_post_likes,
        })


# =============================[ Normal Post Create ]=============================
@method_decorator(login_required, name='dispatch')
class NormalPostCreateView(CreateView):
    """
    ~~~~~~~~~: This Bit of Code is Help Us to Create A Normal Post :~~~~~~~~~
    """
    model = NormalPosts
    template_name = 'Account/Profile/NormalPost_Create.html'
    fields = ['subject', 'post_pick', 'msg']

    def form_valid(self, form):
        self.object = form.save()
        self.object.uploded_by = self.request.user.normalprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"{self.request.user.normalprofile.name} you successfully Create This Post")
        return f"/Account/profile/{self.request.user.id}/"


@login_required(login_url='LogIn')
def create_post_by_capturing(request):
    """
    :~~~~~~~~:~~~~~~~:[ Capture An Image Through WebCam ]:~~~~~~~~:~~~~~~~:
    """
    if request.method == "POST":
        image_data = request.POST.get('imageData')  # get image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  # Image data
        myfile = "profile-" + time.strftime("%Y%m%d-%H%M%S") + "." + ext  # filename
        fs = FileSystemStorage()
        location_img = fs.save("UsrPost/post_img/"+myfile, data)
        subject_text = request.POST.get('subject')
        uploded_by = request.user.normalprofile
        normal_post = NormalPosts.objects.create(post_pick=location_img,
                                                 subject=subject_text,
                                                 uploded_by=uploded_by)
        normal_post.save()
    return HttpResponse('Success')


@login_required(login_url='LogIn')
def normal_post_delete(request, pk):
    """
    ~~~~~~~~~: By this part of Code We Delete A Normal Post :~~~~~~~~~
    """
    if request.method == 'POST':
        """
        ~~~~~~~~~: This Vew Function Delete A particular post according to Post Creator :~~~~~~~~~
        """
        this_post_ = NormalPosts.objects.get(id=pk)
        print(this_post_)
        this_post_.delete()
        return HttpResponse('true')


@method_decorator(login_required, name='dispatch')
class UserNormalPostList(TemplateView):
    """
    ~~~~~~~~~: According to this Class base View we Showing All Users Posts :~~~~~~~~~
    """
    template_name = 'Account/Profile/Profile.html'

    def get(self, request, *args, **kwargs):
        """
        According to this function We Fetch data from the data base ordering by reverse Id
        here (N_post = Normal profile posts)
        (my_post_lists > refer fetching all post from the data base
        """
        my_normal_post_lists = NormalPosts.objects.filter(uploded_by=request.user.normalprofile).order_by("-id")
        return render(request, self.template_name, {
            'my_normal_post_lists': my_normal_post_lists,
        })


@login_required(login_url='LogIn')
def normal_post_comment_list(requests, pk):
    """
    ~~~~~~~~~: This is The List View Of Comments :~~~~~~~~~
    """
    normal_comments = NormalPostComment.objects.filter(post_is=pk).order_by('-timeStamp')
    return render(requests, 'Account/Profile/NormalPostComment/normalPost_Create_Comment.html',
                  {'normal_comments': normal_comments})


@login_required(login_url='LogIn')
def create_normalPost_comment(requests):
    """
    ~~~~~~~~~: Create A Normal Post Comments By this Code_bit :~~~~~~~~~
    """
    if requests.method == 'POST':
        comment = requests.POST.get("NormalComment")
        Comment_by = requests.user.normalprofile
        PostId = requests.POST.get('NormalPostId')
        normalPost = NormalPosts.objects.get(id=PostId)

        Normal_Post_Comment = NormalPostComment(comments=comment, Comment_by=Comment_by, post_is=normalPost)
        Normal_Post_Comment.save()
        return redirect(f"/Account/List_comment/{PostId}")

    return render(requests, 'Account/Profile/NormalPostComment/normalPost_Create_Comment.html')


@login_required(login_url='LogIn')
def normalpost_like_dislike(requests, pk):
    """
    ~~~~~~~~~: To Like & Dis-Like a Post This Section Play a Important Role :~~~~~~~~~
    """
    normal_post = NormalPosts.objects.get(pk=pk)
    liked_by = requests.user
    like = LikeDislike.objects.filter(normal_post=normal_post, liked_by=liked_by)
    if like:
        LikeDislike.disliked(normal_post, liked_by)
        like_count = normal_post.likedislike.liked_by.count()  # This is Like Counter
        total_likes = like_count
        like_data = [{"liked": "False", "likes": total_likes}]
        return HttpResponse(json.dumps(like_data))
    else:
        LikeDislike.liked(normal_post, liked_by)
        like_count = normal_post.likedislike.liked_by.count()  # This is Like Counter
        total_likes = like_count
        like_data = [{"liked": "True", "likes": total_likes}]
        return HttpResponse(json.dumps(like_data))


# ____________________________________________________________________________________
# =============================[ All User Lists ]=============================
# ____________________________________________________________________________________
@login_required(login_url='LogIn')
def user_list(request):
    """
    ~~~~~~~~~: Users List View Section :~~~~~~~~~
    """
    users_list = User.objects.all().order_by('-id')
    follow__un_follow_lists = NormalProfile.objects.all().order_by('-id')

    follow__un_follow = []
    for following in follow__un_follow_lists:
        is_following_user = FollowersFollowing.objects.filter(following_user=following,
                                                         followed_by=request.user.normalprofile)
        if is_following_user:
            follow__un_follow.append(following)
    return render(request, 'Account/Profile/Profile.html', {
        'UsersList': users_list,
        'following__un_following': follow__un_follow,
    })


@login_required(login_url='LogIn')
def user_follow_un_follow(requests, pk):
    """
    ~~~~~~~~~: To Follow & Un-Follow an User We Use This Code :~~~~~~~~~
    """
    following_user = NormalProfile.objects.get(pk=pk)
    followed_by = requests.user.normalprofile
    follow = FollowersFollowing.objects.filter(following_user=following_user, followed_by=followed_by)
    if follow:
        FollowersFollowing.un_follow(following_user, followed_by)
        return HttpResponse('False')
    else:
        FollowersFollowing.follow(following_user, followed_by)
        return HttpResponse('True')


@login_required(login_url='LogIn')
def followers_and_following_list(requests, pk):
    """
    ~~~~~~~~~: This Section Import HowMany Followers and Following Of an User :~~~~~~~~~
    """
    requested_user = User.objects.get(pk=pk)
    all_following_users = FollowersFollowing.objects.filter(followed_by=requested_user.normalprofile)
    return render(requests, 'Account/Profile/Profile.html', {'followings': all_following_users})


@login_required(login_url='LogIn')
def all_user_details_according_to_request(requests, pk):
    """
    ~~~~~~~~~: To Show An User Details We Call This Function :~~~~~~~~~
    """
    requested_user_all = User.objects.get(pk=pk)
    requested_user_all_posts = NormalPosts.objects.filter(uploded_by=requested_user_all.normalprofile)
    return render(requests,
                  'Account/UserDetails_With_Followers_and_Following/UserDetails_With_Followers_and_Following.html',
                  {'Detail_Of_User': requested_user_all,
                   'user_all_posts': requested_user_all_posts})


# ____________________________________________________________________________________
# =============================[ Chat section ]=============================
# ____________________________________________________________________________________
@login_required(login_url='LogIn')
def chat_son_chat(requests, pk):
    """
    ~~~~~~~~~: This Code Bit is UseCase in Case of Chatting With Other User :~~~~~~~~~
    """
    requested_receiver = User.objects.get(pk=pk)
    requested_sender = requests.user
    all_receiver_message_text = ChatWithFriends.objects.filter(sender=requested_sender, receiver=requested_receiver)
    all_sender_message_text = ChatWithFriends.objects.filter(sender=requested_receiver, receiver=requested_sender)
    all_text_messages = all_receiver_message_text | all_sender_message_text
    recent_text_messages = all_text_messages.distinct().order_by('timestamp')
    if requests.method == "POST":
        text_message = requests.POST['message_text']
        chat_message = ChatWithFriends(msg_txt=text_message, receiver=requested_receiver, sender=requested_sender)
        chat_message.save()
        return HttpResponseRedirect(f"/Account/create_chat/{pk}")
    return render(requests, 'ChatSon/chatSon.html',
                  {'Detail_Of_User': requested_receiver,
                   'all_messages': recent_text_messages})


# ____________________________________________________________________________________
# =============================[ Service Profile Update ]=============================
# ____________________________________________________________________________________
@method_decorator(login_required, name='dispatch')
class ServiceProviderProfileUpdateView(UpdateView):
    model = ServiceProviderProfile
    template_name = 'Account/ServiceProvider_Profile/ServiceProvider_Profile_Update_form.html'
    fields = ["SerV_name",
              "SerV_birth_date",
              "SerV_age",
              "SerV_address",
              "SerV_phone_no",
              "SerV_gender",
              "SerV_Profile_pick"]

    def form_valid(self, form):
        self.object = form.save()
        self.object = self.request.user.serviceproviderprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, f"{self.request.user.normalprofile.name} "
                                       f"You Successfully Create Your Service Provider Account.")
        return f"/Account/profile/{self.request.user.id}/"


@login_required(login_url='LogIn')
def distributor_profile_update(request, pk):
    # form = DistributorProfileForm
    # print(form)
    return render(request,
                  'Account/Distributor_Profile/Distributor_Profile_Update_Form.html')

