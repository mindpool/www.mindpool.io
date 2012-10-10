import sys

from twisted.application import service, internet
from twisted.python import usage
from twisted.web import server

from klein import resource

from mindpoolsite import config, const, meta, routes
from mindpoolsite.scripts import sync


class SubCommandOptions(usage.Options):
    """
    A base class for subcommand options.

    Can also be used directly for subcommands that don't have options.
    """


class UpdateDBOptions(SubCommandOptions):
    """
    """
    optParameters = [
        ["language", "l", None,
         ("the language code whose dictionary you want to update; "
          "see 'twistd tharsk language' for the 3-letter codes of the "
          "supported languages")],
        ["action", "a", None,
         ("the type of update action to perform; valid options are "
          "'import', 'export' and 'drop'")],
    ]


class Options(usage.Options):
    """
    """
    optFlags = [
        ["debug", "b", "Enable debugging"],
        ["cache", "c", "Enable the use of memcache"],
    ]

    optParameters = [
        ["webport", "p", config.defaultPort,
         "The port to listen for HTTP requests"],
        # XXX add an option for setting the session timeout
        # XXX add a persona audience parameter
    ]

    subCommands = [
        ["stop", None, SubCommandOptions,
         "Stop the server"],
        ["update-db", None, UpdateDBOptions,
         "update one of the language databases"],
    ]

    def parseOptions(self, options):
        usage.Options.parseOptions(self, options)
        # override debug configuration if the option is passed
        if self.opts["debug"]:
            config.debug = True
        # override the caching configuration if the option is passed
        if self.opts["cache"]:
            config.cache = True
        # check options for subcommands
        if not self.subCommand:
            return
        elif self.subCommand == "stop":
            script = sync.StopDaemon()
            script.run()
            sys.exit(0)


class MindPoolSession(server.Session):
    """
    """
    # let's have our sessions last a full 24 hours
    sessionTimeout = config.sessionTimeout


def makeService(options):
    """
    """
    port = int(options["webport"])
    site = server.Site(resource())
    site.sessionFactory = MindPoolSession
    application = service.Application(meta.description)
    webService = internet.TCPServer(port, site)
    webService.setServiceParent(application)
    return webService
