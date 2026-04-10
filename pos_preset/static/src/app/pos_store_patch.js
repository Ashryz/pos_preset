import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {

    selectPreset(preset) {
        const order = this.get_order();
        if (order) {
            order.update({
                preset_id: preset.id,
            });
        }
    },
});
