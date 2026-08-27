from a2a.server.agent_execution import AgentExecutor

import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
root_path = os.path.dirname(model_file_path)
sys.path.insert(0, root_path)

from app.BaseApp import BaseApp
from executor.MyExecutor import MyExecutor
from agent import buy_agent


class BuyApp(BaseApp):
    """
    课程购买应用
    """

    def app_type(self):
        return "buy"

    def agent_executor(self) -> AgentExecutor:
        return MyExecutor(buy_agent)


buy_app = BuyApp()
