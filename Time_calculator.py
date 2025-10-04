def add_time(start, duration, day=None):
    # Days of the week for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Add minutes
    end_minute = start_minute + dur_minute
    extra_hour = end_minute // 60
    end_minute = end_minute % 60

    # Add hours
    end_hour = start_hour + dur_hour + extra_hour
    days_later = end_hour // 24
    end_hour = end_hour % 24

    # Convert back to 12-hour format
    if end_hour == 0:
        display_hour = 12
        display_period = "AM"
    elif 1 <= end_hour < 12:
        display_hour = end_hour
        display_period = "AM"
    elif end_hour == 12:
        display_hour = 12
        display_period = "PM"
    else:
        display_hour = end_hour - 12
        display_period = "PM"

    # Format minutes
    display_minute = f"{end_minute:02d}"

    # Build result
    new_time = f"{display_hour}:{display_minute} {display_period}"

    # Handle optional weekday
    if day:
        start_day_index = days_of_week.index(day.capitalize())
        end_day_index = (start_day_index + days_later) % 7
        new_time += f", {days_of_week[end_day_index]}"

    # Handle days later text
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
