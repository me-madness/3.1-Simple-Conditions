hour = int(input())
minute = int(input()) + 15


if minute > 60:
    hour += 1
    minute = minute - 60
if hour >= 24:
        hour = hour - 24
if minute < 10:
    print((str(hour) + ':0' + str(minute)))
    pass        
print(str(hour) + ':' + str(minute))        