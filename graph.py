from router import classify_intent

from agents.sales_agent import sales_agent

from agents.billing_agent import billing_agent

from agents.account_agent import account_agent

from agents.technical_agent import technical_agent

def route(state):

    intent = state["intent"]

    if intent == "sales":

        return sales_agent(state)

    elif intent == "billing":

        return billing_agent(state)

    elif intent == "account":

        return account_agent(state)

    else:

        return technical_agent(state)