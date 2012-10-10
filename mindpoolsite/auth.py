from zope.interface import Interface, implements

from twisted.cred.portal import IRealm
from twisted.python.components import registerAdapter
from twisted.web.server import Session

from mindpoolsite import iface


# XXX this likely will go wherever the datamodels end up ... or maybe I'll
# rename this to SessionAccount, and link SessionAccount to the persisted
# Account data ...
class Account(object):
    """
    """
    implements(iface.IAccount)

    def __init__(self, session):
        self.session = session
        self.primaryEmail = ""
        self.displayName = ""
        self.fullName = ""
        self.associatedEmails = []
        self.grantedRoles = []
        self.sessionID = ""

    def setEmail(self, email):
        self.primaryEmail = email

    def getEmail(self):
        return self.primaryEmail

    def addEmail(self, email):
        if not self.getEmail():
            self.setEmail(email)
        else:
            self.associatedEmails.append(email)

    def setDisplayName(self, name):
        self.displayName = name

    def getDisplayName(self):
        return self.displayName

    def addRole(self, role):
        self.grantedRoles.append(role)

    def getSessionID(self):
        return self.session.uid

    def getKey(self, data):
        """
        For use by memcached; can't be unicode.
        """
        return str("%s%s%s" % (data, self.sessionID, self.primaryEmail))


class Persona(object):
    """
    """
    implements(iface.IPersona)

    def __init__(self, email, role=""):
        self.email = email


class AccountRealm(object):
    """
    """
    implements(IRealm)

    def requestAvatar(self, avatarId, mind, *interfaces):
        if IPersona in interfaces:
            # this is a good place to pull information from a DB
            avatar = Persona(avatarId)
            logout = None
            return (iface.IPersona, avatar, logout)
        raise NotImplementedError("no interface")


def getSessionAccount(request):
    return iface.IAccount(request.getSession())


def createSessionAccount(request, avatar):
    account = getSessionAccount(request)
    account.setEmail(avatar.email)
    account.setDisplayName(avatar.email.split("@")[0])
    return account


registerAdapter(Account, Session, iface.IAccount)
