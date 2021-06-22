# -*- coding: utf-8 -*-

from odoo import models, fields

class TrainingStages(models.Model):
	_name = 'bista.training.stages'
	_description = 'Training Stages Master Description.'

	name = fields.Char(string='Stage Name')
	on_batch = fields.Boolean(string='Available on Batch')
	on_training_record = fields.Boolean(string='Available on Training Record')

	status = fields.Selection([('draft', 'Draft'), 
				('progress', 'Progress'),
				('done', 'Done')], 
				default='draft', string='Status')

	def action_pending_confirm(self):
		self.status = 'draft'

	def action_trainee_confirmed(self):
		self.status = 'progress'

	def action_training_started(self):
		self.status = 'progress'

	def action_training_complated(self):
		self.status = 'progress'

	def action_employed(self):
		self.status = 'done'

