from django import template

register = template.Library()


@register.filter(name="add_css")
def add_css(field, css):
    """
    Adds a css class to a field.

    :param field:   "self": the field the addcss is attached to
    :type field:    self
    :param css:     The css command
    :type css:      str
    :return:        The field with css attached
    """
    return field.as_widget(
        attrs={"class": field.field.widget.attrs.get("class") or css}
    )
