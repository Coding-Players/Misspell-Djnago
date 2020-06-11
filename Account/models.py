from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.timezone import now


# ______________________________________________________________________
#                       That Is Normal Profile Section
# ______________________________________________________________________
class NormalProfile(models.Model):
    """
    This is "ALL USERS PROFILE" Model
    """
    name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    age = models.IntegerField(default=12, validators=[MinValueValidator(12)])
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default="I use this app to help others...", null=True, blank=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],
                                max_length=15,
                                null=True,
                                blank=True
                                )
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    profile_pick = models.ImageField(upload_to='Profile/images',
                                     null=True, blank=True
                                     )
    profile_Background_pic = models.ImageField(upload_to='Profile/background_Image',
                                               null=True, blank=True
                                               )

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = NormalProfile.objects.get(id=self.id)
            if this.profile_pick != self.profile_pick:
                this.profile_pick.delete(save=False)
            if this.profile_Background_pic != self.profile_Background_pic:
                this.profile_Background_pic.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(NormalProfile, self).save(*args, **kwargs)


# =========================[ User Posts Section ]=======================
class NormalPosts(models.Model):
    """
    Normal post Creating model.
    """
    post_pick = models.ImageField(upload_to='UsrPost/post_img', null=True)
    subject = models.CharField(max_length=75)
    msg = models.TextField(null=True, blank=True)
    creat_date = models.DateTimeField(auto_now_add=True)
    uploded_by = models.ForeignKey(to=NormalProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.subject

    def delete(self, *args, **kwargs):
        """
        Deleting previous post image file
        """
        self.post_pick.delete()
        super().delete(*args, **kwargs)

    @property
    def get_comments_total(self):
        all_comment = NormalPostComment.objects.filter(post_is=self.id)
        total_comment = all_comment.count()
        return total_comment


class NormalPostComment(models.Model):
    """
    Normal Post Comment and reply Model
    """
    sr_no = models.AutoField(primary_key=True)
    comments = models.TextField()
    Comment_by = models.ForeignKey(to=NormalProfile, on_delete=models.CASCADE, related_name='Comment_by')
    post_is = models.ForeignKey(to=NormalPosts, on_delete=models.CASCADE, related_name='post_is')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.comments[0:20]) + "....By " + str(self.Comment_by.name) + "...Post Is: " + str(self.post_is)


class LikeDislike(models.Model):
    """
    Normal Post Like and Dislike Model
    """
    liked_by = models.ManyToManyField(User, related_name='NormalPost_Like_by')
    normal_post = models.OneToOneField(to=NormalPosts, on_delete=models.CASCADE)

    # This is for liking purpose
    @classmethod
    def liked(cls, normal_post, liked_by_user):
        obj, create = cls.objects.get_or_create(normal_post=normal_post)
        obj.liked_by.add(liked_by_user)

    # This is for dis-liking purpose
    @classmethod
    def disliked(cls, normal_post, liked_by_user):
        obj, create = cls.objects.get_or_create(normal_post=normal_post)
        obj.liked_by.remove(liked_by_user)

    @property
    def get_total_like(self):
        likes = self.liked_by
        total_likes = likes.count()
        return total_likes

    def __str__(self):
        return str(self.normal_post)+" upload by: "+str(self.normal_post.uploded_by)


# =========================[ User Follow-UnFollow Section ]=======================
class FollowersFollowing(models.Model):
    """
    Followers, Following By, Un Follow etc. Of an User.
    """
    followed_by = models.ManyToManyField(to=NormalProfile, related_name='following')
    following_user = models.OneToOneField(to=NormalProfile, on_delete=models.CASCADE)

    # This is for Follow purpose
    @classmethod
    def follow(cls, following_user, followed_by_user):
        obj, create = cls.objects.get_or_create(following_user=following_user)
        obj.followed_by.add(followed_by_user)

    # This is for Un-Follow purpose
    @classmethod
    def un_follow(cls, following_user, followed_by_user):
        obj, create = cls.objects.get_or_create(following_user=following_user)
        obj.followed_by.remove(followed_by_user)

    def __str__(self):
        return "Followers Of: " + str(self.following_user.name)


# =========================[ User Chat-Message Section ]=======================
class ChatWithFriends(models.Model):
    msg_txt = models.TextField(max_length=255)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    # msg_img = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __srt_(self):
        return str(self.msg_txt)

    class Meta:
        ordering = ('timestamp',)


# ______________________________________________________________________
#                 That Is Service Provider Profile Section
# ______________________________________________________________________
class ServiceProviderProfile(models.Model):
    """
    This is "SERVICE PROVIDER PROFILE" MODEL
    Here (SerV) => (service provider)
    """
    SerV_name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    SerV_birth_date = models.DateField(null=True)
    SerV_age = models.IntegerField(default=12, validators=[MinValueValidator(12), MaxValueValidator(80)])
    SerV_address = models.CharField(max_length=255, default='')
    SerV_phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15)
    SerV_gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    SerV_Profile_pick = models.ImageField(upload_to='SerVProfile/images',
                                          null=True, blank=True)

    def __str__(self):
        return '%s' % self.SerV_name

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = ServiceProviderProfile.objects.get(id=self.id)
            if this.SerV_Profile_pick != self.SerV_Profile_pick:
                this.SerV_Profile_pick.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(ServiceProviderProfile, self).save(*args, **kwargs)


# ______________________________________________________________________
#                 That Is Distributor Profile Section
# ______________________________________________________________________
class DistributorProfile(models.Model):
    """
    This is "DISTRIBUTOR PROFILE" Model
    Here (DisB) => ( distributor )
    """
    DisB_name = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    DisB_birth_date = models.DateField(null=True)
    DisB_age = models.IntegerField(default=12, validators=[MinValueValidator(12), MaxValueValidator(80)])
    DisB_address = models.CharField(max_length=255, default='')
    DisB_phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15)
    DisB_gender = models.CharField(max_length=10,
                              default="Male",
                              choices=(("Male", "Male"),
                                       ("Female", "Female"),
                                       ("TransGen", "TransGen")
                                       )
                              )
    DisB_Profile_pick = models.ImageField(upload_to='DisB_Profile_pick/images',
                                          null=True, blank=True)

    def __str__(self):
        return '%s' % self.DisB_name

    def save(self, *args, **kwargs):
        """
        This part is very important for uploading a file because
        It will replace the previous file and insert the new file.
        :return: delete old file when replacing by updating the file
        """
        try:
            this = DistributorProfile.objects.get(id=self.id)
            if this.DisB_Profile_pick != self.DisB_Profile_pick:
                this.DisB_Profile_pick.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(DistributorProfile, self).save(*args, **kwargs)

