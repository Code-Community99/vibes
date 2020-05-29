from signup.models import signup
from django.db.models import Q
from discover.models import Followers as fl
class vibes_friends:
    def __init__(self , userid):
        self.userid = userid
        self.friends_association()
        self.same_location()
        self.same_interest()
        self.sort_users()
        self.friend_of_friend()
    # fetch users and prepare data for use by class

    def friends_association(self):
        self.all_users = signup.objects.filter(Q(followercounter__user_follower = self.userid.uid) | Q(followingcounter__user_follower = self.userid.uid)).exclude(uid=self.userid.uid)
        self.all_users_friends = dict()

        self.all_users_friends["my_friends"] = list()

        for x in self.all_users:
            if x.uid not in self.all_users_friends["my_friends"]:
                self.all_users_friends["my_friends"].append(x.uid)

    def same_location(self):
        users_same_location = signup.objects.filter(location=self.userid.location)
        self.all_users_friends["same_location"] = list()

        for user in users_same_location:
            self.all_users_friends["same_location"].append(user.uid)


    def same_interest(self):
        users_same_interest = signup.objects.filter(location=self.userid.location)
        self.all_users_friends["same_interest"] = list()

        for user in users_same_interest:
            self.all_users_friends["same_interest"].append(user.uid)


    def sort_users(self):
        pass


    def friend_of_friend(self):
        self.all_users_friends["friends_of_my_friends"] = list()
        for user in self.all_users_friends["my_friends"]:
            [print(value.followercounter.all().uid) for value in fl.objects.filter(Q(user_follower_id = user)|Q(user_following_id = user))]

    # destructor
    def __del__(self):
        print("Program terminated ...")
