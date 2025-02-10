import zmq


def send_register_budget_data():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    input_menu = 0
    print("Planning management service has following services.")
    print("1. Register Budget Data")
    print("2. Modify Budget Data")
    print("3. Getting Budget Data")
    print("4. Getting Project List")
    while True:
        input_menu = input("Select the service menus[1-4]: ")
        if input_menu != 1 or input_menu != 2 or \
           input_menu != 3 or input_menu != 4:
            print("Please input the number between 1 and 4")
        else:
            break
    print("\n")

    if input_menu == 1:
        print("Request to register the budget data")

        # Send request JSON
        request_register_budget_json = {
            "request": {
                "event": "registerBudgetData",
                "body": {
                    "projectName": "project",
                    "startMonth": "2025-01",
                    "endMonth": "2025-02",
                    "amount": [
                        {
                            "month": "2025-01",
                            "pv": "100"
                        },
                        {
                            "month": "2025-02",
                            "pv": "200"
                        }
                    ]
                }
            }
        }
        socket.send_json(request_register_budget_json)

        # Receive response JSON
        receive_register_budget_json = socket.recv_json()
        print(receive_register_budget_json['response']['body'])

    elif input_menu == 2:
        print("Request to modify the budget data")

        # Send request JSON
        request_modify_budget_json = {
            "request": {
                "event": "modifyBudgetData",
                "body": {
                    "projectName": "project",
                    "userName": "suzuki",
                    "amount": [
                        {
                            "month": "2025-01",
                            "pv": "100"
                        }
                    ]
                }
            }
        }
        socket.send_json(request_modify_budget_json)

        # Receive response JSON
        receive_modify_budget_json = socket.recv_json()
        print(receive_modify_budget_json['response']['body'])

    elif input_menu == 3:
        print("Request to get the budget data")

        # Send request JSON
        request_get_budget_json = {
            "request": {
                "event": "getBudgetRecord",
                "body": {
                    "projectName": "project"
                }
            }
        }
        socket.send_json(request_get_budget_json)

        # Receive response JSON
        receive_get_budget_json = socket.recv_json()
        print(receive_get_budget_json['response']['body'])
        print(receive_get_budget_json['response']['code'])

    elif input_menu == 4:
        print("Request to get the project list")

        # Send request JSON
        request_get_project_json = {
            "request": {
                "event": "getProjectList",
                "body": ""
            }
        }
        socket.send_json(request_get_project_json)

        # Receive response JSON
        receive_get_project_json = socket.recv_json()
        print(receive_get_project_json['response']['body']['projects'])
        print(receive_get_project_json['response']['code'])

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    send_register_budget_data()
