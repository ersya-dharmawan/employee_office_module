# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeRequest(models.Model):
	_name = 'employee.request' # Table in DB
	_inherit = ['mail.thread']
	_description = 'Employee Request'
	_rec_name = 'nama'

	nama = fields.Char(string="Nama", required=True, help='Wajib, Isi Nama!')
	date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now())
	date_to = fields.Datetime(string='End Date')
	employee_id = fields.Many2one(comodel_name='hr.employee', delegate=True, string='Employee')
	car_id = fields.Many2one(comodel_name='fleet.vehicle', delegate=True, string='Car')
	state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Confirm'),
														 ('validate', 'Validated'), ('refuse', 'Refuse'),
														 ('approved', 'Approved')], default='draft', track_visibility="onchange")

	@api.multi
	def confirm_request(self):
		self.state = 'confirm'

	@api.multi
	def validate_request(self):
		self.state = 'validate'

	@api.multi
	def refuse_request(self):
		self.state = 'refuse'

	@api.multi
	def approve_request(self):
		self.state = 'approved'