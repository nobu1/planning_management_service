import zmq
import pandas as pd

PROJECT = "./csv/project.csv"
BUDGET_DATA = "./csv/budget_data.csv"


def receive_register_budget_data():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Budget Data Receiver Startup.")

    while True:
        # Receive JSON request
        budget_records = socket.recv_json()

        # Confirm event data
        event = budget_records['request']['event']

        if event == "registerBudgetData":
            # Extract the body data from the budget_records
            project_name = \
                budget_records['request']['body']['projectName']
            start_month = \
                budget_records['request']['body']['startMonth']
            end_month = \
                budget_records['request']['body']['endMonth']
            amount1_dict = {
                "month": "",
                "pv": ""
            }
            amount2_dict = {
                "month": "",
                "pv": ""
            }
            amount1_dict["month"] = \
                budget_records['request']['body']['amount'][0]['month']
            amount1_dict['pv'] = \
                budget_records['request']['body']['amount'][0]['pv']
            amount2_dict["month"] = \
                budget_records['request']['body']['amount'][1]['month']
            amount2_dict['pv'] = \
                budget_records['request']['body']['amount'][1]['pv']
            amount_list = [amount1_dict, amount2_dict]

            # Store the budget data into project.csv
            df = pd.DataFrame({
                'projectName': [project_name],
                'startMonth': [start_month],
                'endMonth': [end_month]
            })
            df.to_csv(PROJECT, index=False, mode='a', header=False)

            # Store the budget data into budget_data.csv
            for data in amount_list:
                df = pd.DataFrame({
                    'projectName': [project_name],
                    'month': data["month"],
                    'pv': data["pv"]
                })
                df.to_csv(BUDGET_DATA, index=False, mode='a', header=False)

            # Make response JSON
            response_json = {
                "response": {
                    "event": "registerBudgetData",
                    "body": {"code": "200"}
                }
            }
        else:
            response_json = {
                "response": {
                    "event": "registerBudgetData",
                    "body": {"code": "400"}
                }
            }

        # Respond JSON data
        socket.send_json(response_json)

    socket.close()
    context.destroy()

    return


if __name__ == "__main__":
    receive_register_budget_data()
