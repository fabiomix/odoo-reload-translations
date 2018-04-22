# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

import pprint
import logging
_logger = logging.getLogger(__name__)


class ReloadTranslations(models.TransientModel):
	_name = 'wizard.reload_translations'


	def get_language_list(self):
		active_languages = self.env['res.lang'].search([
				('translatable', '=', True), 
				('active', '=', True)
			])

		return [(l.code, l.name) for l in active_languages]

	
	lang = fields.Selection(
			selection=get_language_list, 
			string="Language",
			required=True
		)

	module_ids = fields.Many2many(
			comodel_name='ir.module.module', 
			relation='wizard_reload_translations_module_rel', 
			column1='wizard_id', 
			column2='module_id',
			string='Modules', 
			domain=[('state','=','installed')]
		)


	def do_reload_translations(self):
		pass
