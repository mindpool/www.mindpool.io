"""
Routes are defined with decorators. They may be either functions or static
methods. Note that if a group of routes are organized into a class, they need
to receive the @staticmethod decorator, since the @pages.cache decorator does
not expect the 'self' parameter.
"""
from twisted.cred import portal
from twisted.web import static

from browserid import checker

from klein.app import _globalKleinApp as app

from mindpoolsite import auth, config, urls
from mindpoolsite.views import pages


@pages.route(urls.map["root"], caching=True)
def root(request):
    return pages.SplashPage


class Services(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["services"], caching=True)
    def services(request):
        return pages.ServicesPage

    @staticmethod
    @pages.route(urls.map["consulting"], caching=True)
    def consulting(request):
        return pages.ConsultingPage

    @staticmethod
    @pages.route(urls.map["training"], caching=True)
    def training(request):
        return pages.TrainingPage


class People(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["people"], caching=True)
    def people(request):
        return pages.PeoplePage

    @staticmethod
    @pages.route(urls.map["teams"], caching=True)
    def teams(request):
        return pages.TeamsPage

    @staticmethod
    @pages.route(urls.map["members"], caching=True)
    def members(request):
        return pages.MembersPage


class Technologies(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["solutions"], caching=True)
    def Solutions(request):
        return pages.SolutionsPage

    @staticmethod
    @pages.route(urls.map["langs"], caching=True)
    def langs(request):
        return pages.LangsPage

    @staticmethod
    @pages.route(urls.map["frameworks"], caching=True)
    def frameworks(request):
        return pages.FrameworksPage

    @staticmethod
    @pages.route(urls.map["concurrency"], caching=True)
    def concurrency(request):
        return pages.ConcurrencyPage

    @staticmethod
    @pages.route(urls.map["messaging"], caching=True)
    def messaging(request):
        return pages.MessagingPage

    @staticmethod
    @pages.route(urls.map["distributed"], caching=True)
    def distributed(request):
        return pages.DistributedPage

    @staticmethod
    @pages.route(urls.map["big-data"], caching=True)
    def data(request):
        return pages.BigDataPage

    @staticmethod
    @pages.route(urls.map["aas"], caching=True)
    def aas(request):
        return pages.AsAServicePage

    @staticmethod
    @pages.route(urls.map["sdn"], caching=True)
    def sdn(request):
        return pages.SDNPage

    @staticmethod
    @pages.route(urls.map["ux"], caching=True)
    def ux(request):
        return pages.UXPage


@pages.route(urls.map["open-source"], caching=True)
def openSource(request):
    return pages.OpenSourcePage


class About(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["about"], caching=True)
    def about(request):
        return pages.AboutPage

    @staticmethod
    @pages.route(urls.map["who"], caching=True)
    def who(request):
        return pages.WhoPage

    @staticmethod
    @pages.route(urls.map["what"], caching=True)
    def what(request):
        return pages.WhatPage

    @staticmethod
    @pages.route(urls.map["culture"], caching=True)
    def culture(request):
        return pages.CulturePage

    @staticmethod
    @pages.route(urls.map["social"], caching=True)
    def social(request):
        return pages.SocialLinksPage

    @staticmethod
    @pages.route(urls.map["careers"], caching=True)
    def careers(request):
        return pages.JobsPage

    @staticmethod
    @pages.route(urls.map["contact"], caching=True)
    def contact(request):
        return pages.ContactPage


@pages.route(urls.map["assets"])
def assets(request):
    return static.File(config.assetsDirectory)


class Members(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["login"], methods=["POST"])
    def login(request):
        realm = auth.AccountRealm()
        loginPortal = portal.Portal(realm)
        loginPortal.registerChecker(checker.BrowserIDChecker(
            config.pesonaAudience, certsDir=config.certsDirectory))
        return pages.LoginPage(app, loginPortal)

    @staticmethod
    @pages.route(urls.map["logout"])
    def logout(request):
        return pages.LogoutPage(app, None)

    @staticmethod
    @pages.route(urls.map["account"])
    def account(request):
        return pages.AccountPage()
