# Calculate the number of completed transactions
#completed = 
# Calculate the number of remaining minutes
avl_minutes = 60
mins_per_trans = 7
completed = avl_minutes // mins_per_trans
minutes = avl_minutes % mins_per_trans 
# Print these values
print("The number of completed transactions is", completed)
print("The number of remaining minutes is", minutes)