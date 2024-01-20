def fullname(first_name, last_name) :

    return first_name + " " + last_name

def string_alternative (full_name):

    return full_name[:: 21]

def main():

    first_name = input("Enter your first name: ")

    last_name = input("Enter your last name: ")

    full_name = fullname(first_name, last_name)

    print ("Full Name:", full_name)

    result = string_alternative (full_name)

    print("Every Other Character in Full Name:", result)
    
main()