#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests

# 远程触发jenkins
REMOTE_URL = 'http://192.168.32.195'
PORT = '8080'
PROJECT_NAME = 'test_job'
TOKEN = '123456'
REMOTE_JOB_URL = '%s:%s/jenkins/job/%s/build?token=%s' % (REMOTE_URL, PORT, PROJECT_NAME, TOKEN)
REMOTE_JENKINS_LOGIN_URL = '%s:%s/jenkins/j_acegi_security_check' % (REMOTE_URL, PORT)


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
    url=REMOTE_JOB_URL
)

assert result.content == ''