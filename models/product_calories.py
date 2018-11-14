# DietFacts application
from odoo import models, fields

# Extend product.template model with Calories

class DietFacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("Calories")
    serving_size = fields.Float("Serving size")
    last_updated = fields.Date("Last updated")
