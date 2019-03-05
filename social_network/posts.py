from datetime import datetime


class Post():
    user = None
    def __init__(self, text, timestamp=None):
         pass

    def set_user(self, user):
         self.user=user

class TextPost(Post):
    
    #define class instance. Set user to default to none until one is assigned
    def __init__(self, text, timestamp=None):
         self.text = text
         self.timestamp = timestamp
         self.date_for_sorting = datetime.now()
         self.date_str = self.date_for_sorting.strftime("%a, %b %d, %Y")
    def __str__(self):
         return '{fname} {lname}: "{text}"\n\t{date}'.format(fname=self.user.first_name,lname=self.user.last_name,text=self.text,date=self.date_str)

    
class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
         self.text = text
         self.image_url = image_url
         self.timestamp = timestamp
         self.date_for_sorting = datetime.now()
         self.date_str = self.date_for_sorting.strftime("%a, %b %d, %Y")
        
    
    def __str__(self):
         return '{fname} {lname}: "{text}"\n\tPic URL: {image_url}\n\t{date}'.format(fname=self.user.first_name,lname=self.user.last_name,text=self.text,image_url=self.image_url,date=self.date_str)

    
class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
         self.text = text
         self.latitude = latitude
         self.longitude = longitude
         self.timestamp = timestamp
         self.date_for_sorting = datetime.now()
         self.date_str = self.date_for_sorting.strftime("%a, %b %d, %Y")
    def __str__(self):
         return '{fname} checked in: "{text}"\n\t{latitude} {longitude}\n\t{date}'.format(fname=self.user.first_name,latitude=self.latitude,longitude=self.longitude,text=self.text,date=self.date_str)
    

class User():
    def __init__(self,first_name="John", last_name="Smith", email="johnsmith@rmotr.com"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.posts=[]
        self.following=[]
        self.timeline=[]
    
    def add_post(self,post):
        post.user = self
        self.posts.append(post)
    
    def follow(self,user):
        self.following.append(user)
        
    def get_timeline(self):
        timeline = []
        for each_user in self.following:
            for each_post in each_user.posts:
                timeline.append(each_post)
        timeline.sort(key=lambda post: post.date)
        return timeline
        
