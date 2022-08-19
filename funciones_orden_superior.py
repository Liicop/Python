from functools import reduce

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    python_devs2 = list(filter(lambda worker : worker["language"] == "python",DATA))
    python_devs2 = list(map(lambda worker : worker["name"],python_devs2))
    javascript_devs = [worker["name"] for worker in DATA if worker["language"] == "javascript"]
    java_devs = [worker["name"] for worker in DATA if worker["language"] == "java"]
    go_devs = [worker["name"] for worker in DATA if worker["language"] == "go"]
    ruby_devs = [worker["name"] for worker in DATA if worker["language"] == "ruby"]
    platzi_workers = list(filter(lambda x : x["organization"] == "Platzi",DATA))
    platzi_workers = list(map(lambda x : x["name"],platzi_workers))
    platzi_workers2 = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(map(lambda worker : worker | {"Mayor": worker["age"]>=18}, DATA))
    adults2 = [x | {"Mayor":True} if x["age"]>17 else x | {"Mayor":False}  for x in DATA ]
    #print(python_devs)
    #print(javascript_devs)
    #print(java_devs)
    #print(go_devs)
    #print(ruby_devs)
    #print(platzi_workers)
    #print(adults)
    print(python_devs == python_devs2)
    print(platzi_workers == platzi_workers2)
    print(adults == adults2) 
   


if __name__ == "__main__":
    run()