def extract_data(filename):
    with open(filename, 'r') as info_file:
        info_file.readline()
        name = []
        grades = []
        for line in info_file:
            words = line.split(',')
            name.append(words[0])
            grades.append(int(words[1]))
        name = name[:-1]     
        grades = grades[:-1] 
        return name, grades

name, grades = extract_data('C:/Users/46921166678/Python-Homework1/info.txt')
print(name)
print(grades)
