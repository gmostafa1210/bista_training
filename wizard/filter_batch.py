# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class FilterBatch(models.TransientModel):
    _name = 'bista.filter.batch'
    _description = 'Filter Batch Description.'
    
    name = fields.Char(string='Batch Name')

    def get_bista_filter_batch(self):
        batch_list = []

        batch_filter_data = self.env['bista.batch'].search([('name','=',self.name)])
        for data in batch_filter_data:
            batch_list.append(data.id)

        return{
            'name': 'Filter Batch',
            'type': 'ir.actions.act_window',
            'res_model': 'bista.batch',
            'view_mode': 'tree,form',
            'domain': [('id','in',batch_list)]
        }