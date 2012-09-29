from twisted.web.template import renderer

from mindpoolsite import const, content, meta
from mindpoolsite.views import elements


class BasePage(elements.TemplateLoader):
    """
    """
    templateFile = "base.xml"

    @renderer
    def head(self, request, tag):
        return elements.HeadFragment()

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
        return elements.TemplateLoader(templateFile="fragments/jsloader.xml")

    @renderer
    def footer(self, request, tag):
        return elements.FooterFragment()


class ContentPage(BasePage):
    """
    """
    htmlContent = ""

    @renderer
    def topnav(self, request, tag):
        return elements.TopNavFragment()

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
        return elements.ContentFragment(
            self.htmlContent, self.sidebarLinks)
