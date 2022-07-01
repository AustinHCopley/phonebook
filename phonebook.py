# phone book created in 2019 during my first cs class

#FUNCTION
def tag_replace(string):
    tag = ''
    if string[0] == 'f':
        print()
        tag = "First"
    elif string[0] == 'l':
        tag = "Last"
    elif string[0] == 'h':
        tag = "Home #"
    elif string[0] == 'm':
        tag = "Mobile #"
    elif string[0] == 'h':
        tag = "Home #"
    elif string[0] == 'e':
        tag = "Email"
    elif string[0] == 'b':
        tag = "Birthdate"
    string = tag + ': ' + string[1:]
    return string

def tag_remove(string):
    string = string[1:]
    return string

print()
#CHECK FOR BIRTHDAYS
import datetime
dt = datetime.datetime.today()

month = str(dt.month)
if len(month) == 1:
    month = '0' + month

day = str(dt.day)
if len(day) == 1:
    day = '0' + day
date = month + '-' + day

with open("phonebook.txt", 'r') as pbr:
    name = ''
    contents = pbr.readlines()
    for line in contents:
        if ('b' + date) in line:
            i = 0
            while i < len(line):
                if line[i] == ',':
                    name = line[1:i]
                    break
                i += 1
            print("       [ALERT]  Today is " + name + "'s birthday")
            

#START
start = 0
while start == 0:

    #OPTIONS MENU
    print("       Phone Book")
    print("<<=+=+=+=+=+=+=+=+=+=+=+=>>")
    print("       Enter an option (1-6):")
    print("  1.  View all contacts")
    print("  2.  Search for a contact")
    print("  3.  Add a contact")
    print("  4.  Update a contact")
    print("  5.  Delete a contact")
    print("  6.  Quit")

    option = input("       OPTION>> ")
    

#OPTION 1
    if option == '1' or option.lower() == 'view all contacts' or option.lower() == 'view':
        
        with open("phonebook.txt", 'r') as pbr:
            content = pbr.readlines()
            
            for line in content:
                i = 0
                j = 0
                
                while i < len(line):
                    if line[i] == ',':
                        print(tag_replace(line[j:i]))
                        j = i + 1
                    i += 1
        print()
        

#OPTION 2
    elif option == '2' or option.lower() == 'search for a contact' or option.lower() == 'search':
        print()
        print("       Please enter the first name of the person you would like to search for:")
        name = input("       NAME>> ")
        result_list = []
        results = 0
        
        with open("phonebook.txt", 'r') as pbr:
            
            content = pbr.readlines()
            for line in content:
                if ("f" + name) in line:
                    result_list.append(line)
                    results += 1
            i = 0
            result = ''
            result_names = []
            
            while i < results:
                j = 0
                k = 0
                l = 0
                m = 0
                while j < len(result_list[i]):
                    result = ''
                    if result_list[i][j] == ',':
                        if result_list[i][j + 1] != 'l':
                            result_names.append(tag_remove(line[0:j]))
                            j = len(result_list[i])
                        else:
                            k = j + 1
                            l = k
                            while l < len(result_list[i]):
                                if result_list[i][l] == ',':
                                    m = l
                                    l = (len(result_list[i]))
                                l += 1
                            
                            result += tag_remove(result_list[i][0:j])
                            result += ' '
                            result += tag_remove(result_list[i][k:m])
                            result_names.append(result)
                            if len(result_names) > 1:
                                result_names.pop(len(result_names) - 2)

                    j += 1
                i += 1

            j = 0
            i = 0
            if results == 0:
                print("       [There were no results]")
            elif results == 1:
                i = 0
                j = 0
                print("       [Found 1 contact]")
                while i < len(result_list[0]):
                    if result_list[0][i] == ',':
                        print(tag_replace(result_list[0][j:i]))
                        j = i + 1
                    i += 1
                print()
            elif results > 1:
                print("       [Found", results, "contacts]")
                print("       Which would you like to view?")
                
                while i < results:
                    print("  " + str(i + 1) + ')  ' + result_names[i])
                    i += 1
                
                choice = int(input("       CONTACT>> "))
                print()
                i = 0
                j = 0
                while i < len(result_list[choice-1]):
                    if result_list[choice-1][i] == ',':
                        print(tag_replace(result_list[choice-1][j:i]))
                        j = i + 1
                    i += 1
            print()


#OPTION 3
    elif option == '3' or option.lower() == 'add a contact' or option.lower() == 'add':
        print()
        contact = ''
        print("       Enter the first name of the new contact.")
        first = input("       FIRST NAME>> ")
        contact = 'f' + first + ','

        #ADDITIONAL INFORMATION
        start2 = True
        print("<<=+=+=+=+=+=+=+=+=+=+=+=>>")
        print("       What information would you like to add?")
        
        while start2:
            
            print("  1.  Last Name")
            print("  2.  Mobile #")
            print("  3.  Home #")
            print("  4.  Email")
            print("  5.  Birthdate")
            print("  6.  None")
            
            option1 = input("       OPTION>> ")
            if option1 == '1':
                print()
                last = input("       LAST NAME>> ")
                contact += ('l' + last + ',')
                print("       [Information added successfully]")
                
            elif option1 == '2':
                print()
                mobile = input("       MOBILE#>> ")
                contact += ('m' + mobile + ',')
                print("       [Information added successfully]")
                
            elif option1 == '3':
                print()
                home = input("       HOME#>> ")
                contact += ('h' + home + ',')
                print("       [Information added successfully]")
                
            elif option1 == '4':
                print()
                email = input("       EMAIL>> ")
                contact += ('e' + email + ',')
                print("       [Information added successfully]")
                
            elif option1 == '5':
                print()
                birth = input("       BIRTHDATE [MM-DD-YYYY]>> ")
                contact += ('b' + birth + ',')
                print("       [Information added successfully]")
                
            elif option1 == '6':
                print()
                contact += '\n'
                start2 = False
                
            else:
                print("      *ERROR: Please enter a valid option")
                print()
            
        with open("phonebook.txt", 'r') as pbr:
            contents = pbr.readlines()
            contents.append(contact)
            contents.sort()

        with open("phonebook.txt", 'w') as pbw:
            for line in contents:
                pbw.write(line)


#OPTION 4
    elif option == '4' or option.lower() == 'update a contact' or option.lower() == 'update':
        print()
        
        print("       Please enter the first name of the person whose contact you would like to update:")
        name = input("       NAME>> ")
        result_list = []
        results = 0
        indexes = []
        i = 0
        
        with open("phonebook.txt", 'r') as pbr:
            
            content = pbr.readlines()
            for line in content:
                if ("f" + name) in line:
                    indexes.append(i)
                    result_list.append(line)
                    results += 1
                i += 1
            i = 0
            result = ''
            result_names = []
            
            while i < results:
                j = 0
                k = 0
                l = 0
                m = 0
                while j < len(result_list[i]):
                    result = ''
                    if result_list[i][j] == ',':
                        if result_list[i][j + 1] != 'l':
                            result_names.append(tag_remove(line[0:j]))
                            j = len(result_list[i])
                        else:
                            k = j + 1
                            l = k
                            while l < len(result_list[i]):
                                if result_list[i][l] == ',':
                                    m = l
                                    l = (len(result_list[i]))
                                l += 1
                            
                            result += tag_remove(result_list[i][0:j])
                            result += ' '
                            result += tag_remove(result_list[i][k:m])
                            result_names.append(result)
                            if len(result_names) > 1:
                                result_names.pop(len(result_names) - 2)

                    j += 1
                i += 1
            j = 0
            i = 0

#NO RESULTS
            if results == 0:
                print("       [There were no results]")

#SINGLE RESULT
            elif results == 1:
                i = 0
                j = 0
                info = ['f']
                print("       [Found 1 contact]")
                while i < len(result_list[0]):
                    if result_list[0][i] == ',':
                        if i < len(result_list[0]) - 1:
                            info.append(result_list[0][i+1])
                        print(tag_replace(result_list[0][j:i]))
                        j = i + 1
                    i += 1
                print()
                
                print("       What information would you like to update?")
                print("       [Please type the character shown]")
                for letter in info:
                    if letter == 'f':
                      print("  F)  " + "First Name")
                    elif letter == 'l':
                        print("  L)  " + "Last Name")
                    elif letter == 'm':
                        print("  M)  " + "Mobile #")
                    elif letter == 'h':
                        print("  H)  " + "Home #")
                    elif letter == 'e':
                        print("  E)  " + "Email")
                    elif letter == 'b':
                        print("  B)  " + "Birthdate")

                option2 = input("       OPTION>> ")
                print()
                print("       Enter the new information.")
                new_info = input("       INFO>> ")
                new_info = (option2.lower() + new_info + ',')
                begin = False
                i = 0
                j = 0
                k = 0
                for each in content[indexes[0]]:
                    if (option2.lower() == 'f' and k == 0) or (each == option2.lower() and content[indexes[0]][k-1] == ','):
                        begin = True
                        index1 = i
                    if begin and each == ',':
                        j = i + 1
                        new = list(content[indexes[0]])
                        h = index1
                        g = j
                        while h < g:
                            new.pop(index1)
                            h += 1
                        h = index1
                        g = j
                        p = 0
                        while p < len(new_info):
                            new.insert(h, new_info[p])
                            p += 1
                            h += 1
                    i += 1
                    k += 1
                new = ''.join(new)
                content[indexes[0]] = new
                with open("phonebook.txt", 'w') as pbw:
                    for line in content:
                        pbw.write(line)
                print("       [Information updated successfully]")
                print()

#MULTIPLE RESULTS
            elif results > 1:
                print("       [Found", results, "contacts]")
                print("       Which would you like to update?")
                
                while i < results:
                    print("  " + str(i + 1) + ')  ' + result_names[i])
                    i += 1
                
                choice = int(input("       CONTACT>> "))
                print()
                i = 0
                j = 0
                info = ['f']
                while i < len(result_list[choice-1]):
                    if result_list[choice-1][i] == ',':
                        if i < len(result_list[choice-1]) - 1:
                            info.append(result_list[choice-1][i+1])
                        print(tag_replace(result_list[choice-1][j:i]))
                        j = i + 1
                    i += 1
                print()
#INFO UPDATE
                print("       What information would you like to update?")
                print("       [Please type the character shown]")
                for letter in info:
                    if letter == 'f':
                      print("  F)  " + "First Name")
                    elif letter == 'l':
                        print("  L)  " + "Last Name")
                    elif letter == 'm':
                        print("  M)  " + "Mobile #")
                    elif letter == 'h':
                        print("  H)  " + "Home #")
                    elif letter == 'e':
                        print("  E)  " + "Email")
                    elif letter == 'b':
                        print("  B)  " + "Birthdate")

                option2 = input("       OPTION>> ")
                print()
                print("       Enter the new information.")
                new_info = input("       INFO>> ")
                new_info = (option2.lower() + new_info + ',')
                begin = False
                i = 0
                j = 0
                k = 0
                stop = False
                for each in content[indexes[choice-1]]:
                    if stop == False and (option2.lower() == 'f' and k == 0) or (each == option2.lower() and content[indexes[choice-1]][k-1] == ','):
                        begin = True
                        index1 = i
                    if begin and each == ',':
                        begin = False
                        stop = True
                        j = i + 1
                        new = list(content[indexes[choice-1]])
                        h = index1
                        g = j
                        while h < g:
                            new.pop(index1)
                            h += 1
                        h = index1
                        g = j
                        p = 0
                        while p < len(new_info):
                            new.insert(h, new_info[p])
                            p += 1
                            h += 1
                    i += 1
                    k += 1
                new = ''.join(new)
                content[indexes[choice-1]] = new
                with open("phonebook.txt", 'w') as pbw:
                    for line in content:
                        pbw.write(line)
                print("       [Information updated successfully]")
                print()
                

#OPTION 5
    elif option == '5' or option.lower() == 'delete a contact' or option.lower() == 'delete':
        
        print()
        print("       Please enter the first name of the person whose contact you would like to delete:")
        name = input("       NAME>> ")
        result_list = []
        results = 0
        indexes = []
        i = 0
        
        with open("phonebook.txt", 'r') as pbr:
            
            content = pbr.readlines()
            for line in content:
                if ("f" + name) in line:
                    indexes.append(i)
                    result_list.append(line)
                    results += 1
                i += 1
            i = 0
            result = ''
            result_names = []
            
            while i < results:
                j = 0
                k = 0
                l = 0
                m = 0
                while j < len(result_list[i]):
                    result = ''
                    if result_list[i][j] == ',':
                        if result_list[i][j + 1] != 'l':
                            result_names.append(tag_remove(line[0:j]))
                            j = len(result_list[i])
                        else:
                            k = j + 1
                            l = k
                            while l < len(result_list[i]):
                                if result_list[i][l] == ',':
                                    m = l
                                    l = (len(result_list[i]))
                                l += 1
                            
                            result += tag_remove(result_list[i][0:j])
                            result += ' '
                            result += tag_remove(result_list[i][k:m])
                            result_names.append(result)
                            if len(result_names) > 1:
                                result_names.pop(len(result_names) - 2)

                    j += 1
                i += 1
            j = 0
            i = 0
            
#NO RESULTS
            if results == 0:
                print("       [There were no results]")

#SINGLE RESULT
            elif results == 1:
                i = 0
                j = 0
                print("       [Found 1 contact]")
                while i < len(result_list[0]):
                    if result_list[0][i] == ',':
                        if i < len(result_list[0]) - 1:
                            info.append(result_list[0][i+1])
                        print(tag_replace(result_list[0][j:i]))
                        j = i + 1
                    i += 1
                choice = 0
                print()

 #MULTIPLE RESULTS
            elif results > 1:
                print("       [Found", results, "contacts]")
                print("       Which would you like to delete?")
                
                while i < results:
                    print("  " + str(i + 1) + ')  ' + result_names[i])
                    i += 1
                
                choice = int(input("       CONTACT>> "))
                print()
                i = 0
                j = 0
                while i < len(result_list[choice-1]):
                    if result_list[choice-1][i] == ',':
                        print(tag_replace(result_list[choice-1][j:i]))
                        j = i + 1
                    i += 1
                print()
                
#FAILSAFE
            if results >= 1:
                print("       Are you sure you would like to delete this contact? (Y/N)")
                failsafe = input("       CONTINUE>> ")
                if failsafe.lower() == "yes" or failsafe.lower() == 'y':
                    content.pop(indexes[choice-1])
                    with open("phonebook.txt", 'w') as pbw:
                        for line in content:
                            pbw.write(line)
                    print("       [Action completed]")
                else:
                    print("       [Action cancelled]")
            print()
            

#OPTION 6
    elif option == '6' or option.lower() == 'quit':
        start = 1

    elif option.lower() == "an option" or option.lower() == "option":
        print("       Yeah okay, funny guy. Try again.")
        print()
    else:
        print("      *ERROR: Please enter a valid option")
        print()
    print("<<=+=+=+=+=+=+=+=+=+=+=+=>>")

