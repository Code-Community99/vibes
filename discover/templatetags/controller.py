from django import template


register = template.Library()


@register.filter("cnt")
def liked(test_follow , my_info):
    controller = False
    for x in test_follow.followingcounter.all():
        if my_info.uid == x.user_follower_id:
            controller = True
            break

    return controller
