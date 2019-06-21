def extract_data(filename):
    with open(filename, 'r') as info_file:
        student_data = {}
        for line in info_file:
            line = line.split(',')
            name = line[0]
            score = int(line[1])
            if name not in student_data:
                student_data[name] = []
            student_data[name].append(score)
        return (student_data.items())

data  = extract_data('C:/Users/46921166678/Python-Homework1/info.txt')
highest_averages = sorted(data, key=lambda x: sum(x[1])/float(len(x[1])), reverse=True)
highest_scores = sorted(data, key=lambda x: max(x[1]), reverse=True)

def print_function(x, y):
    print("{}, {}".format(x, y))

for name, score in highest_scores:
    print_function(name, max(score))

for name, score in highest_averages:
    print_function(name, sum(score)/float(len(score)))