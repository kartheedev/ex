from odoo import fields, models

class travel_model(models.Model):
    _name = 'travel.model'

    name = fields.Char('Name')
