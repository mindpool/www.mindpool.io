from twisted.web.template import renderer

from mindpoolsite import const, content, meta
from mindpoolsite.views import base, fragments


class SplashPage(base.BasePage):
    """
    """
    @renderer
    def topnav(self, request, tag):
        return fragments.SplashTopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return fragments.SplashFragment()


class CloudTechPage(base.ContentPage):
    """
    """
    htmlContent = ""


class OpenSourcePage(base.ContentPage):
    """
    """
    htmlContent = ""


class ServicesPage(base.SidebarPage):
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


class PeoplePage(base.SidebarPage):
    """
    """
    sidebarLinks = const.peopleLinks
    htmlContent = content.people.people


class TeamsPage(PeoplePage):
    """
    """
    htmlContent = content.people.teams


class MembersPage(PeoplePage):
    """
    """
    htmlContent = content.people.members


class AboutPage(base.SidebarPage):
    """
    """


class WhoPage(AboutPage):
    """
    """


class WhatPage(AboutPage):
    """
    """


class CulturePage(AboutPage):
    """
    """


class ContactPage(AboutPage):
    """
    """
