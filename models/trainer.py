# -*- coding: utf-8 -*-

from odoo import models, fields

class Trainer(models.Model):
    _name = 'bista.trainer'
    _description = 'Trainer Master Description.'

    name = fields.Char(string='Name', compute='_get_full_name')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    img = fields.Binary(string='Profile Image', attachment=True)
    
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
