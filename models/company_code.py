from odoo import api, fields, models, api, _


class CompanyCode(models.Model):
    _inherit = 'res.company'

    # company_code = fields.Char(string='Company Code', required=True)
    company_code = fields.Char(string='Company Code', required=True,
                               copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('company_code', _('New')) == _('New'):
            vals['company_code'] = self.env['ir.sequence'].next_by_code(
                'company.code.sequence') or _('New')
        result = super(CompanyCode, self).create(vals)
        return result
