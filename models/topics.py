# -*- coding: utf-8 -*-

from odoo import models, fields

class TrainingTopics(models.Model):
    _name = 'bista.training.topics'
    _description = 'Role Master Description.'

    name = fields.Char(string='Topics Name', required=True)
    subject_id = fields.Many2one('bista.training.subject', string='Subject', readonly=True)

	