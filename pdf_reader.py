from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS 
from langchain.chains import RetrievalQA 
from langchain_community.llms import ollama
from langchain_ollama import OllamaEmbeddings

def pdf_loader(path):
    loader=PyPDFLoader(path)
    pages=[]
    pages=loader.load()
    return pages 

# this function will take the pdf pages and make them into chunks of 1000 characters with 150 characters overlap.
def split_chunks(pages):
    text="\n".join(page.page_content for page in pages)
    splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks= splitter.split_text(text)
    return chunks

#vectorise the chunks using the qwen2.5:7b model and save the vector_db.
def create_vector_db(chunks):
    embedding_model= OllamaEmbeddings(model="qwen2.5:7b")
    vector_db= FAISS.from_texts(chunks, embedding_model)
    vector_db.save_local("a_different_story")
    return vector_db
# load a pre-trained vector_db
def load_vector_db(path):
    embedding_model= OllamaEmbeddings(model="qwen2.5:7b")
    vector_db= FAISS.load_local(path, embeddings=embedding_model, allow_dangerous_deserialization=True)
    return vector_db

# this function will make a bot using the qwen2.5:7b model and train it with the vector_db.
def making_bot(vector_db):
    llm= ChatOllama(
        model= "qwen2.5:7b",
        temperature=0.6
    )
    retriever = vector_db.as_retriever()
    bot = RetrievalQA.from_chain_type(llm, retriever=retriever)
    return bot

# load the bot according to your criteria 
def bot_father(path):
    # *** you must keep one bot turn off otherwise they might make conflict
    # this bot is a brand new bot that has to be trained with a pdf.
    #bot=making_bot(create_vector_db(split_chunks(pdf_loader(path))))
    # this bot is pre-trained with a vector_db
    bot=making_bot(load_vector_db(path))
    
    return bot

def main():
    if __name__ == "__main__":
        
        #Enter the pdf path. e.g. : r"A:\Docs\a_different_story.pdf" 
        #path=
        # if you want your pre built vector_db give it's path here. e.g. : r"A:\Docs\a_different_story_db"
        vector_db_path=r"A:\vscode\llm-pdf-reader\a_different_story"

        # if you want to use pre-trained model than use vector_db_path as bot_father parameter
        # else use path as bot_father parameter. 
        bot= bot_father(vector_db_path)
        prompt=input("Ask your question or give me 'tata' to exit the conversion\n: ")
            
        while (prompt!= "tata"):
            response= bot.invoke(prompt)
            print(":", end="")
            print(response['result'])
            prompt=input("\n: ")
        
    
    else:
        print("Access Denied!!!")



main()