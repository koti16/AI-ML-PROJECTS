from typing import List, Optional
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    description: str = Field(description="Name or concise description of the item/service")
    quantity: int = Field(description="Quantity purchased", default=1)
    unit_price: float = Field(description="Price per single unit")
    total_amount: float = Field(description="Total calculated cost for this line item")


class InvoiceDocument(BaseModel):
    vendor_name: str = Field(description="Name of the business issuing the document")
    invoice_number: Optional[str] = Field(description="Invoice or receipt reference ID", default=None)
    transaction_date: Optional[str] = Field(description="Date in YYYY-MM-DD format", default=None)
    line_items: List[LineItem] = Field(description="List of purchased individual line items")
    subtotal: float = Field(description="Subtotal amount before tax or discounts")
    tax_amount: float = Field(description="Total tax charged", default=0.0)
    total_amount: float = Field(description="Final grand total amount paid or due")
    is_paid: bool = Field(description="True if payment status is marked complete/paid")