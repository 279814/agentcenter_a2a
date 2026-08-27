import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
root_path = os.path.dirname(model_file_path)
sys.path.insert(0, root_path)

from agent.BaseAgent import BaseAgent
from agent.prompts import system_prompt_config


class KnowledgeAgent(BaseAgent):
    """
    知识讲解智能体
    """

    def system_prompt(self):
        return system_prompt_config.chat_knowledge_message


knowledge_agent = KnowledgeAgent()