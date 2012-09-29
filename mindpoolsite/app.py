import sys

from twisted.application import service, internet
from twisted.python import usage
from twisted.web import server

from klein import resource

from mindpoolsite import meta, routes
from mindpoolsite.scripts import async, sync


class SubCommandOptions(usage.Options):
    """
    A base class for subcommand options.

    Can also be used directly for subcommands that don't have options.
    """


class UpdateSourceOptions(SubCommandOptions):
    """
    """
    optParameters = [
        ["language", "l", None,
         ("the language code whose source files you want to update; "
          "see 'twistd tharsk language' for the 3-letter codes of the "
          "supported languages")],
        ["action", "a", None,
         ("the type of update action to perform; valid options are "
          "'parse-wordlist' and 'add-keywords'")],
    ]


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
    optParameters = [
        ["webport", "p", 9080, "The port to listen for HTTP requests"],
    ]

    subCommands = [
        ["stop", None, SubCommandOptions,
         "Stop the server"],
        ["update-db", None, UpdateDBOptions,
         "update one of the language databases"],
        ["update-source", None, UpdateSourceOptions,
         "update one of the language source files"],
    ]

    def parseOptions(self, options):
        usage.Options.parseOptions(self, options)
        # check options
        if not self.subCommand:
            return
        elif self.subCommand == "stop":
            script = sync.StopDaemon()
            script.run()
            sys.exit(0)
        elif self.subCommand == "update-source":
            script = sync.UpdateSourceDispatch(self)
            script.run()
            sys.exit(0)
        elif self.subCommand == "update-db":
            script = async.UpdateDBDispatch(self)
            script.run()
            sys.exit(0)


def makeService(options):
    """
    """
    port = int(options["webport"])
    site = server.Site(resource())
    application = service.Application(meta.description)
    webService = internet.TCPServer(port, site)
    webService.setServiceParent(application)
    return webService
