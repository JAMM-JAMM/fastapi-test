customer_sql_get = '''
    SELECT
        C_CUSTKEY
        , C_NAME
        , C_ADDRESS
        , C_NATIONKEY
        , C_PHONE
        , C_ACCTBAL
        , C_MKTSEGMENT
        , C_COMMENT
    FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF100"."CUSTOMER"
    ORDER BY C_CUSTKEY
'''

customer_sql_post = '''
    SELECT
        C_CUSTKEY
        , C_NAME
        , C_ADDRESS
        , C_NATIONKEY
        , C_PHONE
        , C_ACCTBAL
        , C_MKTSEGMENT
        , C_COMMENT
    FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF100"."CUSTOMER"
    WHERE C_CUSTKEY=%s
'''