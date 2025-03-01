
<div align="center">
<img src="https://github.com/user-attachments/assets/5fc7f121-259c-492c-8bca-f15fe7eb830c" alt="GOAT" width="100px" height="auto" style="object-fit: contain;">
</div>

# Using Crossmint Smart Wallets
## 🚀 Quickstart

This example demonstrates how to use GOAT to **use a [Crossmint Smart Wallet](https://www.crossmint.com/products/embedded-wallets-as-a-service)**. This example uses **Ethereum Sepolia** but you can implement it with any other EVM network supported by Crossmint Smart Wallets by changing the chain and RPC URL.

You can use this example with any other agent framework and protocols of your choice.

## Setup
1. Clone the repository:
```bash
git clone https://github.com/goat-sdk/goat.git && cd goat
```

2. Run the following commands from the `typescript` directory:
```bash
cd typescript
pnpm install
pnpm build
```

3. Go to the example directory:
```bash
cd examples/by-wallet/crossmint-smart-wallets
```

4. Copy the `.env.template` and populate with your values:
```bash
cp .env.template .env
```
- `OPENAI_API_KEY`
- `RPC_PROVIDER_URL`
- `CROSSMINT_STAGING_API_KEY`
- `SMART_WALLET_ADDRESS` - You will generate it with the create-smart-wallet.ts script
- `SIGNER_WALLET_SECRET_KEY` - The wallet address that will act as a signer for the smart wallet
- `SIGNER_WALLET_ADDRESS`

5. Create a smart wallet.
```
pnpm ts-node create-smart-wallet.ts
```

6. Copy the custodial wallet address and add it to the `.env` file.
```
SMART_WALLET_ADDRESS=<your custodial wallet address>
```

## Usage
1. Run the interactive CLI:
```bash
pnpm ts-node index.ts
```

<footer>
<br/>
<br/>
<div>
  <img src="https://github.com/user-attachments/assets/4821833e-52e5-4126-a2a1-59e9fa9bebd7" alt="GOAT" width="100%" height="auto" style="object-fit: contain; max-width: 800px;">

<div>
</footer>
