import datetime

#task 1

# day = datetime.datetime.today()
# new_day = day - datetime.timedelta(days=5)

# print(new_day.strftime("%Y-%m-%d"))

#----------------------------------------------------------------------------

#task 2

# today = datetime.datetime.today()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)

# print("yesterday:", yesterday.strftime("%Y-%m-%d"))
# print("tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#-------------------------------------------------------------------------------

#task 3

# now = datetime.datetime.today()

# without_ms = now.replace(microsecond=0)

# print(now)
# print(without_ms)


#-----------------------------------------------------------------------------------

#task 4
# format_str = "%Y-%m-%d %H:%M:%S"
# date1_str = input()
# date2_str = input()


# date1 = datetime.datetime.strptime(date1_str, format_str)
# date2 = datetime.datetime.strptime(date2_str, format_str)


# difference = abs((date2 - date1).total_seconds())


# print( int(difference))