# import requests to start scraping
import requests
import re
import time
r  = requests.get('https://quotes.toscrape.com/')

print(r.status_code)
text = r.text
# confition to filter our list of quotes :
condition_filter = '<span class="text" itemprop="text">'
# Lets split data by '\n'
data_split = text.split('\n')

data_desc_list = []
data_desc_re = []

start_time = time.time()
# function with regex : 
for desc in data_split:
    if(condition_filter in desc):
        clean = re.compile('<.*?>')
        data_desc_re.append(re.sub(clean, '', desc).strip())
print("Time taken: {:.6f} seconds".format(time.time() - start_time))

start_time1 = time.time()
# function with no regex
for desc in data_split:
    
    if ( condition_filter in desc):
        data_desc_list.append(desc.strip().replace(condition_filter, '').replace('</span>',''))
print("Time taken: {:.6f} seconds".format(time.time() - start_time1))

# put the result in file 
with open('quotes.txt', 'w') as f:
    for line in data_desc_re:
        f.write(line)
        f.write('\n')

author_list = []
author_condition = '<span>by <small class="author" itemprop="author">'
# Extraction the author : 
for author in data_split:
    if (author_condition in author):
        author_list.append(author.replace(author_condition,'').replace('</small>',"").strip())
# Open new file and put the authors names : 

with open('author.txt','w') as f:
    for line in author_list:
        f.write(line)
        f.write('\n')

# For know lets see how to scrapt multiple pages with one method :

for i in range(1, 11):
    url = f'https://quotes.toscrape.com/page/{i}/'
    r = requests.get(url)
    html = r.text
    with open('quotes_page.txt', 'a',encoding="UTF-8") as f:
        for line in html.split('\n'):
            if condition_filter in line:
                line = line.replace(condition_filter, '').replace('</span>','').strip()
                f.write(line)
                f.write('\n')


print(type(r.text))

