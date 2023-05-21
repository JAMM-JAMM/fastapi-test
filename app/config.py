'''
01. System : 
02. Language : Python
03. Description : Environment Variables
---------------------------------------------------------------------
Author : Jaemin Sim
Licence : 
Version : 1.1
History Management : 
    - 2023-05-20 : 초기 작성, v 1.0
    - 2023-05-21 : ADD Customer Table Column Info, v 1.1
'''
import ast
from app.utils.commonUtils import getSecret

config = dict()

# Snowflake Connection
snowflake_secret_name = 'dev/snow-gc/conn'
snowflake_secret_value = ast.literal_eval(getSecret(p_secret_name=snowflake_secret_name))
config['snow_user'] = snowflake_secret_value['snow_user']
config['snow_password'] = snowflake_secret_value['snow_password']
config['snow_account'] = snowflake_secret_value['snow_account']
config['snow_warehouse'] = snowflake_secret_value['snow_warehouse']

# Snowflake Customer Table Columns
config['snow_cust_tb_cols'] = ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT')