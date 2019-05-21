# -*- coding: utf-8 -*-
"""
Created on 2018/7/26

@author: xing yan
"""

query_cust_info_sql = """
                        SELECT T.ID_NO,
                               T.CUST_NAME,
                               H.CUST_NO,
                               T.MOBILE,
                               H.HBONE_NO,
                               T.BANK_ACCT,
                               T.BANK_REGION_NAME
                          FROM TP_ACCT_DEAL_REC T, AC_TX_HBONE H
                         WHERE T.TX_CODE = '520019'
                           AND T.HBONE_NO = H.HBONE_NO
                           AND H.CUST_NO  like :cust_no
                         ORDER BY H.HBONE_NO DESC
                         """


query_notify_deal_order_sql = """
                                SELECT D.DEAL_NO,
                                       D.FUND_CODE,
                                       D.FUND_NAME,
                                       D.TX_ACCT_NO,
                                       D.TX_APP_FLAG,
                                       D.NOTIFY_SUBMIT_FLAG,
                                       P.PAYMENT_TYPE,
                                       P.TX_PMT_FLAG,
                                       D.QUALIFICATION_TYPE,
                                       D.DUALENTRY_STATUS,
                                       D.DUALENTRY_FINISH_DTM,
                                       D.DUALENTRY_INTERPOSE_FLAG,
                                       D.CALLBACK_STATUS,
                                       D.CALLBACK_FINISH_DTM,
                                       D.CALLBACK_INTERPOSE_FLAG,
                                       D.CALMDTM_INTERPOSE_FLAG,
                                       D.ASSETCERTIFICATE_STATUS,
                                       D.ASSET_INTERPOSE_FLAG,jt
                                       D.SUBMIT_TA_DT
                                  FROM HIGH_DEAL_ORDER_DTL D, PAYMENT_ORDER P
                                 WHERE D.NOTIFY_SUBMIT_FLAG = '0'
                                   AND D.DEAL_NO = P.DEAL_NO
                                   AND D.TX_APP_FLAG = '0'
                                   AND P.TX_PMT_FLAG = '2'
                                   AND D.FUND_CODE = :fund_code
                                 ORDER BY D.FUND_CODE
                                 """

