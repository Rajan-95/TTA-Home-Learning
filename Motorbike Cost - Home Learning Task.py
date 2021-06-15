# Task: Motorcycle costs £2000, print the value of the motorcycle every year until its value drops below £1000.
motorbike = 2000
year2021 = motorbike * 0.9
print("Value of bike in 2021: £" + str(year2021))
year2022 = year2021 * 0.9
print("Value of bike in 2022: £" + str(year2022))
year2023 = year2022 * 0.9
print("Value of bike in 2023: £" + str(year2023))
year2024 = year2023 * 0.9
print("Value of bike in 2024: £" + str(year2024))
year2025 = year2024 * 0.9
print("Value of bike in 2025: £" + str(year2025))
year2026 = year2025 * 0.9
print("Value of bike in 2026: £" + str(year2026))
year2027 = year2026 * 0.9
print("Value of bike in 2027: £" + str(year2027))
print("It will take 7 years for the value of the motorbike to drop below £1000.")

# A condensed version of working out the above is programmed below using the 'while' loop.

motorbike = 2000
year = 2020
# while True: <-- also works as a while statement for this program 
# but only if you include "if motorbike >= 1000 \n break"
while(motorbike > 1000):    
    print("Value of bike in year " + str(year) + ": £" + str(motorbike))
    motorbike = motorbike * 0.9
    year += 1
print("In the year " + str(year) + ", the value will depreciate below £1000")
# ^ the str(year) will display 2027 in the print statement
# this is because the last year value would be 2026 - this is the last year where the motorbike's value is above £1000


