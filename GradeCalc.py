def processMenu():
    print('Welcome to the Project Management System')
    print('----------------------------------------')
    print('<1> Read the File/Generate Report')
    print('<2> Create a File')
    print('<3> Highest Grade')
    print('<4> Lowest Grade')
    print('<999> End the Program')

    while True:
        try:
            user_input = int(input('Please select an option from the menu: '))
            if user_input == 1 or user_input == 2 or user_input == 3 or user_input == 4 or user_input == 999:
                break
            print('** Error: Invalid menu option selected, try again\n')
            print('Welcome to the Project Management System')
            print('----------------------------------------')
            print('<1> Read the File/Generate Report')
            print('<2> Create a File')
            print('<3> Highest Grade')
            print('<4> Lowest Grade')
            print('<999> End the Program')
        except:
            print('** Error: Menu selection must be an integer\n')
            print('Welcome to the Project Management System')
            print('----------------------------------------')
            print('<1> Read the File/Generate Report')
            print('<2> Create a File')
            print('<3> Highest Grade')
            print('<4> Lowest Grade')
            print('<999> End the Program')

    return user_input


def processFile():
    try:
        filename = input('Enter the file name you wish to display: ')
        read_file = open(filename, 'r')
        read_line = read_file.readline()
        num_grades = 0
        total_grades = 0
        while '' != read_line:
            num_grades += 1
            cur_name = read_line.rstrip('\n')
            cur_grade = read_file.readline().rstrip('\n')
            total_grades += float(cur_grade)
            print(cur_name + ' :' + format(float(cur_grade), '10.2f'))
            read_line = read_file.readline()

        avg_grade = total_grades / num_grades
        print('Total grades found for this student:  ' + str(num_grades))
        print('Average grade:  ' + str(avg_grade))
        if avg_grade >= 90:
            letter_grade = 'A'
        elif avg_grade >= 80:
            letter_grade = 'B'
        elif avg_grade >= 70:
            letter_grade = 'C'
        elif avg_grade >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        print('Letter grade assigned:  ' + letter_grade)
        print('\n')
        read_file.close()

    except:
        print('** Error: File not found\n')


def createFile():
    new_filename = input('Enter the file name you wish to create: ')
    write_file = open(new_filename, 'w')
    print('Data Entry: Type END when finished')
    assignment_name = input('Enter the name of the project (END to quit): ')
    while assignment_name != 'END':
        try:
            grade = float(input('Enter the percentage grade awarded: '))
            if grade < 0 or grade > 100:
                print('** Error: Needs to be a numeric value between 0 and 100')
            else:
                write_file.write(assignment_name + '\n')
                write_file.write(str(grade) + '\n')
        except:
            print('** Error: Needs to be a numeric value between 0 and 100')

        assignment_name = input('Enter the name of the project (END to quit): ')
    print('\n')
    write_file.close()


def highestGrade():
    try:
        filename = input('Enter the file name you wish to search: ')
        max_file = open(filename, 'r')
        max_num = 0
        cur_line = max_file.readline()
        while cur_line != '':
            cur_grade = max_file.readline()
            if float(cur_grade) > max_num:
                max_num = float(cur_grade)
            cur_line = max_file.readline()
        return max_num
    except:
        print('** Error: File not found\n')


def lowestGrade():
    try:
        filename = input('Enter the file name you wish to search: ')
        min_file = open(filename, 'r')
        cur_line = min_file.readline()
        min_num = float(min_file.readline())
        cur_line = min_file.readline()
        while cur_line != '':
            cur_grade = min_file.readline()
            if float(cur_grade) < min_num:
                min_num = float(cur_grade)
            cur_line = min_file.readline()
        return min_num
    except:
        print('** Error: File not found\n')


def main():
    user_input = processMenu()
    while user_input != 999:
        if user_input == 1:
            processFile()
        if user_input == 2:
            createFile()
        if user_input == 3:
            print('Highest grade found in the file is:   ' + str(highestGrade()) + '\n')
        if user_input == 4:
            print('Lowest grade found in the file is:  ' + str(lowestGrade()) + '\n')
        user_input = processMenu()


if __name__ == '__main__':
    main()
