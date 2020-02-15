from cloudmesh.common import FlatDict

school = {'school': {
    'name': 'IU'},
    'student': {
        'first': 'Yasir',
        'last': 'Alibadi'}}

flat = FlatDict(school, sep=".")
print(flat)
print("name:",flat['school.name'])
print("Student_Name:",flat['student.first'])
