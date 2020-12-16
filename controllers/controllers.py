# -*- coding: utf-8 -*-
# from odoo import http


# class CompanyCode(http.Controller):
#     @http.route('/company_code/company_code/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_code/company_code/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_code.listing', {
#             'root': '/company_code/company_code',
#             'objects': http.request.env['company_code.company_code'].search([]),
#         })

#     @http.route('/company_code/company_code/objects/<model("company_code.company_code"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_code.object', {
#             'object': obj
#         })
