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


class SplashPage(BasePage):
    """
    """
    @renderer
    def topnav(self, request, tag):
        return elements.SplashTopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return elements.SplashFragment()


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


class CloudTechPage(ContentPage):
    """
    """
    htmlContent = ""


class OpenSourcePage(ContentPage):
    """
    """
    htmlContent = ""


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


class ServicesPage(SidebarPage):
    """
    """
    sidebarLinks = const.servicesLinks
    htmlContent = content.services.services


class ConsultingPage(ServicesPage):
    """
    """
    htmlContent = content.services.consulting


class TrainingPage(ServicesPage):
    """
    """
    htmlContent = content.services.training


class PeoplePage(SidebarPage):
    """
    """


class TeamsPage(SidebarPage):
    """
    """


class MembersPage(SidebarPage):
    """
    """


class AboutPage(SidebarPage):
    """
    """
    @renderer
    def contentarea(self, request, tag):
        return elements.TemplateLoader(templateFile="content/about.xml")


class WhoPage(SidebarPage):
    """
    """


class WhatPage(SidebarPage):
    """
    """


class CulturePage(SidebarPage):
    """
    """


class ContactPage(SidebarPage):
    """
    """
    @renderer
    def contentarea(self, request, tag):
        return elements.TemplateLoader(templateFile="content/contact.xml")
