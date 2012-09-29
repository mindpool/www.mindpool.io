import sys

from twisted.internet import reactor
from twisted.python import log

from mindpoolsite.scripts import base


class TwistedScript(base.Script):
    """
    """
    def run(self):
        log.startLogging(sys.stdout)
        log.msg("Running the script ...")
        super(TwistedScript, self).run()
        reactor.run()

    def stop(self, ignore):
        log.msg("Script finished.")
        reactor.stop()

    def logResult(self, result):
        log.msg(result)

    def logError(self, failure):
        log.msg("ERROR: ", failure)


class AddCollection(TwistedScript):
    """
    """
    modelClass = None
    csvFile = ""
    indexFields = ["%s_keywords", "%s_metaphone"]

    def doImport(self):

        # instantiate the collection model
        model = self.modelClass()

        def checkIndices(listResult):
            pass

        def createIndices(ids):
            pass

        def insertData(csvReader):
            pass

        def loadData(response):
            pass

        def dropIndexes(noValue):
            pass

        def dropCollection(database):
            pass

        # get the database and load the data
        d = model.getDB()
        d.addCallback(dropCollection)
        d.addErrback(self.logError)
        return d

    def run(self):
        d = self.doImport()
        d.addCallback(self.stop)
        super(AddCollection, self).run()


class DropCollection(TwistedScript):
    """
    """
    modelClass = None

    def doDrop(self):

        # instantiate the collection model
        model = self.modelClass()

        def printResult(result):
            if bool(result["ok"]) and not bool(result["err"]):
                log.msg("Successfully dropped collection '%s'." % model.name)
                log.msg("Deleted %s documents." % result["n"])

        def dropCollection(database):
            d = model.collection.drop(safe=True)
            d.addErrback(log.msg)
            d.addCallback(printResult)
            return d

        # get the database and drop the collection (defined in the model)
        d = model.getDB()
        d.addCallback(dropCollection)
        d.addErrback(self.logError)
        return d

    def run(self):
        d = self.doDrop()
        d.addCallback(self.stop)
        super(DropCollection, self).run()
