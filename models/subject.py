# -*- coding: utf-8 -*-

from odoo import models, fields

class TrainingSubject(models.Model):
    _name = 'bista.training.subject'
    _description = 'Role Master Description.'

    name = fields.Char(string='Subject Name', required=True)
    description = fields.Html(string='Description')
    topics_ids = fields.One2many('bista.training.topics', 'subject_id', string='Topics')
    trainers_ids = fields.Many2many('bista.trainer', string='Trainers')

