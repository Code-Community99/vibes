from django import template


register = template.Library()
@register.filter("control")
def group_controller(obj , user):

    for x in obj:
        if x.group_member.username == user:

            control = True
            break

        else:
            control = False
    return control

@register.filter("group_get_latest")
def group_get_latest(groupboj):
    try:
        groupinfo = groupboj.post_group_own.latest("post_time").post_content
    except Exception as e:
        return "No Topics yet"
    else:
        return groupinfo
