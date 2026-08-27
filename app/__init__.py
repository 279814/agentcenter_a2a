import os, sys
current_file_path = os.path.abspath(__file__)
model_file_path = os.path.dirname(current_file_path)
root_path = os.path.dirname(model_file_path)
sys.path.insert(0, root_path)

from app.RecommendApp import recommend_app
from app.BuyApp import buy_app
from app.ConsultApp import consult_app
from app.KnowledgeApp import knowledge_app
from app.UnknownApp import unknown_app