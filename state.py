from typing import TypedDict

class CustomerState(TypedDict):

    customer_name: str

    query: str

    intent: str

    retrieved_context: str

    department_response: str

    approval_required: bool

    approved: bool

    final_response: str