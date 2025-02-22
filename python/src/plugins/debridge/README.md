# deBridge Plugin for GOAT SDK

A plugin for the GOAT SDK that provides access to deBridge Liquidity Network (DLN) functionality.

## Installation

```bash
# Install the plugin
poetry add goat-sdk-plugin-debridge


```

## Usage

```python
from goat_plugins.debridge import debridge, DebridgePluginOptions

# Initialize the plugin
options = DebridgePluginOptions()
plugin = debridge(options)

# Get order data
order_data = await plugin.get_order_data(
    id="0x81fbb0ed8209eb57d084aee1986c00e597c1e1ec6bb93bc4dbe97266ca0398fb"
)

# Get supported chains
chains = await plugin.get_supported_chains()

# Get order IDs
order_IDs = await plugin.get_order_IDs(
    hash="0xbe9071de34de9bd84a52039bc4bc6c8229d4bd65127d034ffc66b600d8260276" # Hash of the creation transaction
)
```

## Features

- DLN
    - Create order transaction
    - Get order data
    - Get order status
    - Get order IDs
    - Cancel order
    - Cancel external call
- Utils
    - Get supported chains
    - Get token list
- Single Chain Swap
    - Estimation
    - Transaction

## License

This project is licensed under the terms of the MIT license.
