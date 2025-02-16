from pydantic import BaseModel, EmailStr

class TransactionDetails(BaseModel):
    order_id: str
    gross_amount: int
    payment_link_id: str

class CreditCardInstallment(BaseModel):
    required: bool
    terms: dict

class CreditCard(BaseModel):
    secure: bool
    bank: str
    installment: CreditCardInstallment

class Expiry(BaseModel):
    start_time: str
    duration: int
    unit: str

class ItemDetails(BaseModel):
    id: str
    name: str
    price: int
    quantity: int
    brand: str
    category: str
    merchant_name: str

class CustomerDetails(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    notes: str

# class PaymentLinkRequest(BaseModel):
#     transaction_details: TransactionDetails
#     customer_required: bool
#     credit_card: CreditCard
#     usage_limit: int
#     expiry: Expiry
#     item_details: list[ItemDetails]
#     customer_details: CustomerDetails
#     custom_field1: str = None
#     custom_field2: str = None
#     custom_field3: str = None
class PaymentLinkRequest(BaseModel):
    wisata_id: int
    nama_wisata: str 
    price: int
    firstname: str 
    lastname: str 
    email: str 
    phone: str
    order_id: str
