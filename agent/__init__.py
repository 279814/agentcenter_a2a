import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
root_path = os.path.dirname(model_file_path)
sys.path.insert(0, root_path)

from agent.BuyAgent import buy_agent
from agent.ConsultAgent import consult_agent
from agent.KnowledgeAgent import knowledge_agent
from agent.RecommendAgent import recommend_agent
from agent.UnknownAgent import unknown_agent