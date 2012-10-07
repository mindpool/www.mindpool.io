from twisted.web.template import renderer, tags

from mindpoolsite import const
from mindpoolsite.views import loaders


class BaseFragment(loaders.TemplateLoader):
    """
    """
    @renderer
    def getRootURL(self, request, tag):
        return const.urls["root"]

    def _isInSection(self, request, sectionURL, start=1, end=2):
        current = request.path.split("/")[start:end]
        section = sectionURL.split("/")[start:end]
        if current == section:
            return True
        return False

    def isInSection(self, request, sectionURL):
        return self._isInSection(request, sectionURL)

    def isInSubSection(self, request, sectionURL):
        return self._isInSection(request, sectionURL, end=3)


class AuthFragment(BaseFragment):
    """
    """
    templateFile = "fragments/auth.xml"

    # XXX needs logic for:
    #   * is the user logged in? (check session)
    #   * if so, get their user name, display it, and provide a signout link
    #   * if not, present the Persona login link

    @renderer
    def data(self, request, tag):
        print request
        print self.request
        return tag


class BaseTopNavFragment(BaseFragment):
    """
    """
    navLinks = []

    @renderer
    def data(self, request, tag):
        tag.fillSlots(
            links=self.getLinks(request),
            auth=AuthFragment(request=request)
        )
        return tag

    def getLinks(self, request):
        elements = []
        for text, url, type in self.navLinks:
            cssClass = ""
            if self.isInSection(request, url):
                cssClass = "active"
            if type == const.DROPDOWN:
                cssClass += " dropdown"
                element = self.getDropdown(text, url, cssClass)
            else:
                element = tags.li(tags.a(text, href=url), class_=cssClass)
            elements.append(element)
        return elements

    def getDropdown(self, title, url, cssClass):
        elements = []
        if title == "About":
            links = const.aboutDropDown
        for text, url, type in links:
            if type == const.DIVIDER:
                element = tags.li(class_="divider")
            elif type == const.HEADER:
                element = tags.li(text, class_="nav-header")
            else:
                element = tags.li(tags.a(text, href=url))
            elements.append(element)
        return tags.li(
            tags.a(
                title, tags.b(class_="caret"),
                href="#", class_="dropdown-toggle",
                **{"data-toggle": "dropdown"}),
            tags.ul(elements, class_="dropdown-menu"),
            class_=cssClass)
