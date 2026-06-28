def classify_intent(state):

    query = state["query"].lower()

    if "price" in query or "plan" in query:

        state["intent"] = "sales"

    elif "refund" in query or "invoice" in query or "payment" in query:

        state["intent"] = "billing"

    elif "password" in query or "account" in query:

        state["intent"] = "account"

    else:

        state["intent"] = "technical"

    return state
