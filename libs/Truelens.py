from trulens_eval.feedback.provider.hugs import Huggingface
import langchain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
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

# Construct the absolute path to the JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "google.json")

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file_path
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", default="")  # Provide a default value
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY", default="")

PROJECT_ID = "travel-407110"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

# Initialize Vertex AI SDK
vertexai.init(project="travel-407110", location="us-central1")


class GenerateChat:
    def __init__(self):
        self.llm = VertexAI(
            model_name='text-bison',
            max_output_tokens=1024,
            temperature=0.1,
            top_p=0.8,
            top_k=40,
            verbose=True,
        )
        self.memory = ConversationBufferMemory()

    def generate(self, input_text):
        conversation = ConversationChain(
            llm=self.llm,
            verbose=True,
            memory=self.memory
        )
        return conversation.predict(input=input_text)
