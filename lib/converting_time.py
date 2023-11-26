def convert_to_24_hr(hour, minute, period):
    if period.lower() == "am":
        # Convert 12 am to 00
        hour = 0 if hour == 12 else hour
    else:
        # Convert 12 pm to 12
        hour = hour if hour == 12 else hour + 12
    
    # Format to four digit string
    time_format = f"{hour:02d}{minute:02d}"
    return time_format

# Get user input
hour = int(input("Enter the hour (1-12): "))
minute = int(input("Enter the minute (0-59): "))
period = input("Enter the period 'am' or 'pm': ")

time = convert_to_24_hr(hour, minute, period)
print(f"The time in 24 hours is: {time}")