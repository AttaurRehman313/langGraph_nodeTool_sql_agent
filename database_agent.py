
import os
from pymongo import MongoClient
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langgraph.checkpoint.mongodb import MongoDBSaver
from langchain.tools import tool

from langgraph.graph import StateGraph
# from langgraph import Annotation
from pydantic import BaseModel, Field
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection
mongo_uri = "mongodb://ask-dubai:ask-dubai@34.16.43.4:27017/ask-dubai"
client = MongoClient(mongo_uri)
db_name = "ask-dubai"
db = client[db_name]
collection = db["employees"]

class EmployeeLookupInput(BaseModel):
    query: str = Field(description="The search query")
    n: int = Field(default=10, description="Number of results to return")

# @tool(name="employee_lookup", description="Gathers employee details from the HR database", input_schema=EmployeeLookupInput)
async def employee_lookup_tool(input: EmployeeLookupInput):
    print("Employee lookup tool called")

    db_config = {
        'collection': collection,
        'index_name': 'vector_index',
        'text_key': 'embedding_text',
        'embedding_key': 'embedding',
    }

    # Initialize vector store
    vector_store = MongoDBAtlasVectorSearch(
        embedding=OpenAIEmbeddings(),
        **db_config
    )

    result = await vector_store.similarity_search_with_score(input.query, input.n)
    return result

print("***********************************************\n",employee_lookup_tool('how many table in database'))

