people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            print(person['age'])
    return '해당하는 사람이 없습니다.' 
print(get_age('john'))
        
        
# def get_age(myname):
#     for person in people:
#         if person['name'] == myname:
#             return person['age']
#     return '해당하는 이름이 없습니다'
# print(get_age('b'))