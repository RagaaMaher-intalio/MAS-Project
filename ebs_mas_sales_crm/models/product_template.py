# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_price = fields.Float('Minimum Price')


