# creating your own filter

from django import template

register = template.Library()

def sli(value, arg):
    """
    This slices a string
    """
    return value.replace(arg, '')
 

register.filter('sli', sli)
