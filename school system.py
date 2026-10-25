Principal = str('Ronald')
Password = str(101112)

Login = str(input('\nEnter your login: '))
Password_register = str(input('Enter your Password: '))

if Login != Principal:
    Login = str(input("\nThis login doesn't exist. Try again: "))

while Password_register != Password:
    Password_register = str(input("\nyour pin is wrong. Try again:"))

print ("\nwelcome to the school system {}".format (Login))


Student = ['Julia','Pedro','Andrea','Joe','Cloe']
print ('\nStudent List:\n{}'.format (Student))
choice = int(input('\n1 - Add a Student\n2 - Delete a Student\n3- Exit \nChoice: '))

if choice >3:
    print ('Invalid choice')
    input ('press "enter" to exit: ')


elif choice == 1:
    print ('='*20)
    Set_Student = str(input("Enter the new Student's name: "))
    Set_Age = int(input("Enter the new Student's Age:"))
    Student.append(Set_Student)
    print ("update student list: {}".format (Student))
    input ('press "enter" to exit: ')

elif choice == 2:
    print('=' * 20)
    print('\nStudent list:')
    print(Student)

    Del_Student = input('\nDelete a student: ')

    if Del_Student in Student:
        Student.remove(Del_Student)
        print('Student Removed.')
        input ('press "enter" to exit: ')
    else:
        print('Student not found.')
        input ('press "enter" to exit: ')

    print(Student)

elif choice == 3:
    print ('Ok goodbye')
    input ('press "enter" to exit: ')
    


#Ass: 𝕭𝖎𝖌𝕱𝖆𝖙
