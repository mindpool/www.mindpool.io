from zope.interface import Interface


class IAccount(Interface):
    """
    A marker interface for Account objects.
    """
    pass


class IPersona(Interface):
    """
    A marker interface for Mozilla Persona (Browser ID) objects.
    """
