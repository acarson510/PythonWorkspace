import pandas as pd
import concurrent.futures
import requests
import time

def some_function(a):
    return (a + 5) / 2
    
my_formula = [some_function(i) for i in range(10)]
#print(my_formula)
filtered = [i for i in range(20) if i%2==0]
print(filtered)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]


out = []
CONNECTIONS = 100
TIMEOUT = 5

tlds = []
uri = 'https://randomuser.me/api/?results=10'

response = requests.get(uri)
a = response.json()

maxRowCount = 4
startCount = 1
while startCount < maxRowCount:
    tlds.append(uri.format(startCount))
    print(uri)
    startCount += 1

#tlds = open('../data/sample_1k.txt').read().splitlines()
urls = ['https://{}'.format(x) for x in tlds[1:]]

def load_url(url, timeout):
    ans = requests.head(url, timeout=timeout)
    print(ans.status_code)
    return ans.status_code

with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
    future_to_url = (executor.submit(load_url, url, TIMEOUT) for url in urls)
    time1 = time.time()
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            data = future.result()
        except Exception as exc:
            data = str(type(exc))
        finally:
            out.append(data)

            print(str(len(out)),end="\r")

    time2 = time.time()

print(f'Took {time2-time1:.2f} s')
print(pd.Series(out).value_counts())

