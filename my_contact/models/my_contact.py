from odoo import  fields, api, models

class MyContact(models.Model):
    _inherit = 'res.partner'
    wage = fields.Integer(string="Wage")
