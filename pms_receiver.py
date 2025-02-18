import zmq
import pms_register_budget_data as register_budget
import pms_modify_budget_data as modify_budget
import pms_get_budget_record as get_budget
import pms_get_project_list as get_project


def response_json_with_code(socket, event, response_code):
    """Send response JSON with event and response code"""

    # Make response JSON
    response_json = {
        "response": {
            "event": event,
            "body": {"code": response_code}
        }
    }

    socket.send_json(response_json)


def response_json_with_data(socket, json_data):
    """Send response JSON with data"""
    socket.send_json(json_data)


def receive_json_data():
    """Receive request JSON data"""

    # Set port of ZeroMQ
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("PMS Receiver Startup.")
    while True:
        # Extract event data from the request JSON data
        receive_records = socket.recv_json()
        event = receive_records['request']['event']

        if event == "registerBudgetData":
            # Get the response code from registering the budget data
            response_code = register_budget.register(receive_records)

            response_json_with_code(socket, event, response_code)
        elif event == "modifyBudgetData":
            # Get the response code from modifying the budget data
            response_code = modify_budget.modify(receive_records)

            response_json_with_code(socket, event, response_code)
        elif event == "getBudgetRecord":
            response_json_with_data(
                get_budget.make_budget_data(receive_records)
            )
        elif event == "getProjectList":
            response_json_with_data(
                get_project.make_project_list(receive_records)
            )
        else:
            response_json_with_code(socket, "wrongRequest", "400")

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    receive_json_data()
