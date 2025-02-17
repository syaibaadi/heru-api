import datetime
import uuid

import requests
from fastapi import APIRouter, Depends, HTTPException
from core.database import get_db
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import schemas
from modules.transaksi import crud
from modules.transaksi.models import Transaksi
from typing import List
import hmac
import hashlib
import json


router = APIRouter()

MIDTRANS_SERVER_KEY = "Basic U0ItTWlkLXNlcnZlci1fZnV1d1NVZWk2Y0UtUnBGOEdGVE51al8="
MIDTRANS_API_URL = "https://api.sandbox.midtrans.com/v1/payment-links"

@router.post("/create-payment-link")
async def create_payment_link(request_body: schemas.PaymentLinkRequest):
    try:
        # Generate unique order_id and payment_link_id
        # order_id = str(uuid.uuid4())[:8]  # Example unique ID
        # payment_link_id = order_id

        # Set expiry start_time and duration dynamically
        start_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+07:00")
        expiry_duration = 1  # Default duration in days
        expiry_unit = "days"

        # Build the payload
        payload = {
            "transaction_details": {
                "order_id": request_body.order_id,
                "gross_amount": request_body.price,  # Use price from the request body
                "payment_link_id": request_body.order_id
            },
            "customer_required": True,
            "credit_card": {
                "secure": True,
                "bank": "bca",
                "installment": {
                    "required": True,
                    "terms": {
                        "bni": [3, 6, 12],
                        "mandiri": [3, 6, 12],
                        "cimb": [3],
                        "bca": [3, 6, 12],
                        "offline": [6, 12]
                    }
                }
            },
            "usage_limit": 1,
            "expiry": {
                "start_time": start_time,
                "duration": expiry_duration,
                "unit": expiry_unit
            },
            "enabled_payments": [
                "credit_card",
                "bca_va",
                "bni_va",
                "indomaret"
            ],
            "item_details": [
                {
                    "id": str(request_body.wisata_id),
                    "name": request_body.nama_wisata,
                    "price": request_body.price,
                    "quantity": 1,
                    "brand": "Midtrans",
                    "category": "Wisata",
                    "merchant_name": "PT. Midtrans"
                }
            ],
            "customer_details": {
                "first_name": request_body.firstname,
                "last_name": request_body.lastname,
                "email": request_body.email,
                "phone": request_body.phone,
                "notes": "Thank you for your purchase. Please follow the instructions to pay."
            }
        }

        # Make the request to Midtrans API
        headers = {
            "Content-Type": "application/json",
            "Authorization": MIDTRANS_SERVER_KEY
        }

        response = requests.post(MIDTRANS_API_URL, json=payload, headers=headers)
        
        # Check for errors in response
        # if response.status_code != 201:
        #     raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# @router.post("/webhook")
# async def handle_webhook(payload: dict):
#     # Handle webhook logic here
#     print("Webhook received:", payload)
#     return {"status": "success"}

# def verify_signature(payload: dict, secret_key: str) -> bool:
#     # Mengambil signature_key dari payload dan membandingkannya dengan hasil HMAC SHA256
#     signature = payload.get('signature_key')
    
#     # Urutkan parameter sesuai dengan dokumentasi Midtrans
#     order_id = payload.get('order_id')
#     transaction_status = payload.get('transaction_status')
#     gross_amount = payload.get('gross_amount')  # pastikan gross_amount ada di payload
#     payment_type = payload.get('payment_type')  # pastikan payment_type ada di payload
    
#     # Membuat string untuk perhitungan HMAC
#     payload_str = f"{order_id}|{transaction_status}|{gross_amount}|{payment_type}"

#     # HMAC dengan secret_key
#     calculated_signature = hmac.new(
#         secret_key.encode('utf-8'),
#         payload_str.encode('utf-8'),
#         hashlib.sha256
#     ).hexdigest()

#     return calculated_signature

# class WebhookPayload(BaseModel):
#     order_id: str
#     transaction_status: str
#     gross_amount: int
#     payment_type: str
#     signature_key: str

# # Webhook handler
# @router.post("/webhook")
# async def handle_webhook(payload: WebhookPayload, db: Session = Depends(get_db)):
#     # Verify the signature first
#     secret_key = "SB-Mid-server-_fuuwSUei6cE-RpF8GFTNuj_"  # Ganti dengan server key Anda
#     # if not verify_signature(payload.dict(), secret_key):
#     #     raise HTTPException(status_code=400, detail="Invalid signature")

#     test = verify_signature(payload.dict(), secret_key)

#     # # Get the transaction from the database
#     # transaction = db.query(Transaksi).filter(Transaksi.order_id == payload.order_id).first()

#     # if not transaction:
#     #     raise HTTPException(status_code=404, detail="Transaction not found")

#     # # Update the transaction status based on the transaction status received from Midtrans
#     # if payload.transaction_status == "capture":
#     #     transaction.status = "PAID"
#     # elif payload.transaction_status == "deny" or payload.transaction_status == "expire":
#     #     transaction.status = "FAILED"
#     # elif payload.transaction_status == "pending":
#     #     transaction.status = "PENDING"
    
#     # # Commit the changes to the database
#     # db.commit()
#     # db.refresh(transaction)

#     # Return success response
#     # return {"status": "success", "order_id": payload.order_id, "new_status": transaction.status}
#     return {"signature": test}
