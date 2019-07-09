# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Repair(models.Model):
    _inherit = 'repair.order'

    employee_reparador = fields.Many2one('hr.employee', 'Reparador')
    entregado_estatus = fields.Boolean(string='Entregado')
    imei = fields.Char('Imei', size=15)
    fecha_reparado = fields.Date('Fecha Reparado')
    