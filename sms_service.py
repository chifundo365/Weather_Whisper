#!/usr/bin/python3
""" Sends sms to subcribers about that days weather """

from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(configuration))
send_transac_sms = sib_api_v3_sdk.SendTransacSms(sender="Weatherwh", recipient="265994396986", content="Weather details for today", type="transactional")

try:
    api_response = api_instance.send_transac_sms(send_transac_sms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalSMSApi->send_transac_sms: %s\n" % e)










