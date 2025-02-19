import pandas as pd
import csv_file_path as PATH


def register(receive_records):
    """Register data into budget_data.csv and project.csv"""

    # Extract the body data from the receive_records
    project_name = \
        receive_records['request']['body']['projectName']
    start_month = \
        receive_records['request']['body']['startMonth']
    end_month = \
        receive_records['request']['body']['endMonth']
    amount = receive_records['request']['body']['amount']

    # Store the budget data into project.csv
    df = pd.DataFrame({
        'projectName': [project_name],
        'startMonth': [start_month],
        'endMonth': [end_month]
    })
    df.to_csv(PATH.PROJECT, index=False, mode='a', header=False)

    # Store the budget data into budget_data.csv
    for data in amount:
        df = pd.DataFrame({
            'projectName': [project_name],
            'month': data["month"],
            'pv': data["pv"]
        })
        df.to_csv(PATH.BUDGET_DATA, index=False, mode='a', header=False)

    # Return response code
    return "200"
