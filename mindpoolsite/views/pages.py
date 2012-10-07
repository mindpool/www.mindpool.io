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
        return fragments.SplashTopNavFragment(request=request)

    @renderer
    def contentarea(self, request, tag):
        return fragments.SplashFragment()


class ServicesPage(base.SidebarPage):
    """
    """
    sidebarLinks = const.servicesLinks
    contentData = content.services.services


class ConsultingPage(ServicesPage):
    """
    """
    contentData = content.services.consulting


class TrainingPage(ServicesPage):
    """
    """
    contentData = content.services.training


class PeoplePage(base.SidebarPage):
    """
    """
    sidebarLinks = const.peopleLinks
    contentData = content.people.people


class TeamsPage(PeoplePage):
    """
    """
    contentData = content.people.teams


class MembersPage(PeoplePage):
    """
    """
    contentData = content.people.members


class CloudTechPage(base.SidebarPage):
    """
    """
    contentData = content.cloudtech.cloudtech
    sidebarLinks = const.cloudTechLinks


class LangsPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.langs


class FrameworksPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.frameworks


class ConcurrencyPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.concurrency


class MessagingPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.messaging


class DistributedPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.distributed


class BigDataPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.data


class VirtualizationPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.virtualization


class UXPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.ux


class OpenSourcePage(base.SidebarPage):
    """
    """
    contentData = content.opensource.opensource
    sidebarLinks = const.openSourceLinks


class AboutPage(base.SidebarPage):
    """
    """
    sidebarLinks = const.aboutLinks


class WhoPage(AboutPage):
    """
    """
    contentData = content.about.who


class WhatPage(AboutPage):
    """
    """
    contentData = content.about.what


class CulturePage(AboutPage):
    """
    """
    contentData = content.about.culture


class SocialLinksPage(AboutPage):
    """
    """
    contentData = content.about.social


class JobsPage(AboutPage):
    """
    """
    contentData = content.about.jobs


class ContactPage(AboutPage):
    """
    """
    contentData = content.about.contact


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
    contentData = ""
