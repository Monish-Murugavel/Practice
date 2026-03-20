x=[]
z=[]
s='({)}'
for i in s:
            if i=='(':
                if ')' in s:
                    print(True)
                else:
                    print(False)
                x.append(i)
            elif i=='{':
                if '}' in s:
                        print(True)
                else:
                    print(False)
                x.append(i)
            elif i=='[':
                if i==']':
                    print(True)
                else:
                    print(False)
                x.append(i)
                