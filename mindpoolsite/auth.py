from zope.interface import Interface, implements

from twisted.cred.portal import IRealm, Portal


class IAccount(Interface):
    """
    """
    pass # marker for callers who want these Account objects


class Account(object):
    """
    """
    def __init__(self, email, role=""):
        self.email = email
        self.role = role


class AccountRealm(object):
    """
    """
    implements(IRealm)

    def requestAvatar(self, avatarId, mind, *interfaces):
        if IAccount in interfaces:
            # this is a good place to pull information from a DB
            avatar = Account(avatarId)
            logout = None
            return (IAccount, avatar, logout)
        raise NotImplementedError("no interface")
