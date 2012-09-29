# -*- coding: utf-8
from datetime import datetime

from twisted.web.template import renderer

from mindpoolsite import meta
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
        return elements.TopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        raise NotImplementedError()

    @renderer
    def sidebar(self, request, tag):
        return tag

    @renderer
    def content(self, request, tag):
        return tag

    @renderer
    def copyright(self, request, tag):
        year = meta.startingYear
        thisYear = datetime.now().year
        if thisYear > year:
            year = "%s - %s" % (year, thisYear)
        return tag("© %s %s" % (year, meta.author))

    @renderer
    def jsloader(self, request, tag):
        return elements.TemplateLoader(templateFile="fragments/jsloader.xml")

    @renderer
    def footer(self, request, tag):
        return elements.FooterFragment()


class SplashPage(BasePage):
    """
    """
    @renderer
    def contentarea(self, request, tag):
        return elements.SplashFragment()


class ServicesPage(BasePage):
    """
    """


class SidebarPage(BasePage):
    """
    """
    @renderer
    def sidebar(self, request, tag):
        return elements.TemplateLoader(templateFile="content/sidebar.xml")


class AboutPage(SidebarPage):
    """
    """
    @renderer
    def content(self, request, tag):
        return elements.TemplateLoader(templateFile="content/about.xml")


class ContactPage(SidebarPage):
    """
    """
    @renderer
    def content(self, request, tag):
        return elements.TemplateLoader(templateFile="content/contact.xml")
