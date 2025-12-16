from datetime import datetime
from agent.BaseAgent import BaseAgent
from agent.prompts import system_prompt_config
from agent.tools import query_course_by_id


class ConsultAgent(BaseAgent):
    """
    课程咨询智能体
    """

    def system_prompt(self):
        return system_prompt_config.chat_consult_message

    def system_prompt_params(self):
        return {"now": datetime.now()}

    def tools(self) -> list:
        return [query_course_by_id]


consult_agent = ConsultAgent()
