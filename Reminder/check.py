#-*- coding:utf-8 -*-
import sqlite3
import sys
import time

import requests

from send_email import MailSender

reload(sys)
sys.setdefaultencoding('utf-8')   

def getHtml(url):
    delay = 1
    retry = 0
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    while retry < 3:
        try:
            r = requests.get(url,timeout = 10,headers = headers)
            return r.content
        except:
            retry += 1
            time.sleep(delay)
    return None

def check_and_send():
    ms = MailSender()
    conn = sqlite3.connect('./test.db')
    cur = conn.execute("select url,keyword,mail from info")
    for row in cur:
        url = row[0]
        keyword = row[1]
        mail = row[2]

        html = getHtml(url).encode("utf-8")

        if keyword in html:
            if ms.send_email([mail],u'【Reminder】**'+keyword+u'** 出现了!',keyword + "\nhas found in\n" + url):
                print mail + " Send Successfully!"

if __name__ == '__main__':
    ms = MailSender()
    url = "http://hp.whut.edu.cn/tzgg/" 
    keyword = u"校外门诊医疗费报销"
    mail = "nobystander96@gmail.com"
    html = getHtml(url).encode("utf-8")
    cnt = html.count(keyword)
    print cnt
    if cnt > 4:
        tries = 0
        while not ms.send_email([mail],u'【Reminder】**'+keyword+u'** 出现了!',keyword + "\nhas found in\n" + url):
            time.sleep(10)
            tries += 1
            if tries > 10:
                break

        if tries > 10:
            with open('log.txt','r') as f:
                f.write("Faild Send The E-Mail")
                f.close()
        else:
            print mail + " Send Successfully!"

    #check_and_send()
