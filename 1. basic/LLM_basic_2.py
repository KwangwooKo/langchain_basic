import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage 

# from langchain.chat_models import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Set your API key from environment variable
api_key = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = api_key

# model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

# model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 1)

messages = [
    SystemMessage (content = "You are a neuroscientist for more than 30 years. When you receive HumanMessage, summarize them with one paragraph"),
    HumanMessage (content = "Why is neurodegenerative disease difficult to treat")
]

result=model.invoke(messages)
print(result.content)
