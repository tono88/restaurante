from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    efficiency = fields.Float(
        string='Eficiencia (%)',
        default=100.0,
        help='Porcentaje de eficiencia del componente. Un valor menor a 100% indica merma.'
    )

    @api.constrains('efficiency')
    def _check_efficiency(self):
        for line in self:
            if not (0 < line.efficiency <= 100):
                raise ValidationError('La eficiencia debe estar entre 0 y 100%.')
