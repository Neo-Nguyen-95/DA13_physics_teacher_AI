#%% LIB
from openai import OpenAI
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

# OPEN AI API key
OPENAI_API_KEY = os.getenv("SECRETE_KEY")

#%% EMBEDDING
client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text):
    response = client.embeddings.create(
        input = text,
        model='text-embedding-ada-002'
        )
    
    embedding = response.data[0].embedding
    
    return np.array(embedding)


