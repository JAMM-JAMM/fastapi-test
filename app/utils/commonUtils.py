'''
01. System : 
02. Language : Python
03. Description : Common Util Functions
---------------------------------------------------------------------
Author : Jaemin Sim
Licence : 
Version : 1.0
History Management : 
    - 2023-05-20 : 초기 작성, v 1.0
'''
import time
import boto3
import functools
from loguru import logger
from botocore.exceptions import ClientError


def decorate(original_func):
    @functools.wraps(original_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        original_func(*args, **kwargs)
        end = time.time()
        logger.debug('[DEBUG] Duration of time {:.5f}s'.format(end - start))
    return wrapper

def getSecret(p_secret_name: str, p_region_name="ap-northeast-2") -> str:
    '''
    Get AWS Secrets Manager Value
    :param p_secret_name (str): AWS Secrets Manager - Secret name EX) dev/snow-gc/conn
    :param p_region_name(str): AWS Region name - Default EX) ap-northeast-2
    :return secret_string(str): AWS Secret Value Response 
    '''

    secret_name = p_secret_name
    region_name = p_region_name

    logger.debug(f'Secret Name : {secret_name}, Region Name : {region_name}')

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        secret_string = get_secret_value_response['SecretString']
        logger.debug(f'[DEBUG] Get Secret Value from AWS Secrets Manager - {secret_name}')
        return secret_string
    except ClientError as e:
        logger.error(f'[ERROR] Get Secret Value from AWS Secrets Manager - {e}')