# coding=utf-8
from zope.component import createObject
try:
    from five.formlib.formbase import PageForm
except ImportError:
    from Products.Five.formlib.formbase import PageForm

class SiteForm(PageForm):
    def __init__(self, context, request):
        PageForm.__init__(self, context, request)
        self.__siteInfo = None

    @property
    def siteInfo(self):
        if self.__siteInfo == None:
            self.__siteInfo = \
                createObject('groupserver.SiteInfo', self.context)
        return self.__siteInfo

