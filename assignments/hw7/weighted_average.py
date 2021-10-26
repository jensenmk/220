def weighted_average(in_file_name, out_file_name):
    # open file(s)
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    # read file and split into appropriate lists
    total_total = 0
    grade_avg_list = []
    for line in in_file.readlines():
        name, data = line.split(':')
        data_list = data.split()

        grade_list = data_list[1::2]
        weight_list = data_list[::2]
        weighted_weight_list = []

        # change the lists of strings into a list of ints and get the weights
        # into decimal form
        for i in weight_list:
            weighted_weight_list.append(int(i) * .01)

        num_grade_list = []
        for i in grade_list:
            num_grade_list.append(int(i))

        weight_total = 0
        grade_total = 0

        for i in range(len(grade_list)):
            grade_total += num_grade_list[i] * weighted_weight_list[i]
            weight_total += weighted_weight_list[i] * 100

        if weight_total < 100:
            print(name + "'s average: Error: The weights are less than 100.", file=out_file)
        elif weight_total > 100:
            print(name + "'s average: Error: The weights are more than 100.", file=out_file)
        else:
            print(name + "'s average: " + "{:.1f}".format(round(grade_total, 2)), file=out_file)

            grade_avg_list.append(grade_total)
            total_total += grade_total

    if len(grade_avg_list) == 0:
        print('Class average:')
    else:
        avg = round(total_total / len(grade_avg_list), 1)
        print("Class average:", avg)
        in_file.close()
        out_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()
