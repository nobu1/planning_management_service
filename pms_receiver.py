import zmq
import pandas as pd

PROJECT = "./csv/project.csv"
BUDGET_DATA = "./csv/budget_data.csv"


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
            # Extract the body data from the receive_records
            project_name = \
                receive_records['request']['body']['projectName']
            start_month = \
                receive_records['request']['body']['startMonth']
            end_month = \
                receive_records['request']['body']['endMonth']
            amount1_dict = {
                "month": "",
                "pv": ""
            }
            amount2_dict = {
                "month": "",
                "pv": ""
            }
            amount1_dict["month"] = \
                receive_records['request']['body']['amount'][0]['month']
            amount1_dict['pv'] = \
                receive_records['request']['body']['amount'][0]['pv']
            amount2_dict["month"] = \
                receive_records['request']['body']['amount'][1]['month']
            amount2_dict['pv'] = \
                receive_records['request']['body']['amount'][1]['pv']
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

            # Respond JSON data
            socket.send_json(response_json)
        elif event == "modifyBudgetData":
            # Extract the body data from the receive_records
            project_name = \
                receive_records['request']['body']['projectName']
            amount_dict = {
                "month": "",
                "pv": ""
            }
            amount_dict["month"] = \
                receive_records['request']['body']['amount'][0]["month"]
            amount_dict["pv"] = \
                receive_records['request']['body']['amount'][0]["pv"]

            # Read budget_data.csv
            df = pd.read_csv(BUDGET_DATA)

            # Check exisiting project name and month
            if df[
                (df["projectName"] == str(project_name)) &
                (df["month"] == str(amount_dict["month"]))
            ].bool:
                # Update the value of pv
                df.loc[
                    (df["projectName"] == str(project_name)) &
                    (df["month"] == str(amount_dict["month"])), "pv"
                ] = int(amount_dict["pv"])

                # Modify budget_data.csv
                df.to_csv(BUDGET_DATA, index=False)

                # Make response JSON
                response_json = {
                    "response": {
                        "event": "modifyBudgetData",
                        "body": {"code": "200"}
                    }
                }

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
        elif event == "getBudgetRecord":
            # Extract the projectName from the receive_records
            project_name = \
                receive_records['request']['body']['projectName']

            # Read budget_data.csv
            df = pd.read_csv(BUDGET_DATA)
            df = df[df['projectName'] == project_name]

            # Initialize JSON
            response_json = {
                "response": {
                    "event": "getBudgetRecord",
                    "body": {
                        "records": []
                    },
                    "code": "200"
                }
            }

            # Append into records
            for _, row in df.iterrows():
                response_json["response"]["body"]["records"].append({
                    "month": str(row['month']),
                    "pv": str(row['pv'])
                })

            # Respond JSON data
            socket.send_json(response_json)
        elif event == "getProjectList":
            # Read project.csv
            df = pd.read_csv(PROJECT)

            # Initialize JSON
            response_json = {
                "response": {
                    "event": "getBudgetRecord",
                    "body": {
                        "projects": []
                    },
                    "code": "200"
                }
            }

            # Append into projects
            for _, row in df.iterrows():
                response_json["response"]["body"]["projects"].append({
                    "projectName": str(row['projectName']),
                    "startMonth": str(row['startMonth']),
                    "endMonth": str(row['endMonth'])
                })

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
