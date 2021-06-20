# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date

class Trainee(models.Model):
    _name = 'bista.trainee'
    _description = 'Trainee Master Description.'
    _sql_constraints = [
        ('trainee_id_unique', 'unique(trainee_id)', 'Trainee ID already exists!')
    ]

    name = fields.Char(string='Name', compute='_get_full_name')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    trainee_id = fields.Char(string='Trainee ID')
    emp_code = fields.Char(string='EMP Code')
    email = fields.Char(string='Personal Email ID', required=True)
    linkedin_url = fields.Char(string='Linked In Profile URL')
    gender = fields.Selection([('m', 'Male'), 
                                ('f', 'Female')], 
                                string='Gender', default='m', required=True)
    dob = fields.Date(string='DOB', required=True)
    date_of_joining = fields.Date(string='Date of Joining')

    def full_name(self):
        first_name = ''
        last_name = ''
        if self.first_name:
            first_name = self.first_name
        if self.last_name:
            last_name = self.last_name

        return first_name + ' ' + last_name
        
    def _get_full_name(self):
        for item in self:
            item.name = item.full_name()

    @api.constrains('dob')
    def _check_something(self):
        for record in self:
            if record.dob >= date.today():
                raise UserError(_("Invalid DOB!"))

