from twisted.web.template import renderer

from mindpoolsite import const, content, meta, utils
from mindpoolsite.views import fragments, loaders


class BasePage(loaders.TemplateLoader):
    """
    """
    templateFile = "base.xml"

    @renderer
    def head(self, request, tag):
        return fragments.HeadFragment()

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
        return tag


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
