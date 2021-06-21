# -*- coding: utf-8 -*-

from odoo import models, fields

class TraineeRole(models.Model):
    _name = 'bista.trainee.role'
    _description = 'Role Master Description.'

    name = fields.Char(string='Role Name', required=True)
    sequnce = fields.Integer(string='Sequnce')

	