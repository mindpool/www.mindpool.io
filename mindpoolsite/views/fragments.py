# -*- coding: utf-8
from datetime import datetime
import os.path

from twisted.python.filepath import FilePath
from twisted.web.template import Element, XMLFile, renderer, tags

from mindpoolsite import const, content, meta, utils
from mindpoolsite.models import collection
from mindpoolsite.controllers import retrieve
from mindpoolsite.views import basefragments as base


class HeadFragment(base.BaseFragment):
    """
    """
    templateFile = "fragments/head.xml"

    @renderer
    def title(self, request, tag):
        title = "mindpool"
        parts = [x for x in request.path.split("/") if x]
        if len(parts) > 1:
            title = title + ".".join(parts)
        elif len(parts) == 1:
            title = "%s.%s" % (title, parts[0])
        return tag(title)


class TopNavFragment(base.BaseTopNavFragment):
    """
    """
    templateFile = "fragments/topnav.xml"
    navLinks = const.topNavLinks


class SplashTopNavFragment(base.BaseTopNavFragment):
    """
    """
    templateFile = "fragments/splashtopnav.xml"
    navLinks = const.splashTopNavLinks


class SplashFragment(base.BaseFragment):
    """
    """
    templateFile = "fragments/splash.xml"

    @renderer
    def data(self, request, tag):
        tag.fillSlots(
            tagline=const.tagline,
            consulting=content.splash.consulting,
            training=content.splash.training,
            teams=content.splash.teams,
            consultingURL=const.urls["consulting"],
            trainingURL=const.urls["training"],
            teamsURL=const.urls["teams"]
            )
        return tag

    @renderer
    def footer(self, request, tag):
        return FooterFragment()


class ContentFragment(base.BaseFragment):
    """
    """
    templateFile = "fragments/content.xml"

    def __init__(self, htmlContent, sidebarLinks=None, sidebarHeading="",
                 *args, **kwargs):
        super(ContentFragment, self).__init__(*args, **kwargs)
        self.htmlContent = htmlContent
        self.sidebarLinks = sidebarLinks or []
        self.sidebarHeading = sidebarHeading or ""

    @renderer
    def data(self, request, tag):
        sidebar = ""
        if self.sidebarLinks or self.sidebarHeading:
            sidebar = SidebarFragment(self.sidebarHeading, self.sidebarLinks),
        tag.fillSlots(
            sidebar=sidebar,
            content=self.htmlContent,
            footer=FooterFragment())
        return tag


class SidebarFragment(ContentFragment):
    """
    """
    templateFile = "fragments/sidebar.xml"

    @renderer
    def data(self, request, tag):
        tag.fillSlots(
            heading=self.sidebarHeading,
            links=self.getLinks(request))
        return tag

    def getLinks(self, request):
        elements = []
        for text, url, type in self.sidebarLinks:
            if type == const.DIVIDER:
                continue
            if type == const.HEADER:
                elements.append(
                    tags.li(text, class_="nav-header"))
                continue
            cssClass = ""
            if self.isInSubSection(request, url):
                cssClass = "active"
            elements.append(
                tags.li(tags.a(text, href=url), class_=cssClass))
        return elements


class FooterFragment(base.BaseFragment):
    """
    """
    templateFile = "fragments/footer.xml"

    # XXX - add __init__ here that takes isSplash as a parameter, and adjust
    # the CSS for the footer accordingly

    @renderer
    def data(self, request, tag):
        tag.fillSlots(
            cities=self.getCities(),
            copyright=self.getCopyright(),
            )
        return tag

    def getCities(self):
        elements = []
        for index, city in enumerate(sorted(const.officeCities)):
            if index >= 1:
                elements.append("·")
            elements.append(tags.span(city, class_="city"))
        return elements

    def getCopyright(self):
        year = meta.startingYear
        thisYear = datetime.now().year
        mailTo = "mailto:%s" % const.salesEmail
        if thisYear > year:
            year = "%s - %s" % (year, thisYear)
        return ("© %s " % year, tags.a(meta.author, href=mailTo))
