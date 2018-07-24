from app.utils.news_api import NewsAPI
from app.utils.slack_helper import SlackHelper
from config import get_env

news = NewsAPI(get_env("NEWS_API_KEY"))
slack_helper = SlackHelper()


class Actions:

    @staticmethod
    def help():
        return {
            "text": "Available Commands",
            "attachments": [
                {
                    "text": "`/lit headlines` To get the top headlines"
                }
            ]
        }

    @staticmethod
    def headlines():
        slack_helper.post_message_with_attachment(news.get_top_headlines())

    @staticmethod
    def allowed_commands():
        return [
            'help',
            'headlines',
            'my headlines'
        ]

    @staticmethod
    def get_user_info(uid):
        return slack_helper.get_user_info(uid)

    @staticmethod
    def send_headlines_to_user(user_id):
        return slack_helper.post_message_to_user_with_attachments(news.get_top_headlines(), user_id)
