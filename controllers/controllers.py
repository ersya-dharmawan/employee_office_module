# -*- coding: utf-8 -*-
from odoo import http

# class EmployeeOffice(http.Controller):
#     @http.route('/employee_office/employee_office/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_office/employee_office/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_office.listing', {
#             'root': '/employee_office/employee_office',
#             'objects': http.request.env['employee_office.employee_office'].search([]),
#         })

#     @http.route('/employee_office/employee_office/objects/<model("employee_office.employee_office"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_office.object', {
#             'object': obj
#         })