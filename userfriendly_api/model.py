from signup.models import signup as sp
from django.db.models import Q , Count , F
from discover.models import Followers as fl
from itertools import chain

# define the class
class vibes_friends:
    def __init__(self , target_user):
        self.userid = target_user
        self.my_friends = set()
        self.my_new_friends = set()
        self.usersSame_location = set()
        self.usersSame_interest = set()
        self.friends()
        self.friends_of_my_friends()
        self.users_same_location_and_interest()
        self.suggest_friends()
        self.users_sort_noOfFriends()

    # fetch users and prepare data for use by class
    def friends(self):
        all_friends = sp.objects.filter(Q(followercounter__user_following = self.userid.uid) | Q(followingcounter__user_follower = self.userid.uid)).exclude(uid = self.userid.uid)
        [self.my_friends.add(value.uid) for value in all_friends if (value.uid not in self.my_friends)]

    def friends_of_my_friends(self):
        friends_list = set()
        for one_friend in self.my_friends:
            friends_list.add(sp.objects.filter(Q(followercounter__user_following = one_friend) | Q(followingcounter__user_follower = one_friend)).exclude(uid = one_friend))
        # adjust above
        try:
            friends_list = list(friends_list)[0]
        except IndexError as e:
            pass
        else:
            for one_friend in friends_list:
                if one_friend.uid not in self.my_friends and one_friend.uid != self.userid.uid:
                    self.my_new_friends.add(one_friend.uid)

    def users_same_location_and_interest(self):
        [self.usersSame_location.add(location.uid) for location in sp.objects.all() if (location.location==self.userid.location)]
        [self.usersSame_interest.add(interests.uid) for interests in sp.objects.all() if (interests.hobby==self.userid.hobby)]
        # print(self.usersSame_interest , self.usersSame_location)

    def users_sort_noOfFriends(self):
        # print(self.my_new_friends.order_by("djn"))
        pass

    def suggest_friends(self):
        for one_friend in self.usersSame_interest:
            if one_friend not in self.my_friends and one_friend != self.userid.uid:
                if one_friend not in [value for value in self.my_new_friends]:
                    self.my_new_friends.add(one_friend)

        for one_friend in self.usersSame_location:
            if one_friend not in self.my_friends and one_friend != self.userid.uid:
                if one_friend not in [value for value in self.my_new_friends]:
                    self.my_new_friends.add(one_friend)

        # sort the results
        self.my_new_friends = sp.objects.filter(uid__in = self.my_new_friends).annotate(totalchaining = Count("followercounter__user_follower") + Count("followingcounter__user_follower")).order_by("-totalchaining")
    def model_report(self):
        return (self.my_new_friends)


# location prediction
class predict_user_location:
    def __init__(self , target_user):
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
        # print(self.possibility1  , self.possibility2)
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
