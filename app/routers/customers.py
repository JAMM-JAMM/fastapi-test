from loguru import logger
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.utils.dbUtils import getSwitchDbConn
from app.sql.queries import customer_sql


router = APIRouter(
    prefix='/customers',
    tags=['customers']
)

@router.get('/')
async def read_customers():
    conn = getSwitchDbConn(dbName='SNOW')
    cursor = conn.cursor()
    cursor.execute(customer_sql)
    result = cursor.fetchone()
    print(result)
    return list(result)