# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.interface.interface import Interface
from zope.schema import Text, ASCIILine, Field
from zope.contentprovider.interfaces import IContentProvider

class IFormStatus(IContentProvider):
    errors = Field(title=u'Errors',
        description=u'The errors, if any',
        required=True)

    status = Text(title=u'Status',
        description=u'The status of the form.',
        required=True)

    widgets = Field(title=u'Widgets',
        description=u'The widg',
        required=True)

    pageTemplateFileName = Text(title=u"Page Template File Name",
        description=u'The name of the ZPT file that is used to '\
        u'render the status message.',
        required=False,
        default=u"browser/templates/statusmessage.pt")

