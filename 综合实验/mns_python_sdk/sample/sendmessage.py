#!/usr/bin/env python
#coding=utf8

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
from sample_common import MNSSampleCommon
from mns.account import Account
from mns.queue import *


def my_send_msg(num):

    # 从sample.cfg中读取基本配置信息
    ## WARNING： Please do not hard code your accessId and accesskey in next line.(more information: https://yq.aliyun.com/articles/55947)
    accid, acckey, endpoint, token = MNSSampleCommon.LoadConfig()

    # 初始化 my_account, my_queue
    my_account = Account(endpoint, accid, acckey, token)
    queue_name = "MyQueue1"
    my_queue = my_account.get_queue(queue_name)

    try:
        # msg_body = "I am test message %s." % i
        msg_body = num
        msg = Message(msg_body)
        re_msg = my_queue.send_message(msg)
        # print
        # "Send Message Succeed! MessageBody:%s MessageID:%s" % (msg_body, re_msg.message_id)
    except MNSExceptionBase, e:
        if e.type == "QueueNotExist":
            print
            "Queue not exist, please create queue before send message."
            sys.exit(0)
        print
        "Send Message Fail! Exception:%s\n" % e
