# coding=utf-8
from zope.app.form.browser import SelectWidget

def select_widget(field, request):
    retval = SelectWidget(field, field.vocabulary, request)
    retval.size = 15 # Because there are a lot of items.
    return retval

