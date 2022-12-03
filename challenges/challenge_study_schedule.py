def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    count = 0
    for element in permanence_period:
        join_time = element[0]
        exit_time = element[1]
        if not isinstance(join_time, int) or not isinstance(exit_time, int):
            return None
        if join_time <= target_time <= exit_time:
            count += 1
    return count
