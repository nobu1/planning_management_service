# Planning Management Service

1. Instructions for REQUEST data
    - Make a request JSON.
    - Example request call is as follows.
    ```
    **** Request call of Register Budget Data ****
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

    **** Request call of Modify Budget Data ****
    request_modify_budget_json = {
        "request": {
            "event": "modifyBudgetData",
            "body": {
                "projectName": "project",
                "userName": "suzuki",
                "amount": [
                    {
                        "month": "2025-01",
                        "pv": "200"
                    }
                ]
            }
        }
    }

    **** Request call of Get Budget Data ****
    request_get_budget_json = {
        "request": {
            "event": "getBudgetRecord",
            "body": {
                "projectName": "project"
            }
        }
    }

    **** Request call of Get Project List ****
    request_get_project_json = {
        "request": {
            "event": "getProjectList",
            "body": ""
        }
    }
    ```
    - Send the request JSON to the receiver.
    - Receive JSON data from the receiver.  
1. Instructions for RECEIVE data
    - Receive the request JSON.
    - Confirm the event data of the JSON.
    - Extract data from the received JSON
    - Make a response JSON
    - Example response call is as follows.
    ```
    **** Response call of Register Budget Data ****
    response_json = {
        "response": {
            "event": "registerBudgetData",
            "body": {"code": "200"}
        }
    }

    **** Response call of Modify Budget Data ****
    response_json = {
        "response": {
            "event": "modifyBudgetData",
            "body": {"code": "200"}
        }
    }

    **** Response call of Get Budget Data ****
    response_json = {
        "response": {​​
            "event": "getBudgetRecord",​​
            "body": {​​
                "records": [​​
                    {​​
                        "month": "2025-01",​​
                        "pv": "100"​​
                    },​​
                    {​​
                        "month": "2025-02",​​
                        "pv": "200"​​
                    }​​
                ]​​
            },​​
            "code" : "200”,​​
        }
    }​​

    **** Response call of Get Project List ****
    response_json = {
        "response": {
            "event": "getBudgetRecord",
            "body": {
                "projects": [
                    {
                        "projectName": "projectA",
                        "startMonth": "2025-01",
                        "endMonth": "2025-02"
                    },
                    {
                        "projectName": "projectB",
                        "startMonth": "2025-03",
                        "endMonth": "2025-04"
                    }                 
                ]
            },
            "code": "200"
        }
    }
    ```
    - Send the response JSON to the sender.
1. UML sequence diagram
    - Sequence diagram for Register Budget Data
    ![Resiger Budget Data](./img/UML_RegisterBudgetData.jpg "Register Budget Data")  

    - Sequence diagram for Modify Budget Data
    ![Modify Budget Data](./img/UML_ModifyBudgetData.jpg "Modify Budget Data")  

    - Sequence diagram for Get Budget Data
    ![Get Budget Data](./img/UML_GetBudgetData.jpg "Get Budget Data")  

    - Sequcence diagram for Get Project List
    ![Get Project List](./img/UML_GetProjectList.jpg "Get Project List")  