import pandas as pd
import csv_file_path as PATH


def make_project_list(receive_records):
    """Make project list with received JSON records"""

    # Read project.csv
    df = pd.read_csv(PATH.PROJECT)

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

    # Append into projects list
    for _, row in df.iterrows():
        response_json["response"]["body"]["projects"].append({
            "projectName": str(row['projectName']),
            "startMonth": str(row['startMonth']),
            "endMonth": str(row['endMonth'])
        })

    # Return the response JSON
    return response_json
