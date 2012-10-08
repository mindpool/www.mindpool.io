from zope.interface import Interface, implements

from twisted.cred.portal import IRealm, Portal
from twisted.python.components import registerAdapter
from twisted.web.server import Session


# XXX this needs to go in an iface module
class IAccount(Interface):
    """
    A marker interface for Account objects.
    """
    pass


# XXX this likely will go wherever the datamodels end up ... or maybe I'll
# rename this to SessionAccount, and link SessionAccount to the persisted
# Account data ...
class Account(object):
    """
    """
    implements(IAccount)

    def __init__(self, session):
        self.session = session
        self.email = ""
        self.displayName = ""
        self.role = ""
        self.sessionID = ""

    def setEmail(self, email):
        self.email = email

    def setDisplayName(self, name):
        self.displayName = name

    def setRole(self, role):
        self.role = role

    def setSessionID(self, sessionID):
        self.sessionID = sessionID


class IPersona(Interface):
    """
    A marker interface for Mozilla Persona (Browser ID) objects.
    """


class Persona(object):
    """
    """
    implements(IPersona)

    def __init__(self, email, role=""):
        self.email = email


class AccountRealm(object):
    """
    """
    implements(IRealm)

    def requestAvatar(self, avatarId, mind, *interfaces):
        print "In requestAvatar:", avatarId, mind, interfaces
        if IPersona in interfaces:
            # this is a good place to pull information from a DB
            avatar = Persona(avatarId)
            logout = None
            return (IPersona, avatar, logout)
        raise NotImplementedError("no interface")


def getSessionAccount(request):
    session = request.getSession()
    account = IAccount(session)
    account.setSessionID(session.uid)
    return account


registerAdapter(Account, Session, IAccount)
