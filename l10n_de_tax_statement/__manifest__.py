# -*- coding: utf-8 -*-
# Copyright 2017 BIG-Consulting GmbH(<http://www.openbig.org>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'German VAT Statement',
    'version': '10.0.1.1.0',
    'category': 'Localization',
    'license': 'AGPL-3',
    'author': 'OpenBIG.org, Odoo Community Association (OCA)',
    'website': 'http://www.openbig.org',
    'depends': [
        'account_tax_balance',
        'report',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/tax_statement_security_rule.xml',
        'data/report_layouts.xml',
        'views/l10n_de_tax_statement.xml',
        'report/reports.xml',
        'report/report_tax_statement.xml',
        'wizard/l10n_de_tax_statement_config_wizard.xml',
    ],
    'installable': True,
}
