{
    'name': 'Product Image in so & mo',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Adds product image to sale order lines and manufacturing orders',
    'author': 'Tag Technology',
    'company': 'Tag Technology',
    'depends': ['sale', 'mrp', 'product'],
    'data': [
        'views/sale_order_line_views.xml',
        'views/mrp_production_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
