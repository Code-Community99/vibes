from django import template


register = template.Library()


@register.filter("cnt")
def liked(curuid , qidobj):
    controller = False

    # look for the match
    print(curuid)
    print("\n\n")

    for x in qidobj.followingcounter.all():
        # Test if the current user has followed this user
        print(x.user_follower_id)
        if curuid == x.user_follower_id:
            controller = True
            break

    return controller
