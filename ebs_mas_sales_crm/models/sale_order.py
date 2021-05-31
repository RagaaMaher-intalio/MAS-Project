# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="[('user_id', '=', user_id),'|', ('company_id', '=', False), ('company_id', '=', company_id)]", )


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('product_id', 'price_unit')
    def _check_minimum_price(self):
        for record in self:
            if record.price_unit > record.product_id.minimum_price:
                raise ValidationError(_("The Unit Price exceeds %(name)s Minimum Price %(price)s.", name=record.product_id.name, price=record.product_id.minimum_price))

