from dotenv import load_dotenv
from langchain_openai import ChatOpenAI # <- OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI # <- GoggoleGenerativeAI
from langchain_groq import ChatGroq # <- Groq

# Load environment variables from .env
load_dotenv()

## Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")

## Creat a GoogleGenerativeAI model
# model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

## Creat a Groq model
model = ChatGroq(model='llama3-70b-8192')

# Invoke the model with a message
result = model.invoke("Who is the president of United States?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
