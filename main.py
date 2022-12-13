import sys

list_with_str = []

def task1():
    country_input = sys.argv[3]
    years_input = sys.argv[4]

    sum_gold = 0
    sum_silver = 0
    sum_bronze = 0

    with open("athlete_events.tsv", "r") as file:
        head_line = file.readline()
        while True:
            line = file.readline()
            if not line:
                break

            split_line = line.split("\t")
            name = split_line[1]
            country_name = split_line[6]
            country_noc = split_line[7]
            year = split_line[9]
            sport = split_line[12]
            medal = split_line[14]

            if medal == "NA\n":
                continue
            if country_input == country_noc and years_input == year or country_input == country_name and years_input == year:
                if medal == "Gold\n":
                    sum_gold += 1
                if medal == "Silver\n":
                    sum_silver += 1
                if medal == "Bronze\n":
                    sum_bronze += 1
                if sum_gold + sum_silver + sum_bronze <= 10:
                    print(f"{name} - {sport} - {medal}")
                    list_with_str.append(f"{name} - {sport} - {medal}")

        if 0 < sum_gold + sum_silver + sum_bronze < 10:
            print("Less than 10 medals!")

        if sum_gold + sum_silver + sum_bronze == 0:
            print("Incorrect input")
            exit()
        print(f"Gold medals - {sum_gold}, Silver medals - {sum_silver}, Bronze medals - {sum_bronze}")
        list_with_str.append(f"Gold medals - {sum_gold}, Silver medals - {sum_silver}, Bronze medals - {sum_bronze}")

def output_w(listik):
    file_output = sys.argv[6]
    with open(file_output, "w") as output:
        for line in listik:
            output.write(line)


def task2():
    years_input = sys.argv[3]

    with open("athlete_events.tsv", "r") as file:
        head_line = file.readline()
        while True:
            line = file.readline()
            if not line:
                break

            split_line = line.split("\t")
            country_name = split_line[6]
            year = split_line[9]
            medal = split_line[14]

            if medal == "NA\n":
                continue
            if years_input == year:
                print(f"{country_name} - {medal}")

def task3():
    countries = sys.argv[3:]
    for country_input in countries:
        result = {}
        list_with_amount_of_medals = []
        with open("athlete_events.tsv", "r") as file:
            head_line = file.readline()
            while True:
                line = file.readline()
                if not line:
                    break

                split_line = line.split("\t")
                country_name = split_line[6]
                year = split_line[9]
                medal = split_line[14]

                if medal == "NA\n":
                    continue
                if country_input == country_name:
                    if year not in result:
                        result[year] = [medal]
                    else:
                        result[year].append(medal)
            result_keys = list(result.keys())
            result_values = list(result.values())
            for i in range(len(result_values)):
                list_with_amount_of_medals.append(len(result_values[i]))
                max_value = max(list_with_amount_of_medals)
                index = [index for index, item in enumerate(list_with_amount_of_medals) if item == max_value][0]
            print(f"{country_input} - {result_keys[index]} - {max_value}")

def main():
    if sys.argv[2] == "-medals":
        task1()
        if len(sys.argv) > 5:
            if sys.argv[5] == "-output":
                output_w(list_with_str)
    if sys.argv[2] == "-total":
        task2()
    if sys.argv[2] == "-overall":
        task3()
    else:
        pass


if __name__ == '__main__':
    main()
