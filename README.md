# Planning Management Service

1. Instructions for REQUEST data
- Make request of registering budget JSON.
- Example request call is as follows.
```
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
```
- Send the register budget JSON.
- Receive register budget JSON response.  
1. Instructions for RECEIVE data
1. UML sequence diagram
  
- Sequence diagram for Register Budget Data
![Resiger Budget Data](./img/UML_RegisterBudgetData.jpg "Register Budget Data")  

- Sequence diagram for Modify Budget Data
![Modify Budget Data](./img/UML_ModifyBudgetData.jpg "Modify Budget Data")  

- Sequence diagram for Get Budget Data
![Get Budget Data](./img/UML_GetBudgetData.jpg "Get Budget Data")  

- Sequcence diagram for Get Project List
![Get Project List](./img/UML_GetProjectList.jpg "Get Project List")  