#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import sys

# 远程触发jenkins
REMOTE_URL = 'http://192.168.32.195'
PORT = '8080'
PROJECT_NAME = 'config_sosotest_url'
TOKEN = '123456'
ARGV = sys.argv[1]
REMOTE_JOB_URL = '%s:%s/jenkins/job/%s/build?token=%s' % (REMOTE_URL, PORT, PROJECT_NAME, TOKEN)
REMOTE_JENKINS_LOGIN_URL = '%s:%s/jenkins/j_acegi_security_check' % (REMOTE_URL, PORT)
ARGV_REMOTE_JOB_URL = '%s:%s/jenkins/job/%s/buildWithParameters?token=%s&vm_ip=%s' % (REMOTE_URL, PORT, PROJECT_NAME, TOKEN, ARGV)

print ARGV_REMOTE_JOB_URL
session = requests.session()
bady = {
    'j_username': 'ync',
    'j_password': 'ync',
    'from': '/jenkins/',
    'Submit': '登录'
}

# 关闭重定向，登录获取token
response = session.post(
    url=REMOTE_JENKINS_LOGIN_URL,
    data=bady,
    allow_redirects=False
)

result = session.get(
    url=ARGV_REMOTE_JOB_URL
)
print result.content
assert result.content == ''