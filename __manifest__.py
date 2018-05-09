# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HRT Theme',
    'summary': '',
    'description': '',
    'category': 'Theme',
    'sequence': 900,
    'version': '1.0',
    'depends': ['website','sale'],
    'data': [
        'data/data.xml',
        'views/templates.xml',
        'XML/footer_logo.xml',
        'XML/website_sale.products_item.xml',
        'XML/snippets.xml',
        'XML/header.xml',
        'XML/website_sale.confirmation.xml',
        'XML/signup.xml',
        'XML/address_management.xml',
        'XML/portal_layout.xml',
        'views/pages.xml',
    ],
    'images': ['static/img/logo.png'],
    'application': True,
}
