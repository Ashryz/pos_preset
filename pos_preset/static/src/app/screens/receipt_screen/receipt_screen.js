import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";

patch(PosStore.prototype, {
    getReceiptHeaderData(order) {
        console.log(order)
        return {
            ...super.getReceiptHeaderData(...arguments),
            preset_id : order.preset_id,
        };
    },
});