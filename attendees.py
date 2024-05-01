"""
Function max_attendees(E: array of strings):
    Create a dictionary to count the number of attendees for each day from 0 -9
    The nested loop iterates through each string in the E list. For each string (representing an employee's availability), it further iterates through each character in the string. It increments the count for the corresponding day in the count
    For each employee E[i] in E:
        For each day d in E[i]:
            Increment the count of attendees for day d
    Find the two days with the highest total number of attendees:The dictionary items are then sorted based on their values (number of attendees) in descending order.
    Return the sum of attendees for these two days
"""

def max_attendees(E):
    # Create a dictionary to count the number of attendees for each day
    day_counts = {str(i): 0 for i in range(10)}

    # Count the number of attendees for each day
    for availability in E:
        for day in availability:
            day_counts[day] += 1

    # Find the two days with the highest total number of attendees
    sorted_days = sorted(day_counts.items(), key=lambda x: x[1], reverse=True)
    max_days = sorted_days[:2]

    # Return the sum of attendees for these two days
    return sum(count for day, count in max_days)

# Example usage:
E = ["039", "4", "14", "32", "", "34", "7"]
print(max_attendees(E))