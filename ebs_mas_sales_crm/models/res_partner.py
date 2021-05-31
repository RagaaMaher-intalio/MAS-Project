# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class ResPartner(models.Model):
    _inherit = 'res.partner'

    marketing_representative_id = fields.Many2one('hr.employee', string='Marketing representative')
    mas_code = fields.Char(string='Customer Code', copy=False)

    @api.model
    def create(self, vals):

        vals['mas_code'] = vals['city']+ self.env['ir.sequence'].next_by_code('mas.customer.code') or _('New')
        return super(ResPartner, self).create(vals)


