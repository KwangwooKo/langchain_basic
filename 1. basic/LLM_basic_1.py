import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Set your API key from environment variable
api_key = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = api_key

# model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
# model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature = 0)
# model = ChatGroq(model='llama3-70b-8192', temperature =0)

# Invoke the model with a message 
# 'content' method: to make the results more human-readable
result=model.invoke("Tell me a joke?")
print("** With content method **")
print(result.content)

print("** Without content method **")
print(result)