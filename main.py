import json
from http.client import HTTPException
from typing import Annotated
from fastapi import APIRouter, Form, Request, Response, Header
import requests

import hashlib
import hmac

from models.message import MessageEvent

r = APIRouter()


def generate_hash_signature(
        payload: bytes,
        digest_method=hashlib.sha1):
    print("control over here")
    return hmac.new(payload, digest_method).hexdigest()


@r.post('/webhook')
async def get_all_messages(request: Request, x_hub_signature: str = Header(None)):
    try:
        r = requests
        payload = await request.body()
        decoded_payload = json.loads(payload.decode("utf-8"))
        # print(type(decoded_payload), decoded_payload)
        for key in decoded_payload.keys():
            print(key, decoded_payload[key])
        print("control over here")
        signature = generate_hash_signature(payload)
        if x_hub_signature != f"sha1={signature}":
            raise HTTPException(status_code = 401, detail="Authentication error")
        print("control over here")
        r = requests.post(
            "https://script.google.com/macros/s"
            "/AKfycbxlAvm1e3AzOY19jxND77mSRQkaYi6tLd9JcORlzzul_P8W6Zk1dToZixANbnKp9NRi/exec",
            data = decoded_payload
                          )
        print(r.text)
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
