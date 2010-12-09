# coding=utf-8
'''Radio Widget

The main difference between the standard radio widget and this radio
widget is the ``for`` attribute of the label is set in this radio
widget. This makes the widget easier to use, as it allows the radio
button to be toggled by clicking on the label.

To use this radio widget import ``radio_widget`` and assign it as the
``custom_widget`` for the field::
    formFields['basicPrivacy'].custom_widget = radio_widget
'''
from zope.app.form.browser import RadioWidget
from zope.app.form.browser.widget import renderElement

class NotBrokenRadioWidget(RadioWidget):
    _joinButtonToMessageTemplate = u'<div class="radioItem">%s&nbsp;%s</div>\n'
    def renderItem(self, index, text, value, name, cssClass):
        widgetId = '%s.%s' % (name, index)
        elem = renderElement(u'input',
                             type="radio",
                             cssClass=cssClass,
                             name=name,
                             id=widgetId,
                             value=value)
        label = '<label class="radioLabel" for="%s">%s</label>' % \
          (widgetId, text)
        return self._joinButtonToMessageTemplate % (elem, label)

    def renderSelectedItem(self, index, text, value, name, cssClass):
        """Render a selected item of the list."""
        widgetId = '%s.%s' % (name, index)
        elem = renderElement(u'input',
                             value=value,
                             name=name,
                             id=widgetId,
                             cssClass=cssClass,
                             checked="checked",
                             type='radio')
        label = '<label class="radioLabel" for="%s">%s</label>' % \
          (widgetId, text)
        return self._joinButtonToMessageTemplate % (elem, label)

def radio_widget(field, request):
    return NotBrokenRadioWidget(field,
                                field.vocabulary,
                                request)


