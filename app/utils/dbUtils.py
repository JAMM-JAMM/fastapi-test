from loguru import logger
import snowflake.connector
from app.config import config

class SnowConn:
    def __init__(self):
        try:
            self.conn = snowflake.connector.connect(
                    user=config['snow_user'],
                    password=config['snow_password'],
                    account=config['snow_account'],
                    warehouse=config['snow_warehouse']
                )
        except Exception as e:
            logger.error(f'[DEBUG] Snowflake Connection Error - {e}')
    
    def getDbConn(self):
        return self.conn

def getSwitchDbConn(p_db_name):

    logger.debug(f'[DEBUG] DB Name : {p_db_name}')

    if p_db_name == 'SNOW':
        clsDb = SnowConn()
        conn = clsDb.getDbConn()
        return conn