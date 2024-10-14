from odoo import api, models

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _get_moves_raw_values(self):
        moves_raw_values = super()._get_moves_raw_values()
        for move_value in moves_raw_values:
            bom_line = self.bom_id.bom_line_ids.filtered(lambda l: l.id == move_value.get('bom_line_id'))
            if bom_line:
                efficiency = bom_line.efficiency or 100.0
                efficiency_factor = efficiency / 100.0
                if efficiency_factor > 0:
                    move_value['product_uom_qty'] = move_value['product_uom_qty'] / efficiency_factor
        return moves_raw_values
