# -*- coding: utf-8 -*-
from plone.behavior.interfaces import IBehaviorAssignable
from plone.dexterity.schema import SCHEMA_CACHE
from zope.component import adapter
from zope.interface import implementer
from plone.app.contenttypes.interfaces import IFolder


@implementer(IBehaviorAssignable)
@adapter(IFolder)
class DexterityBehaviorAssignable(object):
    """Support plone.behavior behaviors stored in the FTI
    """

    def __init__(self, context):
        self.context = context

    def supports(self, behavior_interface):
        for behavior in self.enumerateBehaviors():
            if behavior_interface in behavior.interface._implied:
                return True
        return False

    def enumerateBehaviors(self):
        isview = self.context.layout == 'cciaa_modulistica_view'
        iface = 'cciaa.modulistica.behaviors.folder_modulistica.'\
                'IFolderWithColumnsExtension'
        for behavior in SCHEMA_CACHE.behavior_registrations(
            self.context.portal_type
        ):
            if not isview and behavior.interface.__identifier__ == iface:
                continue
            yield behavior
