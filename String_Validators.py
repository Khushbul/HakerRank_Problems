
def validator(s):
    for i,v in enumerate(s):
        if v.isalnum():
            print("True")
            break
    for i,v in enumerate(s):
        if v.isalpha():
            print("True")
            break
    for i,v in enumerate(s):
        if v.isdigit():
            print("True")
            break
    for i,v in enumerate(s):
        if v.islower():
            print("True")
            break
    for i,v in enumerate(s):
        if v.isupper():
            print("True")
            break


if __name__ == '__main__':
    s = input()

    validator(s)