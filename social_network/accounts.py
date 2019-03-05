class User():
    def __init__(self,first_name, last_name, email):
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
        timeline.sort(key=lambda post: post.date_for_sorting)
        return timeline
