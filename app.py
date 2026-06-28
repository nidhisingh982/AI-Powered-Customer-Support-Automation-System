from router import classify_intent

from graph import route

from rag import retrieve_documents

from human import approval

from supervisor import supervisor

from memory import save_memory,get_last_query

name = input("Customer Name: ")

query = input("Enter Query: ")

if "previous" in query.lower():

    print(get_last_query(name))

    exit()

state={

    "customer_name":name,

    "query":query,

    "intent":"",

    "retrieved_context":"",

    "department_response":"",

    "approval_required":False,

    "approved":False,

    "final_response":""

}

save_memory(name,query)

state=classify_intent(state)

state=route(state)

state=retrieve_documents(state)

state=approval(state)

state=supervisor(state)

print()

print(state["final_response"])