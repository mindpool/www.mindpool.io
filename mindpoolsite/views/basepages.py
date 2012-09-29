from twisted.web.template import renderer

from mindpoolsite import const
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


class ContentPage(BasePage):
    """
    """
    htmlContent = ""

    @renderer
    def topnav(self, request, tag):
        return fragments.TopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(self.htmlContent)


class SidebarPage(ContentPage):
    """
    """
    sidebarHeading = ""
    sidebarLinks = []
    htmlContent = ""

    @renderer
    def contentarea(self, request, tag):
        return fragments.ContentFragment(
            self.htmlContent, self.sidebarLinks)
