{
    'name': 'Vendor Self-Service Portal',
    'version': '16.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Module for vendor self-service functionalities.',
    'description': """
        This module provides a portal for vendors to:
        - View demand forecasts
        - Submit order adjustment requests
    """,
    'author': 'sd',
    'depends': ['base', 'sale', 'website'],
    'data': [
        'views/vendor_forcast.xml',
        'models/vendor_forcast.py',
        'models/vendor_adjustment.py',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}