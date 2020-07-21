import re

test_string = 'hello2018-12-01    heo helo hello helllo'
test_string1 = '叶  睿  饶  璟'
# result = re.search('l',test_string)
# result = re.findall('\d',test_string)
# result = re.findall('hel?o',test_string)
# result = re.search('hello(.*) heo',test_string)
result = test_string1.replace(' ','')
# result = re.sub('-','=',test_string)
print(result)

if '叶睿' in test_string1.replace(' ',''):
    print('in')
