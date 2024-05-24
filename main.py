seconds = 9876453
days = seconds // (24 * 3600)
print(days)
seconds = seconds % (24 * 3600)
hours = seconds // 3600
print(hours)
seconds = seconds % 3600
minutes = seconds // 60
print(minutes)
seconds = seconds % 60
print(seconds)
current_time = str(days) + "day, " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
print(current_time)