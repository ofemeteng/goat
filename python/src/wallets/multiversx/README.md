# MultiversX Wallet for GOAT SDK

A Python implementation of a MultiversX wallet for the GOAT SDK, providing secure key management and transaction signing capabilities.

## Installation

```bash
poetry add goat-sdk-wallet-multiversx
```

## Usage

```python
from goat_wallets.multiversx import multiversx_wallet

# Initialize wallet with seed phrase
wallet = multiversx_wallet(
    seed="${MULTIVERSX_WALLET_SEED}",  # Your MultiversX seed phrase
    network="${MULTIVERSX_NETWORK}", # The MultiversX network - "mainnet", "testnet" or "devnet"
)

# Get wallet address
address = wallet.get_address()

# Get EGLD balance
balance = await wallet.get_balance()

# Sign message
signature = await wallet.sign_message(
    message="your_message"
)

# Sign and send transaction
transaction_hash = await wallet.send_transaction(
    receiver="the receiver of the transaction"
)

# Get transaction status
status = await wallet.get_transaction_status(transaction_hash)
```

## Features

- Secure Key Management:
  - Seed phrase support
  - Address derivation
  
- Transaction Operations:
  - Transaction signing
  - Transaction sending
  - Status tracking
  - Signature verification
  
- Balance Management:
  - EGLD balance queries
  - Token account balance
  
- Network Support:
  - Mainnet
  - Testnet
  - Devnet

## License

This project is licensed under the terms of the MIT license.
