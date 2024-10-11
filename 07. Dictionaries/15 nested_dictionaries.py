# Nested dictionary
company = {
    "employee": {
        "Alice" : {"age": 32, "profession":"Engineer" },
        "Bob": {"age": 25, "profession": "Designer"},
        "Charlie": {"age": 35, "profession": "Manager"}
    },
    "department": ["Engineering", "Design", "Management"]
}


print(company["employee"]["Alice"].get("age"))
company["employee"].update({
    "Abdullah": {"age": 32, "profession": "Engineer"},
    "Abdul Aziz": {"age": 25, "profession": "Designer"},
})

employees = company.get("employee")
print(employees)

for employee in employees:
    print(employee)
    employee_details = company["employee"][employee]
    for emp_det in employee_details.values():
        print(emp_det)

    print()
