str=input('enter string')
def palendrome(str):
    str_copy=str[::-1]
    if str==str_copy:
        return(True)
    else:
        return(False)
print(palendrome(str))
