# -*- coding: utf-8
from twisted.python.filepath import FilePath
from twisted.web.template import Element, XMLFile


class TemplateLoader(Element):
    """
    """
    templateDir = "templates"
    templateFile = ""

    def __init__(self, loader=None, templateFile=None, request=None):
        super(TemplateLoader, self).__init__(loader=loader)
        self.request = request
        if templateFile:
            self.templateFile = templateFile
        template = FilePath(
            "%s/%s" % (self.templateDir, self.templateFile))
        self.loader = XMLFile(template.path)
