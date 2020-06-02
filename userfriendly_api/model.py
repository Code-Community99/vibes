from signup.models import signup as sp
from django.db.models import Q
from discover.models import Followers as fl
from itertools import chain


class vibes_friends:
    def __init__(self , userid):
        self.userid = userid
        self.friends_association()
        self.same_location()
        self.same_interest()
        self.friend_of_friend()
    # fetch users and prepare data for use by class

    def friends_association(self):
        self.all_users = sp.objects.filter(Q(followercounter__user_follower = self.userid.uid) | Q(followingcounter__user_follower = self.userid.uid)).exclude(uid=self.userid.uid)
        self.all_users_friends = dict()

        self.all_users_friends["my_friends"] = set()

        for x in self.all_users:
            if x.uid not in self.all_users_friends["my_friends"]:
                self.all_users_friends["my_friends"].add(x.uid)

    def same_location(self):
        users_same_location = sp.objects.filter(location=self.userid.location)
        self.all_users_friends["same_location"] = set()

        for user in users_same_location:
            if user.uid not in self.all_users_friends["my_friends"] and user.uid != self.userid.uid:
                self.all_users_friends["same_location"].add(user.uid)


    def same_interest(self):
        users_same_interest = sp.objects.filter(hobby=self.userid.hobby)
        self.all_users_friends["same_interest"] = set()

        for user in users_same_interest:
            if user.uid not in self.all_users_friends["my_friends"] and user.uid not in self.all_users_friends["same_location"] and user.uid != self.userid.uid:
                self.all_users_friends["same_interest"].add(user.uid)

    def sort_users(self , all_users_id):
        outer_index = 0
        inner_index = 0
        all_users_id = list(all_users_id)
        # print(all_users_id)
        for user in all_users_id:
            u1 = sp.objects.get(uid = user)
            for test in all_users_id:
                u2 = sp.objects.get(uid = test)
                # print(u1.uid , u2.uid)
                if (u2.followercounter.all().count() + u2.followingcounter.all().count())>(u1.followercounter.all().count() + u1.followingcounter.all().count()):
                    all_users_id[inner_index] = u1.uid
                    all_users_id[outer_index] = u2.uid
                    # print(all_users_id)
                inner_index+=1

            inner_index = 0
            outer_index+=1
        data = sp.objects.get(uid = all_users_id[0])
        for value in range(1,len(all_users_id)):
            data = chain(data , sp.objects.get(uid = all_users_id[value]))
        return all_users_id


    def friend_of_friend(self):
        self.all_users_friends["friends_of_my_friends"] = set()

        for user in self.all_users_friends["my_friends"]:
            [self.all_users_friends["friends_of_my_friends"].add(value.uid) for value in sp.objects.filter(Q(followercounter__user_follower = user) | Q(followingcounter__user_follower = user)).exclude(uid=user) if value not in self.all_users_friends["my_friends"]]


    def arrange_data(self):
        all_users_id = set()
        for user in self.all_users_friends.items():
            [all_users_id.add(info) for info in user[1]]

        all_users_id = self.sort_users(all_users_id)
        return all_users_id


    def model_report(self):
        return set(self.arrange_data())


    # destructor
    def __del__(self):
        pass


class predict_user_location:
    def __init__(self , target_user):
        print("Testing location module")
        self.target_user = target_user
        self.my_friends = sp.objects.filter(Q(followercounter__user_follower = self.target_user.uid) | Q(followingcounter__user_follower = self.target_user.uid)).exclude(uid=self.target_user.uid)
        self.target_user_hobby = self.target_user.hobby
        self.collect_friends_information()
        self.predict_user_loc()

    def collect_friends_information(self):
        friends_same_hobby = self.my_friends.filter(hobby = self.target_user.hobby)
        self.possibility1 = self.search_location_from_friend()
        self.possibility2 = self.search_hobby_from_friend(friends_same_hobby)


    def search_hobby_from_friend(self , friends_same_hobby):
        tmp_loc = set([value.location for value in friends_same_hobby])
        possible_locations = dict()
        for x in tmp_loc:
            possible_locations[x]=0

        for x in friends_same_hobby:
            possible_locations[x.location]+=1

        return possible_locations


    def search_location_from_friend(self):
        possible_locations = dict()
        tmp_loc = set([value.location for value in self.my_friends])

        for x in tmp_loc:
            possible_locations[x] = 0
        for x in self.my_friends:
            possible_locations[x.location]+=1

        return possible_locations


    def predict_user_loc(self):
        print(self.possibility1  , self.possibility2)
        if len(self.possibility1)>1:
            largest_group_of_peers = ("Unkown" , 0)

            for x in self.possibility2.items():
                if x[1]>largest_group_of_peers[1]:
                    largest_group_of_peers = x

            self.target_user.location = largest_group_of_peers[0]
            self.target_user.save()
        elif len(self.possibility1)==1:
            self.target_user.location = list(self.possibility1)[0]
            self.target_user.save()
