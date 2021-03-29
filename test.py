import time

t = '0:00:00.5011'

def format_time(t):
	timeArray = time.strptime(t, "%H:%M:%S.%f")
	otherStyle = time.strftime("%H:%M:%S", timeArray)
	return otherStyle

print(format_time(t))