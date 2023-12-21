def activity_selection(activities):
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_finish_time = activities[0][1]

    for start, finish in activities[1:]:
        if start >= last_finish_time:
            selected.append((start, finish))
            last_finish_time = finish

    return selected

# Example activities (start, finish)
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]

# Select activities
selected_activities = activity_selection(activities)
print(selected_activities)
