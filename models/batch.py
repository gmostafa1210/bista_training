# -*- coding: utf-8 -*-

from odoo import models, fields


class TrainingAttendance(models.Model):
    _name = 'bista.batch'
    _description = 'Training Batch Master Description.'

    name = fields.Char(string='Batch Name')
    trainee_ids = fields.One2many('bista.trainee', 'batch_id', string='Trainee List')

    