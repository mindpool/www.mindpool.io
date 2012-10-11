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
    """
    @functools.wraps(routeFunction)
    def wrapper(request):
        pageClass = routeFunction(request)
        if not config.cache:
            return pageClass()
        return base.MemCacheHelper(request, pageClass).getPage()
    return wrapper


def route(url, cache=False, *args, **kwargs):
    return klein.route(url, *args, **kwargs)


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


class SolutionsPage(base.SidebarPage):
    """
    """
    contentData = content.solutions.solutions
    sidebarLinks = urls.SolutionsLinks


class LangsPage(SolutionsPage):
    """
    """
    contentData = content.solutions.langs


class FrameworksPage(SolutionsPage):
    """
    """
    contentData = content.solutions.frameworks


class ConcurrencyPage(SolutionsPage):
    """
    """
    contentData = content.solutions.concurrency


class MessagingPage(SolutionsPage):
    """
    """
    contentData = content.solutions.messaging


class DistributedPage(SolutionsPage):
    """
    """
    contentData = content.solutions.distributed


class BigDataPage(SolutionsPage):
    """
    """
    contentData = content.solutions.data


class AsAServicePage(SolutionsPage):
    """
    """
    contentData = content.solutions.aas


class SDNPage(SolutionsPage):
    """
    """
    contentData = content.solutions.sdn


class UXPage(SolutionsPage):
    """
    """
    contentData = content.solutions.ux


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
