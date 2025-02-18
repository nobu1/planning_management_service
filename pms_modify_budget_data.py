import pandas as pd
import csv_file_path as PATH


def modify(receive_records):
    """Modify data of budget_data.csv"""

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
    df = pd.read_csv(PATH.BUDGET_DATA)

    # Check exisiting project name and month
    if df[
        (df["projectName"] == str(project_name)) &
        (df["month"] == str(amount_dict["month"]))
    ].bool:
        # If exist, update the value of pv
        df.loc[
            (df["projectName"] == str(project_name)) &
            (df["month"] == str(amount_dict["month"])), "pv"
        ] = int(amount_dict["pv"])

        # Modify budget_data.csv
        df.to_csv(PATH.BUDGET_DATA, index=False)

        # Return response code
        return "200"
    else:
        # If not exist, return response code
        return "400"
