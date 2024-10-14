# product_efficiency_bom/__manifest__.py

{
    'name': 'Product Efficiency in BoM',
    'version': '1.0',
    'summary': 'Gestiona la eficiencia de productos en las listas de materiales',
    'description': """
        Permite establecer un porcentaje de eficiencia para los componentes en las listas de materiales, ajustando las cantidades en las órdenes de producción.
    """,
    'author': 'Tu Nombre',
    'website': 'https://tuweb.com',
    'category': 'Manufacturing',
    'depends': ['mrp'],
    'data': [
        'views/mrp_bom_line_views.xml',
    ],
    'installable': True,
    'application': False,
}
