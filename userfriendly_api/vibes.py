import sqlite3 as sql


class vibes_friends:
    def __init__(self):
        self.db = sql.connect("platform.db")
        self.dbcur = self.db.cursor()

    def db_manager(self):
        pass

    def friends_association(self):
        self.all_users_friends = dict()
        sqlquery = """
            SELECT * from users
        """
        self.all_users = [value for value in self.dbcur.execute(sqlquery).fetchall()]
        for user in self.all_users:
            self.all_users_friends[user[0]] = dict({"userinfo":user[1:] , "friends":list() ,"no_of_friends":int() , "suggest_friends":list()})

        sqlquery ="""
        SELECT muid , suid FROM friends WHERE muid=? OR suid=?
        """
        for user in self.all_users_friends.items():
            all_user_friends_association = [value[0] if (int(user[0])==value[1]) else value[1] for value in self.dbcur.execute(sqlquery , (int(user[0]),int(user[0]))).fetchall()]

            # append all friends to the list
            [user[1]["friends"].append(value) for value in all_user_friends_association]

            # save the number of friends
            user[1]["no_of_friends"] = len(all_user_friends_association)
        self.all_users_friends = dict(self.all_users_friends)
        return self.all_users_friends

    # organize data
    def data_clean(self , dataobject , dataindex):
        users_same_location = dict()
        for x in dataobject:
            users_same_location[x] = list()

        for x in self.all_users_friends.items():
            if x[1]["userinfo"][dataindex] in dataobject:
                users_same_location[x[1]["userinfo"][dataindex]].append(x[0])

        return users_same_location

    def location_user_association(self):
        self.friends_association()
        locations = list()
        for x in self.all_users_friends.items():
            locations.append(x[1]["userinfo"][2])

        locations = self.data_clean(set(locations) , 2)
        return locations

    def interests_user_association(self):
        self.friends_association()
        interests = list()
        for x in self.all_users_friends.items():
            interests.append(x[1]["userinfo"][1])

        interests = self.data_clean(set(interests) , 1)
        return interests


    def sort_algorithm(self):
        self.friends_association()
        sorted_users = list(self.friends_association().items())
        for x in range(len(sorted_users)):
            for y in range(len(sorted_users)):
                if sorted_users[x][1]["no_of_friends"] > sorted_users[y][1]["no_of_friends"]:
                    tmp = sorted_users[y]
                    sorted_users[y] = sorted_users[x]
                    sorted_users[x] = tmp

        return sorted_users

    def filter_suggestions(self , users_friends , currentid):
        target_friends = list()
        for x in self.friends_association().items():
            if (x[0] in users_friends) and (x[0] not in target_friends):
                if currentid[0] in x[1]["friends"]:
                    del x[1]["friends"][x[1]["friends"].index(currentid[0])]
                    target_friends.append(x[1]["friends"])

        for x in target_friends:
            ([currentid[1]["suggest_friends"].append(value) for value in x])

        for x in self.friends_association().items():
            if x[1]["userinfo"][2] == currentid[1]["userinfo"][2]:
                currentid[1]["suggest_friends"].append(x[0])

        for x in self.friends_association().items():
            if x[1]["userinfo"][1] == currentid[1]["userinfo"][1]:
                currentid[1]["suggest_friends"].append(x[0])


        return currentid

    def suggest_user(self):
        self.friends_association()
        for x in self.friends_association().items():
            # print(x)
            print(self.filter_suggestions(x[1]["friends"] , x))


    def modify_user_location(self):
        sqlquery ="""
        SELECT * FROM users WHERE location IS NULL
        """
        print(self.dbcur.execute(sqlquery).fetchall())


    # destructor
    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    model = vibes_friends()
    model.modify_user_location()
    while True:
        try:
            print("\n\nchoose one of the options below ... \n1. Display users and there friends\n2. Display users sharing the same location\n3. Display users sharing the same interests\n4. Sorted users\n5. Suggested users\n0. Exit")
            option = int(input("Your choice: "))
        except Exception as e:
            print("\n\nInvalid information provided, try again.")
            print("choose one of the options below ... \n1. Display users and there friends\n2. Display users sharing the same location\n3. Display users sharing the same interests\n4. Sorted users\n5. Suggested users\n0. Exit")
            option = int(input("Your choice: "))
        else:
            if option==1:
                for x in model.friends_association().items():
                    print(x)

            elif option==2:
                for x in model.location_user_association().items():
                    print("users from {} {}".format(x[0] , x[1]))

            elif option==3:
                for x in model.interests_user_association().items():
                    print("users interested in {} {}".format(x[0] , x[1]))

            elif option==4:
                for x in model.sort_algorithm():
                    print(x)

            elif option==5:
                model.suggest_user()
            elif option==0:
                break
            else:
                print("\n\nInvalid information provided, try again.")
