from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = "pos.order"

    preset_id = fields.Many2one(
        'pos.preset',
        string='Preset',
        help='Preset type for this order (Dine In, Takeout, Delivery)'
    )


class PosPreset(models.Model):
    _name = 'pos.preset'
    _inherit = 'pos.load.mixin'
    _description = 'POS Preset'

    name = fields.Char(
        string='Name',
        required=True,
        translate=True,
        help='Display name of the preset (e.g., Dine In, Takeout, Delivery)'
    )

    def _loader_params_pos_preset(self):
        """
        Loader configuration for POS frontend
        Returns search parameters to load all presets into POS client
        """
        return {
            'search_params': {
                'domain': [],
                'fields': ['id', 'name'],
            }
        }

    @api.model
    def _get_all_presets(self):
        """
        Helper method to get all presets formatted for POS frontend
        """
        return self.search_read([], ['id', 'name'])


class PosSession(models.Model):
    _inherit = "pos.session"

    @api.model
    def _load_pos_data_models(self, config_id):
        res = super(PosSession, self)._load_pos_data_models(config_id)
        res.append('pos.preset')
        return res