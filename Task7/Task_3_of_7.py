# Task3: Days and Activities 
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
activities = [input(f"Enter activity for {day}: ") for day in ('Monday', 'Wednesday', 'Friday')]
days_activities = {day: activity for day, activity in zip(('Monday', 'Wednesday', 'Friday'),activities)}
print(days_activities)
