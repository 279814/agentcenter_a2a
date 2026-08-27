from datetime import datetime

import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
root_path = os.path.dirname(model_file_path)
sys.path.insert(0, root_path)

from agent.BaseAgent import BaseAgent
from agent.prompts import system_prompt_config
from agent.tools import query_course_by_id
import asyncio
from agent.mcp import mcp_service


class ConsultAgent(BaseAgent):
    """
    课程咨询智能体
    """

    def system_prompt(self):
        return system_prompt_config.chat_consult_message

    def system_prompt_params(self):
        return {"now": datetime.now()}

    def tools(self) -> list:
        # return [query_course_by_id]
        # 通过名字获取工具，添加到智能体中使用
        tool = asyncio.run(mcp_service.get_tool("query_course_by_id"))
        return [tool]


consult_agent = ConsultAgent()
