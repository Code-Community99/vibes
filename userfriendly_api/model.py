from signup.models import signup
from django.db.models import Q
from discover.models import Followers as fl

class vibes_friends:
    def __init__(self , userid):
        self.userid = userid
        self.friends_association()
        self.same_location()
        self.same_interest()
        self.friend_of_friend()
    # fetch users and prepare data for use by class

    def friends_association(self):
        self.all_users = signup.objects.filter(Q(followercounter__user_follower = self.userid.uid) | Q(followingcounter__user_follower = self.userid.uid)).exclude(uid=self.userid.uid)
        self.all_users_friends = dict()

        self.all_users_friends["my_friends"] = set()

        for x in self.all_users:
            if x.uid not in self.all_users_friends["my_friends"]:
                self.all_users_friends["my_friends"].add(x.uid)

    def same_location(self):
        users_same_location = signup.objects.filter(location=self.userid.location)
        self.all_users_friends["same_location"] = set()

        for user in users_same_location:
            if user.uid not in self.all_users_friends["my_friends"] and user.uid != self.userid.uid:
                self.all_users_friends["same_location"].add(user.uid)


    def same_interest(self):
        users_same_interest = signup.objects.filter(hobby=self.userid.hobby)
        self.all_users_friends["same_interest"] = set()

        for user in users_same_interest:
            if user.uid not in self.all_users_friends["my_friends"] and user.uid not in self.all_users_friends["same_location"] and user.uid != self.userid.uid:
                self.all_users_friends["same_interest"].add(user.uid)


    def sort_users(self , all_users_id):
        outer_index = 0
        inner_index = 0
        all_users_id = list(all_users_id)

        for user in all_users_id:
            for test in all_users_id:
                u1 = signup.objects.get(uid = user)
                u2 = signup.objects.get(uid = test)
                print(u1.uid , u2.uid)
                if (u1.followercounter.all().count() + u1.followingcounter.all().count()) > (u2.followercounter.all().count() + u2.followingcounter.all().count()):
                    tmp = u2.uid
                    all_users_id[inner_index] = u1.uid
                    all_users_id[outer_index] = tmp

                inner_index+=1

            outer_index+=1
            inner_index = 0
        return sorted(all_users_id)


    def friend_of_friend(self):
        self.all_users_friends["friends_of_my_friends"] = set()

        for user in self.all_users_friends["my_friends"]:
            [self.all_users_friends["friends_of_my_friends"].add(value.uid) for value in signup.objects.filter(Q(followercounter__user_follower = user) | Q(followingcounter__user_follower = user)).exclude(uid=user) if value not in self.all_users_friends["my_friends"]]


    def arrange_data(self):
        all_users_id = set()
        for user in self.all_users_friends.items():
            [all_users_id.add(info) for info in user[1]]

        all_users_id = self.sort_users(all_users_id)
        return all_users_id


    def model_report(self):
        return self.arrange_data()


    # destructor
    def __del__(self):
        pass
