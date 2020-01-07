# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'


	npwp = fields.Char(string="NPWP",)
	sale_order_ids = fields.One2many(string="Sale Orders",
									comodel_name="sale.order",
									inverse_name="partner_id", )

	@api.multi
	def create_invoice(self):
		obj_inv = self.env['account.invoice']
		obj_acc = self.env['account.account']

		account = obj_acc.search([('name','=','Cash')])

		data = {
				'partner_id' : self.id,
				'invoice_line_ids' : [
					(0,0,{
							'name': 'Subscription',
							'quanty' : 1.0,
							'price_unit' : 40,
							'account_id' : account[0].id,
							}),

					(0,0,{
							'name': 'Management Fee',
							'quanty' : 1.0,
							'price_unit' : 10,
							'account_id' : account[0].id,
							}),

				]
			}
		obj_inv.create(data)