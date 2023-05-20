'''
01. System : 
02. Language : Python
03. Description : Environment Variables
---------------------------------------------------------------------
Author : Jaemin Sim
Licence : Kyobobook
Version : 1.0
History Management : 
    - 2023-05-20 : 초기 작성, v 1.0
'''
import ast
from app.utils.commonUtils import get_secret

config = dict()

# Snowflake Connection
snowflake_secret_name = 'dev/snow-gc/conn'
snowflake_secret_value = ast.literal_eval(get_secret(p_secret_name=snowflake_secret_name))
config['snow_user'] = snowflake_secret_value['snow_user']
config['snow_password'] = snowflake_secret_value['snow_password']
config['snow_account'] = snowflake_secret_value['snow_account']
config['snow_warehouse'] = snowflake_secret_value['snow_warehouse']