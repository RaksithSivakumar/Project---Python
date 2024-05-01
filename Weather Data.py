
def get_user_input():
    temps = []
    number_of_temps = int(input("How many temperatures would you like to enter? "))
    for i in range(number_of_temps):
        temp = float(input(f"Enter temperature #{i+1}: "))
        temps.append(temp)
    return temps

def analyze_temperatures(temps):
    average_temp = sum(temps) / len(temps)
    highest_temp = max(temps)
    lowest_temp = min(temps)
    return average_temp, highest_temp, lowest_temp

temperatures = get_user_input()

average, highest, lowest = analyze_temperatures(temperatures)

print(f"Average Temperature: {average:.1f}°C")
print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")
