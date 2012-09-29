from twisted.web.template import renderer

from mindpoolsite import const, content, meta
from mindpoolsite.views import basepages as base, fragments


class SplashPage(base.BasePage):
    """
    """
    @renderer
    def topnav(self, request, tag):
        return fragments.SplashTopNavFragment()

    @renderer
    def contentarea(self, request, tag):
        return fragments.SplashFragment()


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


class CloudTechPage(base.ContentPage):
    """
    """
    htmlContent = content.cloudtech.cloudtech


class OpenSourcePage(base.ContentPage):
    """
    """
    htmlContent = content.opensource.opensource


class AboutPage(base.SidebarPage):
    """
    """
    sidebarLinks = const.aboutLinks


class WhoPage(AboutPage):
    """
    """
    htmlContent = content.about.who


class WhatPage(AboutPage):
    """
    """
    htmlContent = content.about.what


class CulturePage(AboutPage):
    """
    """
    htmlContent = content.about.culture


class JobsPage(AboutPage):
    """
    """
    htmlContent = content.about.jobs


class ContactPage(AboutPage):
    """
    """
    htmlContent = content.about.contact
