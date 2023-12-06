from trulens_eval import TruChain, Feedback, OpenAI, Huggingface, Tru
import langchain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms.base import LLM
from pydantic import BaseModel, root_validator
from typing import Any, Mapping, Optional, List, Dict
import markdown
import vertexai
from langchain.llms import VertexAI
from dotenv import load_dotenv
import os
from google.cloud import aiplatform

# Load environment variables
load_dotenv()
dotenv_result = load_dotenv()

print("Dotenv Result:", dotenv_result)

# Construct the absolute path to the JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "google.json")

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file_path
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # Provide a default value
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")

PROJECT_ID = "travel-407110"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

# Initialize Vertex AI SDK
vertexai.init(project="travel-407110", location="us-central1")

openai = OpenAI()
hugs = Huggingface()
tru = Tru()
tru.run_dashboard()

class GenerateChat:
    def __init__(self):
        tru.reset_database()

        self.llm = VertexAI(
            model_name='text-bison',
            max_output_tokens=1024,
            temperature=0.1,
            top_p=0.8,
            top_k=40,
            verbose=True,
        )
        
#         template = """You are a chatbot having a conversation with a human.
#         {chat_history}
#         Human: {human_input}
#         Chatbot:"""
#         self.prompt = PromptTemplate(
#        input_variables=["chat_history", "human_input"], template=template
# )
        self.memory = ConversationBufferMemory()


    def generate(self, input_text):

        chain = ConversationChain(llm=self.llm, memory=self.memory, verbose=True)
        # Question/answer relevance between overall question and answer.
        f_relevance = Feedback(openai.relevance).on_input_output()
        f_lang_match = Feedback(hugs.language_match).on_input_output()

        # Moderation metrics on output
        f_hate = Feedback(openai.moderation_hate).on_output()
        f_violent = Feedback(openai.moderation_violence, higher_is_better=False).on_output()
        f_selfharm = Feedback(openai.moderation_selfharm, higher_is_better=False).on_output()
        f_maliciousness = Feedback(openai.maliciousness_with_cot_reasons, higher_is_better=False).on_output()
# TruLens Eval chain recorder
        chain_recorder = TruChain(
        chain, app_id="travel-chat", feedbacks=[f_relevance, f_hate, f_violent, f_selfharm,f_lang_match, f_maliciousness]
            )       
        with chain_recorder as recording:
            llm_response = chain(input_text)

        return       chain.predict(input=input_text)

