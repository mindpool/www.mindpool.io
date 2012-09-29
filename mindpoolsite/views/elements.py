# -*- coding: utf-8
from datetime import datetime
import os.path

from twisted.python.filepath import FilePath
from twisted.web.template import Element, XMLFile, renderer, tags

from mindpoolsite import const, content, meta, utils
from mindpoolsite.models import collection
from mindpoolsite.controllers import retrieve


class TemplateLoader(Element):
    """
    """
    templateDir = "templates"
    templateFile = ""

    def __init__(self, loader=None, templateFile=None):
        super(TemplateLoader, self).__init__(loader=loader)
        if templateFile:
            self.templateFile = templateFile
        template = FilePath(
            "%s/%s" % (self.templateDir, self.templateFile))
        self.loader = XMLFile(template.path)


class BaseFragment(TemplateLoader):
    """
    """
    @renderer
    def getRootURL(self, request, tag):
        return const.urls["root"]


class HeadFragment(BaseFragment):
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


class BaseTopNavFragment(BaseFragment):
    """
    """
    templateFile = "fragments/topnav.xml"
    navLinks = []

    @renderer
    def navData(self, request, tag):
        """
        """
        tag.fillSlots(
            projectName=meta.displayName,
            userName="Anonymous",
            )
        return tag

    @renderer
    def navLinks(self, request, tag):
        """
        """
        currentPath = request.path
        links = self.navLinks
        elements = []
        for text, url in links:
            cssClass = ""
            if url == currentPath:
                cssClass = "active"
            elements.append(
                tags.li(tags.a(text, href=url), class_=cssClass),
                )
        return tag(elements)


class TopNavFragment(BaseTopNavFragment):
    """
    """
    navLinks = const.topNavLinks


class SplashTopNavFragment(BaseTopNavFragment):
    """
    """
    navLinks = const.splashTopNavLinks


class SplashFragment(BaseFragment):
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


class FooterFragment(BaseFragment):
    """
    """
    templateFile = "fragments/footer.xml"

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
