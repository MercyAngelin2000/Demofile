ju = [{'scholarshipName': 'Minority', 'boy': '20', 'girl': '30', 'byGovt': 'yes', 'byPrivate': 'no'}, {'scholarshipName': 'SC/SC', 'boy': '20', 'girl': '40', 'byGovt': 'yes', 'byPrivate': 'no'}, {'scholarshipName': 'Farmer', 'boy': '30', 'girl': '10', 'byGovt': 'yes', 'byPrivate': 'no'}, {'scholarshipName': 'National', 'boy': '30', 'girl': '10', 'byGovt': 'yes', 'byPrivate': 'no'},
     {'scholarshipName': 'Guezou', 'boy': '100', 'girl': '1000', 'byGovt': 'no', 'byPrivate': 'yes'}]
j=[]
for i in ju:
    j.append(list(i.values()))
print(j)
