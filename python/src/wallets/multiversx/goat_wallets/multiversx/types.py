from typing import TypedDict, List, Dict, Any
from typing_extensions import NotRequired


class MultiversXTransaction(TypedDict):
    receiver: str
    native_amount: NotRequired[int]  # Using int for bigint
    gas_limit: NotRequired[int]
    chain_id: NotRequired[str]
    function: NotRequired[str]
    contract: NotRequired[Any]
    arguments: NotRequired[List[Any]]
    token_transfers: NotRequired[List[Any]]
    data: NotRequired[bytes]

class MultiversXTransactionStatus(TypedDict):
    status: str
    is_completed: str
    is_successful: str