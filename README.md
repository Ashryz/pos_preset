# POS Preset

A simple Odoo 18 Point of Sale addon that allows users to select order presets during checkout.

## Features

- **Preset Selection**: Choose between Dine In, Takeout, or Delivery options for each POS order
- **Frontend Integration**: Preset button integrated into the product screen
- **Order Tracking**: Each order stores its selected preset type
- **Backend Support**: Full backend management and data persistence


## Usage

After installation, a **Preset** button will appear in the POS product screen. Users can:

1. Click the Preset button during order creation
2. Select a preset type (Dine In, Takeout, or Delivery)
3. Continue with the normal checkout process

The selected preset is automatically saved with the order and can be viewed in the order details.

## Requirements

- Odoo 18
- Point of Sale module

## Author

Tarek Ashry

## License

AGPL-3
