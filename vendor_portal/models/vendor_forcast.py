from odoo import models, fields
class VendorForecast(models.Model):

    _name = 'vendor.forecast'
    _description = 'Vendor Demand Forecast'

    product_id = fields.Many2one('product.product', string='Product')
    expected_quantity = fields.Integer(string='Expected Quantity')
    forecast_date = fields.Date(string='Forecast Date')
