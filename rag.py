import os

def retrieve_documents(state):

    context = ""

    folder = "docs"

    for file in os.listdir(folder):

        with open(os.path.join(folder,file),"r") as f:

            context += f.read()

    state["retrieved_context"] = context

    return state
