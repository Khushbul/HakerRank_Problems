
def validator(s):
    count = 0;
    for i,v in enumerate(s):
        if v.isalnum():
            count=count+1;
    if count!=0:
        print("True")
    else:print("False")

    count = 0;
    for i,v in enumerate(s):
        if v.isalpha():
            count = count + 1;
    if count != 0:
        print("True")
    else:
        print("False")

    count = 0;
    for i,v in enumerate(s):
        if v.isdigit():
            count = count + 1;
            break
    if count != 0:
        print("True")
    else:
        print("False")

    count = 0;
    for i,v in enumerate(s):
        if v.islower():
            count = count + 1;
            break
    if count != 0:
        print("True")
    else:
        print("False")

    count = 0;
    for i,v in enumerate(s):
        if v.isupper():
            count = count + 1;
            break
    if count != 0:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    s = input()

    validator(s)