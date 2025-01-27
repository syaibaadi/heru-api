import datetime
import uuid

import requests
from fastapi import APIRouter, Depends, HTTPException
from . import schemas
from typing import List

router = APIRouter()

MIDTRANS_SERVER_KEY = "Basic U0ItTWlkLXNlcnZlci1fZnV1d1NVZWk2Y0UtUnBGOEdGVE51al8="
MIDTRANS_API_URL = "https://api.sandbox.midtrans.com/v1/payment-links"

@router.post("/create-payment-link")
async def create_payment_link(request_body: schemas.PaymentLinkRequest):
    try:
        # Generate unique order_id and payment_link_id
        order_id = str(uuid.uuid4())[:8]  # Example unique ID
        payment_link_id = order_id

        # Set expiry start_time and duration dynamically
        start_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+07:00")
        expiry_duration = 1  # Default duration in days
        expiry_unit = "days"

        # Build the payload
        payload = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": request_body.price,  # Use price from the request body
                "payment_link_id": payment_link_id
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

@router.post("/webhook")
async def handle_webhook(payload: dict):
    # Handle webhook logic here
    print("Webhook received:", payload)
    return {"status": "success"}
