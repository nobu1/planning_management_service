import pandas as pd
import csv_file_path as PATH


def register(receive_records):
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
    df.to_csv(PATH.PROJECT, index=False, mode='a', header=False)

    # Store the budget data into budget_data.csv
    for data in amount_list:
        df = pd.DataFrame({
            'projectName': [project_name],
            'month': data["month"],
            'pv': data["pv"]
        })
        df.to_csv(PATH.BUDGET_DATA, index=False, mode='a', header=False)

    # Return response code
    return "200"
