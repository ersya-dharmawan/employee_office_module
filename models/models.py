# -*- coding: utf-8 -*-

from odoo import models, fields

class EmployeeRequest(models.Model):
	_name = 'employee.request' # Table in DB
	_description = 'Employee Request'

	nama = fields.Char(string="Nama", required=True, help='Wajib, Isi Nama!')
	date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now())
	date_to = fields.Datetime(string='End Date')
	employee_id = fields.Many2one(comodel_name='hr.employee', delegate=True, string='Employee')
	car_id = fields.Many2one(comodel_name='fleet.vehicle', delegate=True, string='Car')