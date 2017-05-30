# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TemosPosto(models.Model):
    _inherit = 'res.partner'
    active = fields.Boolean(string='Ativo?', default=True)
    is_GasStation = fields.Boolean(string=u'É um posto de Gasolina', default=False)
    CódigoCGMP = fields.Char(string=u'Código do Posto', size=5)
    Latitude = fields.Char(string='Latitude')
    Longitude = fields.Char(string='Longitude')
