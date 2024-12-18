from datetime import datetime

now = datetime.now()
timeSecStr = now.strftime("%Y-%m-%d %H:%M:%S")
timeMilStr = now.strftime("%Y-%m-%d_%H-%M-%S_%f")
print(timeSecStr)