list1=[]
tuple1=[]
set1=set()
dict1={}

def add_student(list1,tuple1,dict1):
    new_name=input('Enter new name')
    year=int(input('enter year'))
    list1.append(new_name)
    x=(new_name,year)
    tuple1.append(x)
    dict1[new_name]='Active'
    print('Done')

def update_activities(set1,new_act):
    if new_act not in set1:
        set1.add(new_act)
    else:
        print('Already member')
    print(set1)

def check_membership(dict1,pers_name):
    if pers_name not in dict1:
        print('Not found')
    else:
        c=[]
        d=list(dict1.values())
        c.append(dict1[pers_name])
        c.append(d.count('Active'))
        dict1[pers_name]='Active'
        print(tuple(c))


def all_details(list1,tuple1,dict1,set1):
    print(list1)
    print(tuple1)
    print(dict1)
    print(set1)

while True:
    print('1.ADD STUDENT, PRESS 1')
    print('2. UPDATE ACTIVITIES, PRESS 1')
    print('3.CHECK MEMBERSHIP, PRESS 1')
    print('4. END, PRESS 1')

    input1=int(input('Enter 1,2,3,4,5 :'))
    if input1==1:
        add_student(list1,tuple1,dict1)
    
    elif input1==2:
        new_act=input('ENter new activity')
        update_activities(set1,new_act)
    
    elif input1==3:
        pers_name=input('Enter person name')
        check_membership(dict1,pers_name)

    elif input1==4:
        all_details(list1,tuple1,dict1,set1)

    elif input1==5:
        print('THank you')
        break






