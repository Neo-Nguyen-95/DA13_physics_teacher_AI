#%% LIB
from openai import OpenAI
import faiss
import numpy as np
from business import get_embedding

#%% KNOWLEDGE
with open("knowledge_base.txt", "r") as file:
    kb_content = file.read()
    
with open("qna.txt", "r") as file:
    qa_content = file.read()
    
# Split text into chunks
knowledge_text = kb_content.split('\n')
knowledge_text.extend(qa_content.replace('\n', '').split('---'))

#%% EMBEDDING
knowledge_embeddings = np.array([get_embedding(text) for text in knowledge_text])

dimension = knowledge_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(knowledge_embeddings)

faiss.write_index(index, "knowledge_index.faiss")