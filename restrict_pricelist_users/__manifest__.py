# -*- coding: utf-8 -*-
{
    'name': 'Restrict Pricelist Users',
    'description': "This module restricts user access to specific pricelists in Odoo, "
                   "ensuring that only authorized users can view or manage pricelist data.",
    'version': '18.0.1',
    'author': 'Banica Daniel',
    'maintainers': ["banica-dev"],
    'license': 'OPL-1',
    'price': 10,
    'currency': "EUR",
    'installable': True,
    'data': [
        'views/product_pricelist_views.xml',
        'security/pricelist_rules.xml',
    ],
    'images': ['static/description/banner.png'],
    'category': 'Sale',
    'depends': ['base', 'sale'],
}
