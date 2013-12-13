# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from Products.Archetypes.Field import LinesField
from Products.Archetypes import atapi

#from Products.ATContentTypes.interface import IATFolder
from cciaa.modulistica.interfaces import CCIAAModAbleContent
from cciaa.modulistica import modulisticaMessageFactory as _

class ExtensionColumnsField(ExtensionField, LinesField):
    """ derivative of LinesField for extending schemas """


class FolderWithColumnsExtender(object):
    adapts(CCIAAModAbleContent)
    implements(ISchemaExtender)

    fields = [
        ExtensionColumnsField('columns',
            widget=atapi.LinesWidget(
                label= _(u'label_cciaafolder_columnstitles', default=u'Columns titles'),
                description = _(u'help_cciaafolder_columnstitles',
                                default=u"Put there, one per line (up to 4), columns titles that must be put on the top of the "
                                        u"created tables when using the files views. \n"
                                        u"Not providing those values will not display any table headers.",
                ),
                condition="python:here.getLayout()=='cciaa_modulistica_view'",
            ),
            required=False,
        ),

    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
