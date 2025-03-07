from decimal import Decimal
from abc import ABC, abstractmethod
from typing import Dict, Optional, TypedDict, List, Any

from multiversx_sdk import MainnetEntrypoint, TestnetEntrypoint, DevnetEntrypoint, Account, Address, Mnemonic, Transaction, Message

from goat.classes.wallet_client_base import Balance, Signature, WalletClientBase
from goat.types.chain import Chain

from .types import MultiversXTransactionStatus, MultiversXTransaction


class MultiversXWalletClient(WalletClientBase, ABC):
    """Base class for MultiversX wallet implementations."""

    def get_chain(self) -> Chain:
        """Get the chain type for MultiversX."""
        return {"type": "multiversx"}

    @abstractmethod
    def get_address(self) -> str:
        """Get the wallet's public address."""
        pass

    @abstractmethod
    def sign_message(self, message: str) -> Signature:
        """Sign a message with the current account."""
        pass

    @abstractmethod
    def balance_of(self, address: str) -> Balance:
        """Get the EGLD balance of an address."""
        pass

    @abstractmethod
    def get_transaction_status(self, tx_hash: str) -> MultiversXTransactionStatus:
        """Get the transaction status from a transaction hash."""
        pass


    @abstractmethod
    def send_transaction(self, transaction: Transaction) -> Dict[str, str]:
        """Send a transaction on the MultiversX chain.

        Args:
            transaction: Transaction parameters

        Returns:
            Dict containing the transaction hash
        """
        pass


class MultiversXSeedphraseWalletClient(MultiversXWalletClient):
    """MultiversX implementation using a seedphrase."""

    def __init__(self, seed: str, network: str):
        """Initialize the MultiversX seedphrase wallet client.

        Args:
            seed: the seedphrase
            network: The network to connect to (mainnet, testnet, devnet)
        """
        super().__init__()
        mnemonic = Mnemonic(seed)
        self.account = Account.new_from_mnemonic(mnemonic.get_text())

        if network == "mainnet":
            self.entrypoint = MainnetEntrypoint()
        elif network == "devnet":
            self.entrypoint = DevnetEntrypoint()
        else:
            self.entrypoint = TestnetEntrypoint()

        self.api = self.entrypoint.create_network_provider()

    def get_address(self) -> str:
        """Get the wallet's public address."""
        return str(self.account.address)

    def sign_message(self, message: str) -> Signature:
        """Sign a message with the current account."""
        if not self.account:
            raise ValueError("No account connected")

        message = Message(data=message.encode(), address=self.account.address)
        message.signature = self.account.sign_message(message)
        return {"signature": message.signature.hex()}

    def balance_of(self, address: str) -> Balance:
        """Get the EGLD balance of an address."""
        address = Address.new_from_bech32(address)
        account = self.api.get_account(address=address)
        balance_lamports = account.balance
        # Convert lamports (1e18 lamports in 1 EGLD)
        return {
            "decimals": 18,
            "symbol": "EGLD",
            "name": "MultiversX",
            "value": str(balance_lamports / 10**18),
            "in_base_units": str(balance_lamports),
        }
    
    def get_transaction_status(self, tx_hash: str) -> MultiversXTransactionStatus:
        """Get the transaction status from a transaction hash."""
        transaction_status_obj = self.api.get_transaction(tx_hash).status
        return {
            "status": transaction_status_obj.status,
            "is_completed": transaction_status_obj.is_completed,
            "is_successful": transaction_status_obj.is_successful,
        }

    def send_transaction(self, transaction: MultiversXTransaction) -> Dict[str, str]:
        """Send a transaction on the MultiversX chain."""
        if not self.account:
            raise ValueError("No account connected")
        
        receiver = Address.new_from_bech32(transaction["receiver"])
        sender = self.account
        # Convert amount to reflect the 18 decimals in EGLD
        native_amount = int(Decimal(transaction.get("native_amount", 0)) * Decimal("1e18"))

        # Simple EGLD transfer
        if not transaction.get("contract"):
            factory = self.entrypoint.create_transfers_transactions_factory()

            sender.nonce = self.entrypoint.recall_account_nonce(sender.address)

            transaction = factory.create_transaction_for_transfer(
                sender=sender.address,
                receiver=receiver,
                native_amount=native_amount
            )

            transaction.nonce = sender.get_nonce_then_increment()

            transaction.signature = sender.sign_transaction(transaction)

            tx_hash = self.entrypoint.send_transaction(transaction)

            return {
                "transaction_hash": tx_hash
            }
        

def multiversx_wallet(seed: str, network: str) -> MultiversXSeedphraseWalletClient:
    """Create a new MultiversXSeedphraseWalletClient instance.

    Args:
        seed: the seedphrase of the wallet
        network: The network to connect to (mainnet, testnet, devnet)

    Returns:
        A new MultiversXSeedphraseWalletClient instance
    """
    return MultiversXSeedphraseWalletClient(seed, network)
