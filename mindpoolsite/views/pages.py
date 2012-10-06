import json

#from twisted.web import resource
from twisted.web.server import NOT_DONE_YET
from twisted.web.template import renderer

from browserid import checker

from klein.resource import KleinResource

from mindpoolsite import auth, const, content
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


class CloudTechPage(base.SidebarPage):
    """
    """
    htmlContent = content.cloudtech.cloudtech
    sidebarLinks = const.cloudTechLinks


class LangsPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.langs


class FrameworksPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.frameworks


class ConcurrencyPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.concurrency


class MessagingPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.messaging


class DistributedPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.distributed


class BigDataPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.data


class VirtualizationPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.virtualization


class UXPage(CloudTechPage):
    """
    """
    htmlContent = content.cloudtech.ux


class OpenSourcePage(base.SidebarPage):
    """
    """
    htmlContent = content.opensource.opensource
    sidebarLinks = const.openSourceLinks


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


class SocialLinksPage(AboutPage):
    """
    """
    htmlContent = content.about.social


class JobsPage(AboutPage):
    """
    """
    htmlContent = content.about.jobs


class ContactPage(AboutPage):
    """
    """
    htmlContent = content.about.contact


class LoginPage(KleinResource):
    """
    """
    def __init__(self, app, portal):
        KleinResource.__init__(self, app)
        self.portal = portal

    def writeLoginResults(self, results, request):
            interface, avatar, logout = results
            account = avatar
            # XXX Now we need to set a session cookie and maintain a mapping to
            # this Account object. Assertions are very short lived (5 minutes),
            # so this code provides a one-shot login.
            request.setHeader("content-type", "application/json")
            request.write(
                json.dumps({"results": "logged in as %s" % account.email}))
            request.finish()

    def render(self, request):
        body = json.load(request.content)
        credentials = checker.BrowserIDAssertion(body["assertion"])
        d = self.portal.login(credentials, None, auth.IAccount)
        d.addCallback(self.writeLoginResults, request)
        return NOT_DONE_YET


class LogoutPage(base.ContentPage):
    """
    """
    htmlContent = ""
