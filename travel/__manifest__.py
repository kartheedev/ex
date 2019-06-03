{
    'name': 'Travel',
    'version': '1.0',
    'depends': ['base'],
    'data': [
                'security/ir.model.access.csv',
                'view/travel_view.xml',
            ],

    # 'qweb': [
    #     'static/src/xml/reminder_topbar.xml', ],
    # 'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': True,
    'application': False,
}
