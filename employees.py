# print("this is a debug message")
'''
1. Given E[k] represents an employee = ["039", "4", "14", "32", "", "34", "7"], the answer is 5. It can be achieved for example by running training on days 3 and 4. This way employees number 0, 1, 2, 3 and 5 will attend the training.
Employee Availability 
Employee index 0 : E[K] employee is available on day 0 , 3 , 9
------ 
----- 
Use a dict. to store the availability of the employee for training 
key    value (tag and counter for selection count) or simply use E[K]
0       {0}
1       {2}
2       {3}
3       {0,3,5}    
4       {1,2,5}
5     
6
7       {6}
8
9       {0}     
[3,4] 
Pair the maximum dates together set + set = {0,1,2,3,5} = len(set) = 5
'''

def solution(E):
    # Implement your solution here
    # intialize our availability dictionary 
    availability = {str(day) : set() for day in range(10)}
    # print(availability)

    #populate my availability dictionary 
    for index, days in enumerate(E):
        for day in days:
            availability[day].add(index)

    # find the best two days manually 
    # print(availability)
    max_attendance = 0
    days = list(availability.keys())
    # print(days)
    # [0..9 minus the empty days]
    #iterate from day 0 to day 8
    for i in range(9):
        # iterate from day after i to day 9
        for j in range(i + 1, 10):  
            day1, day2 = days[i] , days[j]
            # calculate the number of unique employees that can attend either day 1 or 2 
            # print("day 1 :", day1)
            # print("day 2 : ", day2)
            combined_attendance = len(availability[day1].union(availability[day2]))
            # print("Combined attendance",combined_attendance)
            if combined_attendance > max_attendance:
                max_attendance = combined_attendance
    return max_attendance