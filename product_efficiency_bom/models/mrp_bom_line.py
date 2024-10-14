# product_efficiency_bom/models/mrp_bom_line.py

from odoo import api, fields, models

class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    efficiency = fields.Float(
        string='Eficiencia (%)',
        default=100.0,
        help='Porcentaje de eficiencia del componente. Un valor menor a 100% indica merma.'
    )
