import sys
sys.path.insert(0, 'LLM policy generator\\api\\')
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Response
from schemas.schemas import UserDetails
from services.policy_generator import policy_suggestion

router = APIRouter()

@router.post('/goml/LLM marketplace/policy_generator', status_code=201)
def policy_detials(model:UserDetails):
    try:
        obj = policy_suggestion(model.__dict__)
        return obj
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))