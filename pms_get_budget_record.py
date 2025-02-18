import pandas as pd
import csv_file_path as PATH


def make_budget_data(receive_records):
    # Extract the projectName from the receive_records
    project_name = \
        receive_records['request']['body']['projectName']

    # Read budget_data.csv
    df = pd.read_csv(PATH.BUDGET_DATA)
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

    # Return the response JSON
    return response_json
