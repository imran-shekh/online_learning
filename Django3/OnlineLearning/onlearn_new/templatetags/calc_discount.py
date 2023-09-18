from django import template

register = template.Library()


register = template.Library()

@register.simple_tag

def discounted_price(price, discount):
    if discount is 0 or discount is None:
        return price
    
    sp = price
    sp = sp - (sp * discount *0.01)
    return int(sp)