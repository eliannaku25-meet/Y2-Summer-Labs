python-review.py

import random
temp = []
temp_sum= 0
for i in range(7):
	temp.append(random.randint(26,41))
	
days_of_the_week = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
good_days_count = 0
for i in range(7):
	if temp[i] % 2 == 0:
		good_days_count = good_days_count + 1
		
highest_temp = 0 
lowest_temp = 40
highest_temp_day='sunday'
lowest_temp_day='sunday'
for i in range(7):
	if temp[i] > highest_temp: 
		highest_temp = temp[i]
		highest_temp_day = days_of_the_week[i]
		
	if temp[i] < lowest_temp:
		lowest_temp = temp[i]
		lowest_temp_day = days_of_the_week[i]
		
for i in range(7):
	temp_sum = temp[i] + temp_sum
average_sum = temp_sum / 7



for i in range(7):
	print(days_of_the_week[i],':', temp[i])
print("Shelly had" , good_days_count, "good days") 
print("The hottest temperature was: " , highest_temp, 'on', highest_temp_day)
print("The lowest temperature was: " ,lowest_temp , "on" , lowest_temp_day)
print( "The average temperature was: " , average_sum)

for i in range(7):
	if temp[i] > average_sum :
		print( "The days of the week where the temperature was above average were: " , days_of_the_week[i])