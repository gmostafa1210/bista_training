# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class TrainingAttendance(models.Model):
    _name = 'bista.training.attendance'
    _description = 'Training Attendance Master Description.'

    name = fields.Char(string='Name')
    trainee_id_code = fields.Char(string='Trainee ID')

    state = fields.Selection([('training', 'Training'), 
                            ('employeed', 'Employeed'),
                            ('rejected', 'Rejected')], 
                            default='training', string='State')

    attendance_line = fields.One2many('bista.training.attendance.line', 'attendance_id', string='Attendance Line')


class TrainingAttendanceLine(models.Model):
    _name = 'bista.training.attendance.line'
    _description = 'Training Attendance Master Date Description.'

    date_of_attendance = fields.Date(string='Date of Attendance',required=True, default=datetime.today())
    morning = fields.Boolean(string='Morning')
    evening = fields.Boolean(string='Evening')

    attendance_id = fields.Many2one('bista.training.attendance', string='Attendance ID')



