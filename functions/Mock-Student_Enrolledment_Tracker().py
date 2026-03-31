student_names=[]
student_info=[]
activities=set()
status={}

def add_student(student_names,student_info,status):
    name=input('Enter name')
    year=int(input('Enter yr'))
    student_names.append(name)
    student_info.append((name,year))
    status[name]='Active'
    return(student_names,student_info,status)


def update_activities(activities,str):
    if str not in activities:
        activities.add(str)
        return(activities)


def check_membership(dicti,name1):
    count=0
    x=dicti[name1]
    for j in dicti:
        if dicti[j]=='Active':
            count+=1
    return(x,count)
name1=input('Enter name')


while True:
    print('----menu----')
    print('1. Add student')
    print('2. Add Activity')
    print('3. Check  Membership')
    print('0. EXIT')
    choice=input('Enter choice:')
    if choice=='1':
        add_student(student_names,student_info,status)
    elif choice=='2':
        update_activities(activities,str)
    elif choice=='3':
        check_membership(status,name1)
    elif choice=='0':
        break
    else:
        print('Invalid')

print("Final Data Verification:")
print("Names List:",student_names)
print("Students Tuple List:",student_info)
print("Activities Set:", activities)
print("Status Dictionary:", status)






