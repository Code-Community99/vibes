from django import template


register = template.Library()


@register.filter("cnt")
def liked(curuid , qidobj):
    controller = False
    for x in qidobj.followingcounter.all():
        print(x)
        if curuid == x.user_follower_id:
            controller = True
            break

    return controller
