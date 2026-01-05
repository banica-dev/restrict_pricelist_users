# -*- coding: utf-8 -*-
{
    'name': 'Restrict Pricelist Users',
    'description': "This module restricts user access to specific pricelists in Odoo, "
                   "ensuring that only authorized users can view or manage pricelist data.",
    'version': '19.0.0.1',
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
    'images': [
        'static/description/banner.png',
        'static/description/pricelist_allowed_users.png',
        'static/description/user_groups.png',
    ],
    'category': 'Sale',
    'depends': ['base', 'sale'],
}
