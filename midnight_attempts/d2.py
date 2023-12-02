
import requests

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', 
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}',
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
    print(f'You are about to submit the follwing answer:')
    print(f'>>>>>>>>>>>>>>>>> {answer}')
    input('Press enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer',
                             headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print('VERDICT : ALREADY SOLVED')
    else:
        print('VERDICT : OK !')

AOC_COOKIE = '53616c7465645f5f0be3dfbce64c428b05c9004ca638590b3709abbd839084a2c730ff2e70fd906f64f728824e2423a8d9d7ff211f13e56c03f212edfc252b65'
YEAR = '2023'
DAY = 2
PART = 1

import itertools
import re

s = get_input(DAY).strip() # the daily input is stored in s
#s = get_example(DAY, offset=1).strip() # the daily example is stored in test

s = [x for x in s.split("\n")]
T_RED = 12
T_GREEN = 13
T_BLUE = 14
ans = 0
for i in s:
    # get all the numbers and the word after them
    spl = re.findall(r'\d+|[a-zA-Z]+', i)
    red = 0
    blue = 0
    green = 0
    impossible = False
    for idx, val in enumerate(spl):
        if val.isnumeric():
            if spl[idx+1] == 'red':
                if int(val) > red:
                    red = int(val)
            elif spl[idx+1] == 'green':
                if int(val) > green:
                    green = int(val)
            elif spl[idx+1] == 'blue':
                if int(val) > blue:
                    blue = int(val)  
    ans += red * green * blue

print(ans)


print(f'Answer for part {ans}')
#submit(DAY, PART, ans)