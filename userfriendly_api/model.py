from signup.models import signup as sp
from django.db.models import Q , Count
from discover.models import Followers as fl
from itertools import chain


class vibes_friends:
    def __init__(self , target_user):
        self.userid = target_user
        self.usersSame_location = None
        self.my_friends = set()
        self.friends()

    # fetch users and prepare data for use by class

    def friends(self):
        [self.my_friends.add(value) for value in sp.objects.filter(Q(followercounter__user_following = self.userid.uid) | Q(followingcounter__user_follower = self.userid.uid)).exclude(uid=self.userid.uid)]
        print(self.my_friends)


    def users_same_location_and_interest(self):
        self.usersSame_location = set()
        self.usersSame_interest = set()
        [self.usersSame_location.add(location) for location in sp.objects.all() if (location.location==self.userid.location)]
        [self.usersSame_interest.add(location) for location in sp.objects.all() if (location.hobby==self.userid.hobby)]
        print(self.usersSame_interest , self.usersSame_location)

    def users_sort_noOfFriends(self):
        # print(sp.objects.all().annotate(follows = Count("followercounter__user_follower")).order_by("follows"))
        pass

    def suggest_friends(self):
        pass

    def model_report(self):
        return (1,)


# location prediction
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
