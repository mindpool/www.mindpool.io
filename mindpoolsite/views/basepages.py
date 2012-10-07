from twisted.web.iweb import IRenderable
from twisted.web.template import renderer

from zope.interface import implements

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
    _cachedContent = ""

    def renderContentData(self):
        if not self._cachedContent:
            if self.contentType == const.contentTypes["rst"]:
                self._cachedContent = ReSTContent(self.contentData)
            elif self.contentType == const.contentTypes["html"]:
                self._cachedContent = self.contentData
        return self._cachedContent

    @renderer
    def topnav(self, request, tag):
        return fragments.TopNavFragment(request=request)

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(self.renderContentData())


class SidebarPage(ContentPage):
    """
    """
    sidebarHeading = ""
    sidebarLinks = []
    contentData = ""

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(
            self.renderContentData(), self.sidebarLinks)
