from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# For Managing User Profile Picture
class UserProfilePhoto(models.Model):
    sno = models.AutoField(primary_key=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="profilePhotos")
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# For Managing Phone Numbers
class PhoneNumber(models.Model):
    sno = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=13 ,default="")    #phone number   
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# For Managing Video Data
class VideoData(models.Model):
    sno = models.AutoField(primary_key=True)
    video_title = models.CharField(max_length=1000)
    video_desc = models.CharField(max_length=5000)
    video_keywords = models.CharField(max_length=4000, default="")
    video_likes = models.IntegerField(default=0)
    video_views = models.IntegerField(default=0)
    video_report_count = models.IntegerField(default=0)
    video_thumbnail = models.ImageField(
        null=True, blank=True, upload_to="thumbnailPhotos")
    video_file = models.FileField(upload_to="videoFiles", null=False)
    notes_file = models.FileField(upload_to="notesFiles", null=True)
    timestamp = models.DateTimeField(default=now)
    username = models.CharField(max_length=1000, default="")
    video_uploader_img = models.ImageField(
        null=True, blank=True, upload_to="channelPhotos")
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OTP(models.Model):
    otp = models.IntegerField()
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EmailVerificationStatus(models.Model):
    is_email_verified = models.BooleanField(default=False)
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class History(models.Model):
    video_id = models.IntegerField()
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bookmark(models.Model):
    video_id = models.IntegerField()
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LoginStatus(models.Model):
    is_loggedin = models.BooleanField(default=False)
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# USED FOR AVOIDING REDUNDANT LIKES
class LikedBy(models.Model):
    video_id = models.IntegerField()
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# USED FOR AVOIDING REDUNDANT LIKES
class ReportedBy(models.Model):
    video_id = models.IntegerField()
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

# FOR QUICK NOTES
class QuickNotes(models.Model):
    notes_value = models.CharField(max_length=10000000)
    # associated with an user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# CHATTING DATA


class ChatRoom(models.Model):
    sno = models.AutoField(primary_key=True)
    roomName = models.CharField(max_length=1000, default="")
    roomPass = models.CharField(default="", max_length=1000)


class Messages(models.Model):
    sno = models.AutoField(primary_key=True)
    value = models.CharField(max_length=4000, default="")
    timestamp = models.DateTimeField(default=now)
    username = models.CharField(default="", max_length=1000)
    room = models.CharField(default="", max_length=1000)
