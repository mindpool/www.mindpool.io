import txmongo.filter

from mindpoolsite import const, exceptions
from mindpoolsite.models import db


class CollectionModel(object):
    """
    """
    dbName = "tharsk"
    name = ""
    title = ""
    langCode = ""
    fields = tuple()
    _db = None
    filter = txmongo.filter

    def __init__(self):
        self.name = "%s_dictionary" % self.langCode
        self.fields = (
            const.langMapper[self.title],
            const.langMapper[self.translateTitle],
            "see-also",
            "%s-keywords" % const.langMapper[self.title],
            )

    @property
    def db(self):
        if not self._db:
            raise exceptions.DatabaseUndefined
        return self._db

    def getDB(self):
        def setDatabase(database):
            self._db = database
            return database

        d = db.getDatabase(self.dbName)
        d.addCallback(setDatabase)
        return d

    @property
    def collection(self):
        if not self._db:
            raise exceptions.DatabaseUndefined
        return getattr(self._db, self.name)

    def getAscendingFilter(self, fields, sortField):
        return self.filter.sort(self.filter.ASCENDING(sortField))

    def find(self, fields={}, sortField="", order="asc", **kwargs):
        if "filter" not in kwargs and sortField:
            if order == "asc":
                kwargs["filter"] = self.getAscendingFilter(
                    fields, sortField)
        return self.collection.find(fields=fields, **kwargs)

    def text_search(self, sort="alpha", order="asc", *terms):
        """
        Search takes advantage of stemming. It stems the input terms and
        matches those against the *_keywords_* indices.

        "order" can be "asc" or "desc"

        "sort" is "alpha" by default. The other acceped value is "rank" but
        this is not yet implemented.
        """
