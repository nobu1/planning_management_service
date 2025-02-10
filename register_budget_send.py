import zmq


def send_register_budget_data():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

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

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    send_register_budget_data()
