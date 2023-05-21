'''
01. System : 
02. Language : Python
03. Description : API Util Functions
---------------------------------------------------------------------
Author : Jaemin Sim
Licence : 
Version : 1.0
History Management : 
    - 2023-05-21 : 초기 작성, v 1.0
'''
import time
from loguru import logger
from app.config import config
from app.utils.commonUtils import decorate
from app.sql.queries import customer_sql_get, customer_sql_post
from app.utils.dbUtils import getSwitchDbConn


def getCustomers():
    '''
    TBD
    '''
    result = list()
    snow_conn = getSwitchDbConn(p_db_name="SNOW")
    with snow_conn.cursor() as cursor:
        try:
            start_time = time.time()
            logger.debug(f'[DEBUG] Snowflake Execute SQL : {customer_sql_get}')
            cursor.execute(customer_sql_get)
            end_time = time.time()
            logger.debug('[DEBUG] Snowflake Query Execution Time {:.5f}s'.format(end_time - start_time))
        except Exception as e:
            logger.error(f'[ERROR] Snowflake Query Execution Error - {e}')
        else:
            rows = cursor.fetchmany(size=10)
            for row in rows:
                tmp = dict(zip(config['snow_cust_tb_cols'], row))
                result.append(tmp)
        finally:
            snow_conn.close()
            logger.debug('[DEBUG] Snowflake Connection Close')
    return result

def postCustomers(p_custkey: int):
    '''
    TBD
    '''
    logger.debug(f'[DEBUG] Parameter : p_custkey={p_custkey}')
    result = list()
    snow_conn = getSwitchDbConn(p_db_name="SNOW")
    with snow_conn.cursor() as cursor:
        try:
            start_time = time.time()
            logger.debug(f'[DEBUG] Snowflake Execute SQL : {customer_sql_post}')
            cursor.execute(customer_sql_post, (str(p_custkey),))
            end_time = time.time()
            logger.debug('[DEBUG] Snowflake Query Execution Time {:.5f}s'.format(end_time - start_time))
        except Exception as e:
            logger.error(f'[ERROR] Snowflake Query Execution Error - {e}')
        else:
            row = cursor.fetchall()
            tmp = dict(zip(config['snow_cust_tb_cols'], row[0]))
            result.append(tmp)
        finally:
            snow_conn.close()
            logger.debug('[DEBUG] Snowflake Connection Close')
    return result