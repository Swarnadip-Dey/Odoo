from odoo import models, fields

class VendorAdjustment(models.Model):
    _name = 'vendor.adjustment'
    _description = 'Vendor Adjustment Request'

    order_id = fields.Many2one('sale.order', string='Order', required=True)
    adjustment_detail = fields.Text(string='Adjustment Details', required=True)
    comment = fields.Text(string='Additional Comments')