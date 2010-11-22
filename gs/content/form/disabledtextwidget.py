# coding=utf-8
from zope.app.form.browser import TextWidget

def disabled_text_widget(field, request):
    retval = TextWidget(field, request)
    retval.cssClass = "disabled"
    return retval
