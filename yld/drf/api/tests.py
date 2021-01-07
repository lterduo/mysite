from django.test import TestCase

# Create your tests here.
import time
i = 0
while True:
    time.sleep(1)
    with open('1.txt', 'a+') as f:
        f.writelines(i)
        f.close()
    i += i
