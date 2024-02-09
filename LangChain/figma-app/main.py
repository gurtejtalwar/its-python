import os

from langchain.indexes import VectorstoreIndexCreator
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.document_loaders.figma import FigmaFileLoader
from langchain_openai import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
import chromadb
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

figma_loader = FigmaFileLoader(
    os.getenv("ACCESS_TOKEN"),
    os.getenv("NODE_IDS"),
    os.getenv("FILE_KEY"), 
)

index = VectorstoreIndexCreator(embedding=OpenAIEmbeddings()).from_loaders([figma_loader])
figma_doc_retriever = index.vectorstore.as_retriever()

def generate_code(human_input):
    # I have no idea if the Jon Carmack thing makes for better code. YMMV.
    system_prompt_template = """You are expert coder Jon Carmack. Use the provided design context to create idiomatic HTML/CSS code as possible based on the user request.
    Everything must be inline in one file and your response must be directly renderable by the browser.
    Figma file nodes and metadata: {context}"""

    human_prompt_template = "Code the {text}. Ensure it's mobile responsive"
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_prompt_template
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_prompt_template
    )
    # delete the gpt-4 model_name to use the default gpt-3.5 turbo for faster results
    gpt_4 = ChatOpenAI(temperature=0.02, model_name="gpt-4")
    # Use the retriever's 'get_relevant_documents' method if needed to filter down longer docs
    relevant_nodes = figma_doc_retriever.get_relevant_documents(human_input)
    print(f"Relevant nodes: {relevant_nodes}")
    conversation = [system_message_prompt, human_message_prompt]
    chat_prompt = ChatPromptTemplate.from_messages(conversation)
    response = gpt_4(
        chat_prompt.format_prompt(
            context=relevant_nodes, text=human_input
        ).to_messages()
    )
    return response

response = generate_code("Meal Calculator Page") 

print (response)