from agent.BaseAgent import BaseAgent
from agent.prompts import system_prompt_config
from agent.tools import query_course_by_id


class RecommendAgent(BaseAgent):
    """
    课程推荐智能体
    """

    def system_prompt(self):
        return system_prompt_config.chat_recommend_message

    def tools(self) -> list:
        return [query_course_by_id]

recommend_agent = RecommendAgent()