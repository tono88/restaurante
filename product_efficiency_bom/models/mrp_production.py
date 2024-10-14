# product_efficiency_bom/models/mrp_production.py

from odoo import api, fields, models

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _get_moves_raw_values(self):
        moves_raw_values = super(MrpProduction, self)._get_moves_raw_values()
        for move_value in moves_raw_values:
            bom_line = self.bom_id.bom_line_ids.filtered(lambda l: l.id == move_value['bom_line_id'])
            if bom_line and bom_line.efficiency:
                efficiency_factor = bom_line.efficiency / 100.0 or 1.0
                move_value['product_uom_qty'] = move_value['product_uom_qty'] / efficiency_factor
        return moves_raw_values
