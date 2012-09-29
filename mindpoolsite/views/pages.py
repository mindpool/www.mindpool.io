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
        raise NotImplementedError()

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
    @renderer
    def topnav(self, request, tag):
        return elements.TopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return tag


class ServicesPage(ContentPage):
    """
    """


class ConsultingPage(ContentPage):
    """
    """


class TrainingPage(ContentPage):
    """
    """


class PeoplePage(ContentPage):
    """
    """


class TeamsPage(ContentPage):
    """
    """


class MembersPage(ContentPage):
    """
    """


class CloudTechPage(ContentPage):
    """
    """


class OpenSourcePage(ContentPage):
    """
    """


class SidebarPage(ContentPage):
    """
    """
    @renderer
    def sidebar(self, request, tag):
        return elements.TemplateLoader(templateFile="content/sidebar.xml")


class AboutPage(ContentPage):
    """
    """
    @renderer
    def content(self, request, tag):
        return elements.TemplateLoader(templateFile="content/about.xml")


class WhoPage(ContentPage):
    """
    """


class WhatPage(ContentPage):
    """
    """


class CulturePage(ContentPage):
    """
    """


class ContactPage(ContentPage):
    """
    """
    @renderer
    def content(self, request, tag):
        return elements.TemplateLoader(templateFile="content/contact.xml")
