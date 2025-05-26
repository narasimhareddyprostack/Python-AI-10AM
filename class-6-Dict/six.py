employees = [
    {"id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com", "phone": "555-101-0001", "department": "Engineering"},
    {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com", "phone": "555-101-0002", "department": "HR"},
    {"id": 3, "name": "Carol Lee", "email": "carol.lee@example.com", "phone": "555-101-0003", "department": "Sales"},
    {"id": 4, "name": "David Brown", "email": "david.brown@example.com", "phone": "555-101-0004", "department": "IT"},
    {"id": 5, "name": "Eva Davis", "email": "eva.davis@example.com", "phone": "555-101-0005", "department": "Finance"},
    {"id": 6, "name": "Frank Moore", "email": "frank.moore@example.com", "phone": "555-101-0006", "department": "Marketing"},
    {"id": 7, "name": "Grace Taylor", "email": "grace.taylor@example.com", "phone": "555-101-0007", "department": "Legal"},
    {"id": 8, "name": "Henry Wilson", "email": "henry.wilson@example.com", "phone": "555-101-0008", "department": "Operations"},
    {"id": 9, "name": "Ivy Clark", "email": "ivy.clark@example.com", "phone": "555-101-0009", "department": "Engineering"},
    {"id": 10, "name": "Jack White", "email": "jack.white@example.com", "phone": "555-101-0010", "department": "HR"},
    {"id": 11, "name": "Kim Lewis", "email": "kim.lewis@example.com", "phone": "555-101-0011", "department": "Sales"},
    {"id": 12, "name": "Liam Walker", "email": "liam.walker@example.com", "phone": "555-101-0012", "department": "IT"},
    {"id": 13, "name": "Mia Hall", "email": "mia.hall@example.com", "phone": "555-101-0013", "department": "Finance"},
    {"id": 14, "name": "Noah Allen", "email": "noah.allen@example.com", "phone": "555-101-0014", "department": "Marketing"},
    {"id": 15, "name": "Olivia Young", "email": "olivia.young@example.com", "phone": "555-101-0015", "department": "Legal"},
    {"id": 16, "name": "Paul Hernandez", "email": "paul.hernandez@example.com", "phone": "555-101-0016", "department": "Operations"},
    {"id": 17, "name": "Quinn King", "email": "quinn.king@example.com", "phone": "555-101-0017", "department": "Engineering"},
    {"id": 18, "name": "Rachel Wright", "email": "rachel.wright@example.com", "phone": "555-101-0018", "department": "HR"},
    {"id": 19, "name": "Samuel Lopez", "email": "samuel.lopez@example.com", "phone": "555-101-0019", "department": "Sales"},
    {"id": 20, "name": "Tina Hill", "email": "tina.hill@example.com", "phone": "555-101-0020", "department": "IT"},
    # ... entries 21 to 99 omitted for brevity ...
    {"id": 100, "name": "Zoe Nash", "email": "zoe.nash@example.com", "phone": "555-101-0100", "department": "Marketing"},
]


#all employees name with depertment

for emp in employees:
    print(emp['name'],"-", emp['department'])