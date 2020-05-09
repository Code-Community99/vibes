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
