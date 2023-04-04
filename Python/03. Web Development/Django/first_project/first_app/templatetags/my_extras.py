from django import template

# Creating a custom built template filter

register = template.Library()

@register.filter(anem="cut")
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string.
    """

    return value.replace(arg,"")

# When not using decorators
# register.filter("cut", cut)