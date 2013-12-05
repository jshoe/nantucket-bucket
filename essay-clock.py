import datetime
now = datetime.datetime.now()

words_to_write = int(input("How many words do you need to write? "))

print("")
start = input('Enter the date and time you started the essay, in YYYY-MM-DD-HH-MM format, with HH in 24-hour format and 00 for any 0s: ')
year, month, day, hour, minute = map(int, start.split('-'))
start = datetime.datetime(year, month, day, hour, minute)

print("")
due = input('Enter the date and time the essay is due, in YYYY-MM-DD-HH-MM format, with HH in 24-hour format and 00 for any 0s: ')
year, month, day, hour, minute = map(int, due.split('-'))
due = datetime.datetime(year, month, day, hour, minute)

print("")
print("Essay start time: " + str(start))
print("Essay due time: " + str(due))

def clock():
    now = datetime.datetime.now()
    time_left = due - now
    
    print("")
    print("Time left: " + str(time_left))
    print("Current time: " + str(now))

    since_start = now - start
    time_total = due - start
    percent_so_far = since_start / time_total
    words_so_far = percent_so_far * words_to_write
    
    print("")
    print("You should have written " + str(words_so_far) + " words so far.")
    
    print("")
    user = int(input("Enter 1 to refresh the clock: "))
    if user is not 1:
        return
    clock()
clock()
