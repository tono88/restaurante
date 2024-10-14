# product_efficiency_bom/__manifest__.py

{
    'name': 'Product Efficiency in BoM',
    'version': '1.0',
    'summary': 'Gestiona la eficiencia de productos en las listas de materiales',
    'author': 'Tu Nombre',
    'website': 'https://tuweb.com',
    'category': 'Manufacturing',
    'depends': ['mrp'],
    'data': [
        'views/mrp_bom_views.xml',
        'views/mrp_bom_line_views.xml',
    ],
    'installable': True,
    'application': False,
}
