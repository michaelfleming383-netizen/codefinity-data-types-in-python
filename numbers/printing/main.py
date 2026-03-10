avl_mins = 60
ass_tsks = 10
# Number of completed transactions
mins_2_comp = 7
completed = avl_mins // mins_2_comp
# Number of remaining minutes
minutes = 60 % 7
# Set the number of remaining transactions
remaining_tasks = ass_tsks - completed
# Set the total time needed to complete all transactions
required_time = ass_tsks * mins_2_comp 

def calc_hrs(required_time):
    if required_time > 60:
        hrs = required_time // 60
        mins = required_time % 60
        if required_time < 120:
            time = f'{hrs} hour and {mins} minutes'
            return time
        else :
            times = f'{hrs} hours and {mins} minutes'
            return times
        
        
        #print(f"It would take {hrs} hours and {mins} minutes to complete all transactions")
        return time #print(f"It will take {time} to complete all transactions")
  
        
        
req_time = calc_hrs(required_time)
# Print the results.
print("The number of remaining transactions is", remaining_tasks)
print("The amount of time needed to complete all transactions is", req_time)
#print(f"It would take {hrs} hours and {mins} minutes")