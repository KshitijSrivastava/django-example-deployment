from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all the value of arg from the string

    """
    return value.replace(arg,'')

register.filter('cuts',cut)
