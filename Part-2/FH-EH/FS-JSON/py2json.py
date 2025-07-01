import json 
emp={
    'eid':101,
    'ename':'RG',
    'avail':True,
    'loc':None
}
print(type(emp))

emp_json_str=json.dumps(emp)
print(emp)
print(emp_json_str)
print(type(emp_json_str))