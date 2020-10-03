# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class module__v14(models.Model):
#     _name = 'module__v14.module__v14'
#     _description = 'module__v14.module__v14'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
