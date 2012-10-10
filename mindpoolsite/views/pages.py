import functools
import json

from twisted.internet import protocol, reactor
from twisted.protocols import memcache
from twisted.python import log
from twisted.web.server import NOT_DONE_YET
from twisted.web.template import flattenString, renderer

from browserid import checker

from mindpoolsite import auth, config, content, urls
from mindpoolsite.views import basepages as base, fragments


class MemCacheHelper(object):
    """
    """
    def __init__(self, request, pageClass):
        self.request = request
        self.pageClass = pageClass
        self.memcache = None
        self.key = ""

    def setPage(self, page):
        d = self.memcache.set(self.key, page)
        d.addErrback(log.msg)
        return page

    def getOrFlattenPage(self, result):
        flags, page = result
        if page:
            if config.debug:
                log.msg("Cache hit; skipping page generation ...")
            return page
        if config.debug:
            log.msg("No page in cache; getting and setting ...")
        d = flattenString(self.request, self.pageClass())
        d.addErrback(log.msg)
        d.addCallback(self.setPage)
        return d

    def pokeMemCache(self, mem):
        if not mem:
            if config.debug:
                log.msg("Cannot connect to memcache server!")
            return self.pageClass()
        self.memcache = mem
        d = self.memcache.get(self.key)
        d.addErrback(log.msg)
        d.addCallback(self.getOrFlattenPage)
        return d

    def getPage(self):
        """
        """
        self.key = auth.getSessionAccount(
            self.request).getKey(self.request.path)
        if config.debug:
            log.msg("Generated key:", self.key)
        client = protocol.ClientCreator(reactor, memcache.MemCacheProtocol)
        d = client.connectTCP("localhost", memcache.DEFAULT_PORT)
        d.addErrback(log.msg)
        d.addCallback(self.pokeMemCache)
        d.addErrback(log.msg)
        return d


def cache(routeFunction):
    """
    A decorator for caching pages.
    """
    @functools.wraps(routeFunction)
    def wrapper(request):
        pageClass = routeFunction(request)
        if not config.cache:
            return pageClass
        return MemCacheHelper(request, pageClass).getPage()
    return wrapper


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
    sidebarLinks = urls.servicesLinks
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
    sidebarLinks = urls.peopleLinks
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
    sidebarLinks = urls.cloudTechLinks


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


class AsAServicePage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.aas


class SDNPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.sdn


class UXPage(CloudTechPage):
    """
    """
    contentData = content.cloudtech.ux


class OpenSourcePage(base.SidebarPage):
    """
    """
    contentData = content.opensource.opensource
    sidebarLinks = urls.openSourceLinks


class AboutPage(base.SidebarPage):
    """
    """
    sidebarLinks = urls.aboutLinks


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


class LoginPage(base.BaseResourcePage):
    """
    """
    def success(self, results, request):
        """
        This callback is only fired upon successful BrowserID login.
        """
        interface, avatar, logout = results
        account = auth.createSessionAccount(request, avatar)
        request.setHeader("content-type", "application/json")
        request.write(json.dumps({
            "results": {
                "email": account.getEmail(),
                "displayName": account.getDisplayName(),
            }
        }))
        request.finish()

    def render(self, request):
        body = json.load(request.content)
        credentials = checker.BrowserIDAssertion(body["assertion"])
        d = self.portal.login(credentials, None, auth.IPersona)
        d.addErrback(self.handleError)
        d.addCallback(self.success, request)
        return NOT_DONE_YET


class LogoutPage(base.BaseResourcePage):
    """
    """
    def render(self, request):
        request.getSession().expire()
        return json.dumps({"results": "session expired (logout)"})


class AccountPage(base.ContentPage):
    """
    """
    #sidebarLinks = urls.membersLinks

    def getContentDataTemplate(self, request):
        account = auth.getSessionAccount(request)
        template = content.members.accountAnonymous
        if account.getEmail():
            template = content.members.accountLoggedIn
        return template % {
            "primaryEmail": account.getEmail(),
            "displayName": account.getDisplayName(),
            "fullName": account.fullName,
            "associatedEmails": account.associatedEmails,
            "grantedRoles": account.grantedRoles,
            "sessionID": account.getSessionID()}
