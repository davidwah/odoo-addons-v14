# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleV14(http.Controller):
#     @http.route('/module__v14/module__v14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module__v14/module__v14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module__v14.listing', {
#             'root': '/module__v14/module__v14',
#             'objects': http.request.env['module__v14.module__v14'].search([]),
#         })

#     @http.route('/module__v14/module__v14/objects/<model("module__v14.module__v14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module__v14.object', {
#             'object': obj
#         })
