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


@pages.route(urls.map["root"])
@pages.cache
def root(request):
    return pages.SplashPage


class Services(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["services"])
    @pages.cache
    def services(request):
        return pages.ServicesPage

    @staticmethod
    @pages.route(urls.map["consulting"])
    @pages.cache
    def consulting(request):
        return pages.ConsultingPage

    @staticmethod
    @pages.route(urls.map["training"])
    @pages.cache
    def training(request):
        return pages.TrainingPage


class People(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["people"])
    @pages.cache
    def people(request):
        return pages.PeoplePage

    @staticmethod
    @pages.route(urls.map["teams"])
    @pages.cache
    def teams(request):
        return pages.TeamsPage

    @staticmethod
    @pages.route(urls.map["members"])
    @pages.cache
    def members(request):
        return pages.MembersPage


class Technologies(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["solutions"])
    @pages.cache
    def Solutions(request):
        return pages.SolutionsPage

    @staticmethod
    @pages.route(urls.map["langs"])
    @pages.cache
    def langs(request):
        return pages.LangsPage

    @staticmethod
    @pages.route(urls.map["frameworks"])
    @pages.cache
    def frameworks(request):
        return pages.FrameworksPage

    @staticmethod
    @pages.route(urls.map["concurrency"])
    @pages.cache
    def concurrency(request):
        return pages.ConcurrencyPage

    @staticmethod
    @pages.route(urls.map["messaging"])
    @pages.cache
    def messaging(request):
        return pages.MessagingPage

    @staticmethod
    @pages.route(urls.map["distributed"])
    @pages.cache
    def distributed(request):
        return pages.DistributedPage

    @staticmethod
    @pages.route(urls.map["big-data"])
    @pages.cache
    def data(request):
        return pages.BigDataPage

    @staticmethod
    @pages.route(urls.map["aas"])
    @pages.cache
    def aas(request):
        return pages.AsAServicePage

    @staticmethod
    @pages.route(urls.map["sdn"])
    @pages.cache
    def sdn(request):
        return pages.SDNPage

    @staticmethod
    @pages.route(urls.map["ux"])
    @pages.cache
    def ux(request):
        return pages.UXPage


@pages.route(urls.map["open-source"])
@pages.cache
def openSource(request):
    return pages.OpenSourcePage


class About(object):
    """
    """
    @staticmethod
    @pages.route(urls.map["about"])
    @pages.cache
    def about(request):
        return pages.AboutPage

    @staticmethod
    @pages.route(urls.map["who"])
    @pages.cache
    def who(request):
        return pages.WhoPage

    @staticmethod
    @pages.route(urls.map["what"])
    @pages.cache
    def what(request):
        return pages.WhatPage

    @staticmethod
    @pages.route(urls.map["culture"])
    @pages.cache
    def culture(request):
        return pages.CulturePage

    @staticmethod
    @pages.route(urls.map["social"])
    @pages.cache
    def social(request):
        return pages.SocialLinksPage

    @staticmethod
    @pages.route(urls.map["careers"])
    @pages.cache
    def careers(request):
        return pages.JobsPage

    @staticmethod
    @pages.route(urls.map["contact"])
    @pages.cache
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
