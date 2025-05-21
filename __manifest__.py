# -*- coding: utf-8 -*-
{
    'name': 'Restrict Pricelist Users',
    'description': "This module restricts user access to specific pricelists in Odoo, "
                   "ensuring that only authorized users can view or manage pricelist data.",
    'version': '1.0.1',
    'author': 'Banica Daniel',
    'maintainers': ["banica-dev"],
    'license': 'OPL-1',
    'installable': True,
    'data': [
        'views/product_pricelist_views.xml',
        'security/pricelist_rules.xml',
    ],
    'category': 'Sale',
    'depends': ['base', 'sale'],
    'price': 15.00,
    'currency': 'USD',
}
