from cloudmesh.common.dotdict import dotdict

if __name__=="__main__":
    person = {'name' :'Yasir'}

    person = dotdict(person)
    print(f" Name: {person.name}")

    school = {'name': 'IU',
              'capacity': '50,000',
              'Location':'Bloomington'}


    school = dotdict(school)
    print(f" School Name: {school.name}")
    print(f" School Capacity : {school.capacity}")