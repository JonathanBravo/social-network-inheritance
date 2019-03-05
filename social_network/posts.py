from datetime import datetime


class Post():
    def __init__(self, text, timestamp=None):
        self.user = None

    def set_user(self, user):
        self.user=user

class TextPost(Post):
    
    #define class instance. Set user to default to none until one is assigned
    def __init__(self, text, timestamp=None):
        self.text = text
        if timestamp!=None:
            self.date_for_sorting = timestamp
        else:
            self.date_for_sorting = datetime.now()
        self.date_str = self.date_for_sorting.strftime("%A, %b %d, %Y")
        self.user = None
    def __str__(self):
        user = self.user
        print(user)
        return '@{fname} {lname}: "{text}"\n\t{date}'.format(fname=user.first_name,lname=user.last_name,text=self.text,date=self.date_str)

    
class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        if timestamp!=None:
            self.date_for_sorting = timestamp
        else:
            self.date_for_sorting = datetime.now()
        self.date_str = self.date_for_sorting.strftime("%A, %b %d, %Y")
        self.user = None
    
    def __str__(self):
        user = self.user
        return '@{fname} {lname}: "{text}"\n\t{image_url}\n\t{date}'.format(fname=user.first_name,lname=user.last_name,text=self.text,image_url=self.image_url,date=self.date_str)

    
class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        if timestamp!=None:
            self.date_for_sorting = timestamp
        else:
            self.date_for_sorting = datetime.now()
        self.date_str = self.date_for_sorting.strftime("%A, %b %d, %Y")
        self.user = None
        
    def __str__(self):
        user = self.user
        return '@{fname} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{date}'.format(fname=user.first_name,latitude=self.latitude,longitude=self.longitude,text=self.text,date=self.date_str)
    
