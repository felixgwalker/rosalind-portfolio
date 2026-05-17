#	Rabbits and Recurrence Relations

n = 5 #months
k = 3 #no. offspring

prev_m = curr_m = 1

for month in range(3, n+1):
	next_m = curr_m + k*prev_m
	prev_m = curr_m
	curr_m = next_m

print(curr_m)
