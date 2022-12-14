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
    result = dict()

    with open("athlete_events.tsv", "r") as file:
        head_line = file.readline()
        while True:
            line = file.readline()
            if not line:
                break

            split_line = line.split("\t")
            country_name = split_line[6]
            year = split_line[9]
            medal = split_line[14].replace("\n", "")

            if medal == "NA":
                continue
            if years_input == year:
                if country_name not in result:
                    result[country_name] = [medal]
                else:
                    if medal not in result[country_name]:
                        result[country_name].append(medal)
    for k, v in result.items():
        a = " - ".join(v)
        print(f"{k} - {a}")


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


def task4_first_year_and_country(country_input):
    result_years = {}
    with open("athlete_events.tsv", "r") as file:
        head_line = file.readline()
        while True:
            line = file.readline()
            if not line:
                break

            split_line = line.split("\t")
            country_name = split_line[6]
            year = split_line[9]
            city = split_line[11]

            if country_input == country_name:
                if country_input not in result_years:
                    result_years[country_input] = [year]
                else:
                    result_years[country_input].append(year)
                first_year = min(list(result_years.values())[0])
                if first_year == year:
                    first_city = city

    print(f"First year: {first_year}")
    print(f"First city: {first_city}")


def task4_max_min_medals(country_input):
    result_medals = {}
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
                if year not in result_medals:
                    result_medals[year] = [medal]
                else:
                    result_medals[year].append(medal)
        result_keys = list(result_medals.keys())
        result_values = list(result_medals.values())
        for i in range(len(result_values)):
            list_with_amount_of_medals.append(len(result_values[i]))
            max_value = max(list_with_amount_of_medals)
            min_value = min(list_with_amount_of_medals)
            index_max = [index for index, item in enumerate(list_with_amount_of_medals) if item == max_value][0]
            index_min = [index for index, item in enumerate(list_with_amount_of_medals) if item == min_value][0]
    print(f"Most successful year - {result_keys[index_max]}, amount of medals - {max_value}")
    print(f"Least successful year - {result_keys[index_min]}, amount of medals - {min_value}")


def task4_average_medals(country_input):
    result_medals = {}
    amount_gold = 0
    amount_silver = 0
    amount_bronze = 0
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
                if year not in result_medals:
                    result_medals[year] = [medal]
                else:
                    result_medals[year].append(medal)
        result_keys = list(result_medals.keys())
        result_values = list(result_medals.values())
        amount_of_years = len(result_keys)
        for i in range(amount_of_years):
            list_medals = result_values[i]
            for index in range(len(list_medals)):
                if list_medals[index] == "Gold\n":
                    amount_gold += 1
                if list_medals[index] == "Silver\n":
                    amount_silver += 1
                if list_medals[index] == "Bronze\n":
                    amount_bronze += 1
        average_gold = amount_gold / amount_of_years
        average_silver = amount_silver / amount_of_years
        average_bronze = amount_bronze / amount_of_years
    print(f"Average gold medals - {average_gold}, average silver medals - {average_silver}, average bronze medals - {average_bronze}")


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
    if sys.argv[2] == "-interactive":
        country_input = input("Please write your country:")
        task4_first_year_and_country(country_input)
        task4_max_min_medals(country_input)
        task4_average_medals(country_input)
    else:
        pass


if __name__ == '__main__':
    main()
