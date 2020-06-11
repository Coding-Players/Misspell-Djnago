from django.contrib import admin
from Account.models import NormalProfile, ServiceProviderProfile,\
    DistributorProfile, NormalPosts, NormalPostComment, LikeDislike,\
    FollowersFollowing, ChatWithFriends


admin.site.register(NormalProfile)
admin.site.register(ServiceProviderProfile)
admin.site.register(DistributorProfile)
admin.site.register(NormalPosts)
admin.site.register(NormalPostComment)
admin.site.register(LikeDislike)
admin.site.register(FollowersFollowing)
admin.site.register(ChatWithFriends)

