import time
for i in range(10):
    print("\r",end="")
    print("Loading",i, end="")
    time.sleep(0.5)
print()