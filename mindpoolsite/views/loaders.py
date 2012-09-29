# -*- coding: utf-8
from datetime import datetime
import os.path

from twisted.python.filepath import FilePath
from twisted.web.template import Element, XMLFile, renderer, tags

from mindpoolsite import const, content, meta, utils
from mindpoolsite.models import collection
from mindpoolsite.controllers import retrieve


class TemplateLoader(Element):
    """
    """
    templateDir = "templates"
    templateFile = ""

    def __init__(self, loader=None, templateFile=None):
        super(TemplateLoader, self).__init__(loader=loader)
        if templateFile:
            self.templateFile = templateFile
        template = FilePath(
            "%s/%s" % (self.templateDir, self.templateFile))
        self.loader = XMLFile(template.path)
