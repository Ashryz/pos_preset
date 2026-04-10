import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";
import { makeAwaitable } from "@point_of_sale/app/store/make_awaitable_dialog";
import { _t } from "@web/core/l10n/translation";

patch(ControlButtons.prototype, {

    getPresetList() {
        const presets = this.pos.models["pos.preset"] || [];
        const currentOrder = this.currentOrder;
        // Handle both cases: preset_id as object with .id or as just an ID number
        const currentPresetId = currentOrder?.preset_id?.id || currentOrder?.preset_id;

        return presets.map((preset) => ({
            id: preset.id,
            label: preset.name,
            isSelected: currentPresetId && preset.id === currentPresetId,
            item: preset,
        }));
    },

    async clickPreset() {

        const presetList = this.getPresetList();

        if (!presetList.length) {
            return;
        }

        const payload = await makeAwaitable(this.dialog, SelectionPopup, {
            title: _t("Select Preset"),
            list: presetList,
        });

        if (payload) {
            this.pos.selectPreset(payload);
        }
    },
});
