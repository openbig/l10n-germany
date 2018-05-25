# -*- coding: utf-8 -*-
# Copyright 2017 BIG-Consulting GmbH(<http://www.openbig.org>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.tools.misc import formatLang
from odoo.exceptions import Warning as UserError


BASE_DISPLAY = (
    '20', '21', '22', '23', '24',
    '26', '27', '28', '29', '30',
    '32', '33', '34', '35', '36',
    '38', '39', '40', '41', '42',
    '48', '49', '50', '51', '52',
)

TAX_DISPLAY = (
    '26', '27', '28', '30',
    '33', '34', '35', '36',
    '48', '49', '50', '51', '52', '53', '54',
    '56', '57', '58', '59', '60',
    '61', '62', '63', '65', '66', '67', '68',
)

GROUP_DISPLAY = (
    '17', '18', '19',
    '25', '31', '37',
    '47', '55', '64',
)

EDITABLE_DISPLAY = (
    '67', '28', '35',
)


class VatStatementLine(models.Model):
    _name = 'l10n.de.tax.statement.line'
    _order = 'code'

    name = fields.Char()
    code = fields.Char()

    statement_id = fields.Many2one(
        'l10n.de.tax.statement',
        'Statement'
    )
    currency_id = fields.Many2one(
        'res.currency',
        related='statement_id.company_id.currency_id',
        readonly=True,
        help='Utility field to express amount currency'
    )
    base = fields.Monetary()
    tax = fields.Monetary()
    format_base = fields.Char(compute='_compute_amount_format')
    format_tax = fields.Char(compute='_compute_amount_format')

    is_group = fields.Boolean(compute='_compute_is_group')
    is_readonly = fields.Boolean(compute='_compute_is_readonly')

    state = fields.Selection(related='statement_id.state')

    @api.multi
    @api.depends('base', 'tax', 'code')
    def _compute_amount_format(self):
        for line in self:
            base = formatLang(self.env, line.base, monetary=True)
            tax = formatLang(self.env, line.tax, monetary=True)
            if line.code in BASE_DISPLAY:
                line.format_base = base
            if line.code in TAX_DISPLAY:
                line.format_tax = tax

    @api.multi
    @api.depends('code')
    def _compute_is_group(self):
        for line in self:
            line.is_group = line.code in GROUP_DISPLAY

    @api.multi
    @api.depends('code')
    def _compute_is_readonly(self):
        for line in self:
            if line.state == 'draft':
                line.is_readonly = line.code not in EDITABLE_DISPLAY
            else:
                line.is_readonly = True

    @api.multi
    def unlink(self):
        for line in self:
            if line.statement_id.state == 'posted':
                raise UserError(
                    _('You cannot delete lines of a posted statement! '
                      'Reset the statement to draft first.'))
        super(VatStatementLine, self).unlink()
