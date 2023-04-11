import json
from http.client import HTTPException
from typing import Annotated
from fastapi import APIRouter, Form, Request, Response, Header

import hashlib
import hmac

from models.message import MessageEvent

r = APIRouter()


def generate_hash_signature(
        payload: bytes,
        digest_method=hashlib.sha1):
    return hmac.new(payload, digest_method).hexdigest()


@r.post('/webhook')
async def get_all_messages(request: Request, x_hub_signature: str = Header(None)):
    try:
        payload = await request.body()
        decoded_payload = payload.decode("utf-8")
        print(type(decoded_payload), decoded_payload)
        for key in decoded_payload.keys():
            print(key, payload[key])
        signature = generate_hash_signature(payload)
        if x_hub_signature != f"sha1={signature}":
            raise HTTPException(status_code = 401, detail="Authentication error")
        return {
            "message": "Added"
        }
    except Exception as e:
        print(e)
        return {
            "message": "error"
        }


@r.get('/gupshup/{id}', response_model=dict)
def get_one_message(id):
    print(id)
    return {
        "wow": "works"
    }
