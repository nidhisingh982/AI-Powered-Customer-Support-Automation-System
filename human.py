def approval(state):

    q = state["query"].lower()

    keywords = [

        "refund",

        "cancel",

        "closure",

        "compensation",

        "management"

    ]

    if any(word in q for word in keywords):

        state["approval_required"] = True

        print("Supervisor Approval Required")

        ans = input("Approve? (yes/no): ")

        state["approved"] = ans.lower()=="yes"

    else:

        state["approval_required"] = False

        state["approved"] = True

    return state