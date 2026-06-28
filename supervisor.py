def supervisor(state):

    if state["approved"]:

        state["final_response"] = (

            state["department_response"]

            + "\n\n"

            + state["retrieved_context"]

        )

    else:

        state["final_response"] = (

            "Request rejected by supervisor."

        )

    return state