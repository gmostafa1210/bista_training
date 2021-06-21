# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
import re
from random import randint

class Trainee(models.Model):
    _name = 'bista.trainee'
    _description = 'Trainee Master Description.'
    _sql_constraints = [
        ('trainee_id_code_unique', 'unique(trainee_id_code)', 'Trainee ID already exists!')
    ]

    name = fields.Char(string='Name', compute='_get_full_name')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    trainee_id_code = fields.Char(string='Trainee ID', readonly=True)
    emp_code = fields.Char(string='EMP Code')
    email = fields.Char(string='Personal Email ID', required=True)
    linkedin_url = fields.Char(string='Linked In Profile URL')
    gender = fields.Selection([('male', 'Male'), 
                                ('female', 'Female')], 
                                string='Gender', default='m', required=True)
    dob = fields.Date(string='DOB', required=True)
    date_of_joining = fields.Date(string='Date of Joining')
    location_id = fields.Many2one('bista.location', string='Location')
    designation_id = fields.Many2one('bista.trainee.role', string='Designation', required=True)
    img = fields.Binary(string='Profile Image', attachment=True)
    status = fields.Selection([('new', 'New'), 
                                ('training', 'Training'),
                                ('rejected', 'Rejected'),
                                ('employeed', 'Employeed')], string='Status')


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

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise UserError('Not a valid Email!')

    @api.constrains('dob')
    def _check_dob(self):
        for record in self:
            if record.dob >= date.today():
                raise UserError(_("Invalid DOB!"))

    @api.model
    def create(self, values):
        prefix = 'TRN'
        val = randint(100000, 999999)
        data = prefix + str(val)
        values['trainee_id_code'] = data
        return super(Trainee, self).create(values)

    # @api.model 
    # def create(self, values):
    #     prefix = "TRN" 
    #     last_rec = self.env['bista.trainee'].search([], order='id desc', limit=1)
    #     val = last_rec.id
    #     if val == False:
    #         val = 1
    #     else:
    #         val += 1
    #     n = 7-(len(str(val)))
    #     values['trainee_id_code'] = prefix + ('0'*n) + str(val)
    #     return super(Trainee, self).create(values)
    

