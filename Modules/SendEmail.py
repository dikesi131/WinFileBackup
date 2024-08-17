########################################################################
 # $ @Author: d1k3si
 # $ @Date: 2024-08-08 18:25:30
 # $ @LastEditors: d1k3si
 # $ @LastEditTime: 2024-08-08 20:00:24
 # $ @email:2098415680@qq.com
 # $ @Copyright (c) 2024 by d1k3si
########################################################################
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from pathlib import Path
import sys
from .GlobalVar import GetVar

# 发送邮件
def SendEmail(message=f'{Path(sys.argv[0]).name}运行完毕,文件已备份完成'):
    # code为QQ邮箱开启SMTP服务后的授权码
    SenderConfig={'email': GetVar('Config')['email'],'code':GetVar('Config')['PassCode']}
    # from-->发件人
    # to-->收件人
    # subject:主题
    EmailContent={'from':GetVar('Config')['email'],'to':GetVar('Config')['SendTo'],
                 'subject':'FileBackup Status'}
    # 电子邮件内容设置
    msg = MIMEMultipart()
    msg['From'] = EmailContent['from']
    msg['To'] = Header(EmailContent['to'],'utf-8')
    msg['Subject'] = Header(EmailContent['subject'],'utf-8')
    
    # 添加正文
    msg.attach(MIMEText(message, 'plain'))
    
    # 创建 SMTP 客户端
    try:
        # 链接邮箱服务器，SMTP默认端口为25
        with smtplib.SMTP('smtp.qq.com', GetVar('Config')['port']) as smtp:
            smtp.starttls()
            smtp.login(SenderConfig['email'], SenderConfig['code'])
            smtp.send_message(msg)
        GetVar('g_logger').info("[SUCCESS]邮件发送成功")
    except Exception as e:
        GetVar('g_logger').error(f"[ERROR]邮件发送失败: {e}")