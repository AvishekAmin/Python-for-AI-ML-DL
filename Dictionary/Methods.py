info = {
    "name": "Avishek",
    "cgpa": 7.27,
    "subjects": ["DBMS", "OOPS", "OS", "CN", "DSA"]
}

print(info.keys())      # dict_keys(['name', 'cgpa', 'subjects'])

print(info.values())    # dict_values(['Avishek', 7.27, ['DBMS', 'OOPS', 'OS', 'CN', 'DSA']])

print(info.items())     # dict_items([('name', 'Avishek'), ('cgpa', 7.27), ('subjects', ['DBMS', 'OOPS', 'OS', 'CN', 'DSA'])])

print(info.get("cgpa"))     # 7.27

info.update({
    "city": "Kolkata"
})

print(info)