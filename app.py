from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
import time

from rich.console import Console
from rich.markdown import Markdown

# Ollama should be working in the computer backfround 
model =OllamaLLM(model="gemma3:4b", temperature=0.5)

template = """
You are an assistant specialized in supporting recruiters. 
Your task is to strictly analyze ONLY the CV information provided below. 
Do not use any external knowledge or assumptions beyond the given CVs. 
If some information is missing, simply indicate "Not specified".

CV Content:
{input}

Please help the recruiter by answering the following question based ONLY on the CV data provided:
Question:
{question}

Answer:
"""


#question = "give me a summary of the skills and experiences of the candidate"

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("--------------------------------------")
    question = input("Enter your question (or 'q' to quit): ")
    if question.lower() == 'q':
        break

    # Start timer
    start_time = time.time()

    # Retrieval + Inference
    print("Retrieving relevent CV section...")
    relevent_CV_Section = retriever.invoke(question)
    print("Done. 🟢\n")
    result = chain.invoke({"input": relevent_CV_Section, "question": question})

    # End timer
    end_time = time.time()
    inference_time = end_time - start_time

    # Display result
    resultMd = Markdown(result)
    console = Console()
    console.print(resultMd)

    # Show inference duration
    print(f"\n⏱ Inference time: {inference_time:.2f} seconds\n")