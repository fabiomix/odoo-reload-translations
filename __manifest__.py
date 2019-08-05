# -*- coding: utf-8 -*-
{
    'name': "Reload translations",
    'summary': "Reload i18n files",
    'description': """
        Reload translation files of Odoo modules.
    """,

    'author': "fabiomix",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '10.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [

        # wizards
        'wizard/reload_translations.xml',

    ],

    'application': False,
    'installable': True
}
