import zmq
import pms_register_budget_data as register_budget
import pms_modify_budget_data as modify_budget
import pms_get_budget_record as get_budget
import pms_get_project_list as get_project


def respond_json(socket, event, response_code):
    # Make response JSON
    response_json = {
        "response": {
            "event": event,
            "body": {"code": response_code}
        }
    }

    # Respond JSON data
    socket.send_json(response_json)


def receive_json_data():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("PMS Receiver Startup.")

    while True:
        # Receive JSON request
        receive_records = socket.recv_json()

        # Confirm event data
        event = receive_records['request']['event']

        if event == "registerBudgetData":
            # Register the budget data
            response_code = register_budget.register(receive_records)

            # Respond JSON data
            respond_json(socket, event, response_code)
        elif event == "modifyBudgetData":
            # Modify the budget data
            response_code = modify_budget.modify(receive_records)

            # Respond JSON data
            respond_json(socket, event, response_code)
        elif event == "getBudgetRecord":
            # Get budget record
            response_json = get_budget.make_budget_data(receive_records)

            # Respond JSON data
            socket.send_json(response_json)
        elif event == "getProjectList":
            # Get project list
            response_json = get_project.make_project_list(receive_records)

            # Respond JSON data
            socket.send_json(response_json)
        else:
            response_json = {
                "response": {
                    "event": "wrongRequest",
                    "body": {"code": "400"}
                }
            }

            # Respond JSON data
            socket.send_json(response_json)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    receive_json_data()
