#!/bin/sh

DOMAIN='cciaa.modulistica'

i18ndude rebuild-pot --pot ${DOMAIN}.pot --create ${DOMAIN} ..
i18ndude merge --pot ${DOMAIN}.pot --merge ${DOMAIN}-manual.pot
i18ndude sync --pot ${DOMAIN}.pot ./*/LC_MESSAGES/${DOMAIN}.po

