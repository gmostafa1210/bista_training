# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
from random import randint
import re

class Trainee(models.Model):
    _name = 'bista.trainee'
    _description = 'Trainee Master Description.'
    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Email already exists!'),
        ('linkedin_url_unique', 'unique(linkedin_url)', 'LinkedIn ID already exists!')
    ]

    name = fields.Char(string='Name', compute='_get_full_name')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    trainee_id_code = fields.Char(string='Trainee ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    emp_code = fields.Char(string='EMP Code')
    email = fields.Char(string='Personal Email ID', required=True)
    linkedin_url = fields.Char(string='Linked In Profile URL')
    gender = fields.Selection([('male', 'Male'), 
                                ('female', 'Female')], 
                                string='Gender', default='male', required=True)
    dob = fields.Date(string='DOB', required=True)
    date_of_joining = fields.Date(string='Date of Joining')
    location_id = fields.Many2one('bista.location', string='Location')
    designation_id = fields.Many2one('bista.trainee.role', string='Designation', required=True)
    img = fields.Binary(string='Profile Image', attachment=True)

    state = fields.Selection([('new', 'New'), 
                                ('training', 'Training'),
                                ('rejected', 'Rejected'),
                                ('employeed', 'Employeed')], 
                                default='new', string='State')

    related_user_id = fields.Many2one('res.users', string='Related User')


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
        if values.get('trainee_id_code', _('New')) == _('New'):
            values['trainee_id_code'] = self.env['ir.sequence'].next_by_code('bista.trainee.sequence') or _('New')
        return super(Trainee, self).create(values)


    def action_bista_training(self):
        self.state = 'training'

    def action_bista_employeed(self):
        self.env['hr.employee'].create(dict(
            name=self.name,
            image_1920 = self.img,
            job_title= self.designation_id.name,
            work_email = self.email,
            gender = self.gender,
        ))
        self.state = 'employeed'

    def action_bista_rejected(self):
        self.state = 'rejected'
        
    

