# -*- coding: utf-8 -*-

{
    'name': "Pos Preset",

    'summary': """POS Preset Selection - Dine In, Takeout, Delivery""",

    'description': """
        Add preset selection functionality to POS orders.
        Allows selection of Dine In, Takeout, or Delivery presets.
        Integrates as a control button in the product screen, following Odoo 18 POS architecture.
    """,

    'author': "Tarek Ashry",

    'version': '18.0.1.0',
    'category': 'Sales',

    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/pos_preset.xml',
        'views/pos_order_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_preset/static/src/app/pos_store_create_order_patch.js',
            'pos_preset/static/src/app/pos_store_patch.js',
            'pos_preset/static/src/app/screens/product_screen/control_buttons/control_buttons_method_patch.js',
            'pos_preset/static/src/app/screens/product_screen/control_buttons/preset_button_template.xml',
            'pos_preset/static/src/app/screens/receipt_screen/receipt_screen.js',
            'pos_preset/static/src/app/screens/receipt_screen/receipt/receipt_header/receipt_header.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
