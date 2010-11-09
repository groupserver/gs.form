# coding=utf-8
from zope.app.form.browser import TextAreaWidget

def wym_editor_widget(field, request):
    retval = TextAreaWidget(field, request)
    retval.cssClass = 'wymeditor'
    return retval

