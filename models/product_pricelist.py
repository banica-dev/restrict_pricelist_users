from odoo import fields, models

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    allowed_users = fields.Many2many(
        'res.users',
        string='Allowed Users',
        help="Users allowed to access this pricelist"
    )