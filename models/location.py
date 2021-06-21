# -*- coding: utf-8 -*-

from odoo import models, fields

class BistaLocation(models.Model):
    _name = 'bista.location'
    _description = 'Location Master Description.'

    name = fields.Char(string='Location Name', required=True)
    street_1 = fields.Char(string='Street 1')
    street_2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country', required=True)

	