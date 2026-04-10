import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";


patch(PosStore.prototype, {
    createNewOrder(data = {}) {

        const order = super.createNewOrder(data);

        // Set default preset "Dine In" for new orders
        const defaultPreset = this.models["pos.preset"].find(
            (preset) => preset.name === "Dine In"
        );

        if (defaultPreset) {
            order.update({
                preset_id: defaultPreset.id,
            });
        }

        return order;
    },
});
