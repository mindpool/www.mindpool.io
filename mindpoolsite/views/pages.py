import functools
import json

from twisted.web.server import NOT_DONE_YET
from twisted.web.template import renderer

import klein

from browserid import checker

from mindpoolsite import auth, config, content, iface, urls
from mindpoolsite.views import basepages as base, fragments


def cache(routeFunction):
    """
    A decorator for caching pages.

    Initially intended to be used with klein route functions like this:

        @route("/some/path")
        @cache
        def somePath(request):
            return somePageClass

    this decortator is now being used to do the caching via parameters passed
    to the route decorator.
    """
    @functools.wraps(routeFunction)
    def wrapper(request):
        pageClass = routeFunction(request)
        if not config.cache:
            return pageClass()
        return base.MemCacheHelper(request, pageClass).getPage()
    return wrapper


def route(url, caching=False, *args, **kwargs):
    """
    A decorator that overrides the standard klein route decorator with
    additional keyword arguments.

    Using this decorator is a short-cut; you would otherwise need to use this:

        @klein.route("/my/url")
        @cache
        def getSomePage(request):
            return GetSomePageClass

    With this decorator, you only need to do the following:

        @route("/my/url", caching=True)
        def getSomePage(request):
            return GetSomePageClass

    In order to allow additional keyword arguments on the route decorator
    (above and beyond what Klein provides), we need do inside the decorator
    what we would have done by decorating the function itself:
        * check to see if the caching argument was set
        * if it was, pass the decorated function to the cache decorator
        * then apply the Klein route decorator (to the function that is now
          possibly decorated for caching)
        * return the wrapper that does this bit of jiggery-pokery
    """
    router = klein.route(url, *args, **kwargs)

    def cacheWrapper(routeFunction):
        if caching:
            # note that before the '@' syntax, this is how we used to decorate
            # functions ...
            routeFunction = cache(routeFunction)
        return router(routeFunction)
    return cacheWrapper


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


class TechPage(base.SidebarPage):
    """
    """
    contentData = content.tech.main
    sidebarLinks = urls.techLinks


class LangsPage(TechPage):
    """
    """
    contentData = content.tech.langs


class FrameworksPage(TechPage):
    """
    """
    contentData = content.tech.frameworks


class ConcurrencyPage(TechPage):
    """
    """
    contentData = content.tech.concurrency


class MessagingPage(TechPage):
    """
    """
    contentData = content.tech.messaging


class DistributedPage(TechPage):
    """
    """
    contentData = content.tech.distributed


class BigDataPage(TechPage):
    """
    """
    contentData = content.tech.data


class AsAServicePage(TechPage):
    """
    """
    contentData = content.tech.aas


class SDNPage(TechPage):
    """
    """
    contentData = content.tech.sdn


class UXPage(TechPage):
    """
    """
    contentData = content.tech.ux


class OpenSourcePage(base.SidebarPage):
    """
    """
    contentData = content.opensource.main
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
        d = self.portal.login(credentials, None, iface.IPersona)
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
