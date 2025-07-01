employees=[
    {'eid':101,'ename':'Rahul','loc':'Wayanad'},
    {'eid':102,'ename':'Sonia','loc':'New Delhi'},
    {'eid':103,'ename':'Priyanka','loc':'Noida'},
    {'eid':104,'ename':'Modi','loc':'New Delhi'}
]
#print all employee and loc
for emp in employees:
    print("Employee Name:", emp['ename'],"- and Loc", emp['loc'])