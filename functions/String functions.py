a=8
b=" October is crazy "
print(type(a))
print(type(b))

print(len(b))

#String slicing
print(b[7])
print(b[0:])
print(b[1:5])

#Substring check
if "is" in b:
    print("present")
else:
    print("Absent")

#String methods    
print(b.upper())
print(b.lower())

print(b.strip()) #removes blank space from either ends if any(there is also l-strip and r-strip)

print(b.split())
print(b.split('o'))
print(b.split('is'))

print(b.replace('O','M'))
print(b.replace('crazy','confusing'))

