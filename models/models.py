# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'


	npwp = fields.Char(string="NPWP",)
	sale_order_ids = fields.One2many(string="Sale Orders",
									)