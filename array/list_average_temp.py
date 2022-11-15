def calculate_average_temperature():
    number_of_days = input('Enter number of days: ')

    if not number_of_days.isdigit():
        return 'Number of days should be a number'

    temperature_list = []

    for n in range(int(number_of_days)):
        try:
            temperature_list.append(float(input(f'Enter day {n+1} temperature: ')))
        except ValueError:
            return 'Temperature should be a float'

    average_temp = sum(temperature_list) / len(temperature_list)
    result_message = f'Average temperature for {number_of_days} days is {average_temp:.1f}'

    above_average = [temp for temp in temperature_list if temp > average_temp]

    if above_average:
        result_message += f'\n{len(above_average)} day(s) above average: {", ".join(str(temp) for temp in above_average)}'

    return result_message


print(calculate_average_temperature())
