# -*- coding: utf-8 -*-
# from odoo import http


# class EbsMasSales(http.Controller):
#     @http.route('/ebs_mas_sales/ebs_mas_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ebs_mas_sales/ebs_mas_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ebs_mas_sales.listing', {
#             'root': '/ebs_mas_sales/ebs_mas_sales',
#             'objects': http.request.env['ebs_mas_sales.ebs_mas_sales'].search([]),
#         })

#     @http.route('/ebs_mas_sales/ebs_mas_sales/objects/<model("ebs_mas_sales.ebs_mas_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ebs_mas_sales.object', {
#             'object': obj
#         })
