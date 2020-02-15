from cloudmesh.common.dotdict import dotdict

if __name__=="__main__":
    person = {'name' :'Yasir',
               'school':'IU'}

    person = dotdict(person)
    print(f" Name: {person.name}")
    print(f" School : {person.school}")
