# debridge Plugin for GOAT SDK

A plugin for the GOAT SDK that provides debridge functionality.

## Installation

```bash
# Install the plugin
poetry add goat-sdk-plugin-debridge


```

## Usage

```python
from goat_plugins.debridge import debridge, DebridgePluginOptions

# Initialize the plugin
options = DebridgePluginOptions(
    api_key="your-api-key"
)
plugin = debridge(options)
```

## Features

- Example query functionality
- Example action functionality
- Chain-agnostic support

## License

This project is licensed under the terms of the MIT license.
