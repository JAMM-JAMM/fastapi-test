customer_sql = '''
    SELECT
        C_CUSTKEY
        , C_NAME
        , C_ADDRESS
        , C_NATIONKEY
        , C_PHONE
        , C_ACCTBAL
        , C_MKTSEGMENT
        , C_COMMENT
    FROM "SNOWFLAKE_SAMPLE_DATA"."TPCH_SF1"."CUSTOMER"
'''