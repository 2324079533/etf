import requests
from src.config import config

class Notifier:
    @staticmethod    @静态方法
    def send_wechat发送微信(content: str):内容：字符串):
        if not config.wechat_webhook:        如果 未配置。wechat_webhook:
            return            返回
        requests.post(config.wechat_webhook, json={"msgtype": "markdown", "markdown": {"content": content}})

    @staticmethod    @静态方法
    def send_feishu(content: str):
        if not config.feishu_webhook:
            return            返回
        requests.post(config.feishu_webhook, json={"msg_type": "text", "content": {"text": content}})

    @staticmethod    @静态方法
    def send_dingtalk(content: str):
        if not config.dingtalk_webhook:
            return            返回
        requests.post(config.dingtalk_webhook, json={"msgtype": "markdown", "markdown": {"title": "ETF每日决策看板", "text": content}})

    @classmethod
    def broadcast(cls, report_markdown: str):
        cls.send_wechat(report_markdown)
        cls.send_feishu(report_markdown)
        cls.send_dingtalk(report_markdown)
