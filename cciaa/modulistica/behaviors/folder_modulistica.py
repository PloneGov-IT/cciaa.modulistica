# -*- coding: utf-8 -*-
from cciaa.modulistica import modulisticaMessageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IFolderWithColumnsExtension(model.Schema):

    columns = schema.List(
        title=_(
            u"label_cciaafolder_columnstitles",
            default=u"Columns titles"
        ),
        description=_(
            u"help_cciaafolder_columnstitles",
            default=u"Put there, one per line (up to 4), columns titles that must be put on the top of the created tables when using the files views. \n Not providing those values will not display any table headers."
        ),    
        required=False,
        value_type=schema.TextLine(),
        default=[],
    )


@implementer(IFolderWithColumnsExtension)
@adapter(IDexterityContent)
class FolderWithColumnsExtension(object):

    def __init__(self, context):
        self.context = context

