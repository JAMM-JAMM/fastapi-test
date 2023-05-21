from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.utils.apiUtils import getCustomers, postCustomers


router = APIRouter(
    prefix='/customers',
    tags=['customers']
)

@router.get('/')
def read_customers():
    return getCustomers()

@router.post('/{custkey}')
def read_customers_by_custkey(custkey: int):
    return postCustomers(p_custkey=custkey)