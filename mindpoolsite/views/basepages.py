from twisted.web.iweb import IRenderable
from twisted.web.template import renderer

from zope.interface import implements

from klein.resource import KleinResource

from mindpoolsite import const, utils
from mindpoolsite.views import fragments, loaders


class BasePage(loaders.TemplateLoader):
    """
    """
    templateFile = "base.xml"

    @renderer
    def head(self, request, tag):
        return fragments.HeadFragment()

    @renderer
    def bodyData(self, request, tag):
        bodyClass = ""
        if request.path in const.splashAliases:
            bodyClass = "splash"
        else:
            bodyClass = "content-page"
        return tag.fillSlots(bodyClass=bodyClass)

    @renderer
    def topnav(self, request, tag):
        raise NotImplementedError()

    @renderer
    def contentarea(self, request, tag):
        raise NotImplementedError()

    @renderer
    def sidebar(self, request, tag):
        return tag

    @renderer
    def jsloader(self, request, tag):
        return loaders.TemplateLoader(templateFile="fragments/jsloader.xml")

    @renderer
    def footer(self, request, tag):
        return fragments.FooterFragment()


class BaseResourcePage(KleinResource):
    """
    """
    def __init__(self, app, portal):
        KleinResource.__init__(self, app)
        self.portal = portal

    def handleError(self, failure):
        print "Whoops ..."
        print failure
        print dir(failure)
        print vars(failure)


class ReSTContent(object):
    """
    """
    implements(IRenderable)

    def __init__(self, rstData):
        self.rstData = rstData

    def render(self, request):
        return utils.rstToStan(self.rstData)


class ContentPage(BasePage):
    """
    """
    contentType = const.contentTypes["rst"]
    contentData = ""
    contentDataTemplate = ""
    _cachedContent = ""

    def getContentData(self, request):
        pass

    def getContentDataTemplate(self, request):
        pass

    def getContent(self, request, templateData=""):
        if self.contentData:
            content = self.contentData
        elif self.contentDataTemplate:
            content = self.contentDataTemplate
            if templateData:
                content = content % templateData
        else:
            content = self.getContentData(request)
            if not content:
                content = self.getContentDataTemplate(request)
                if content and templateData:
                    content = content % templateData
        return content

    def renderContentData(self, request):
        if not self._cachedContent:
            if self.contentType == const.contentTypes["rst"]:
                self._cachedContent = ReSTContent(self.getContent(request))
            elif self.contentType == const.contentTypes["html"]:
                self._cachedContent = self.getContent(request)
        return self._cachedContent

    @renderer
    def topnav(self, request, tag):
        return fragments.TopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(self.renderContentData(request))


class SidebarPage(ContentPage):
    """
    """
    sidebarHeading = ""
    sidebarLinks = []
    contentData = ""

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(
            self.renderContentData(request), self.sidebarLinks)
