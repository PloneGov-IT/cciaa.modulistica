import logging

log = logging.getLogger('cciaa.modulistica')
PROFILE_ID = 'profile-cciaa.modulistica:default'


def upgrade_1000_to_1100(context):
    context.runImportStepFromProfile(PROFILE_ID, 'typeinfo')
