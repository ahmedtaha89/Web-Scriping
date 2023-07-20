from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest
url ='https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=data%20analysis'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

title_job = []
job_description=[]
Location = []
skill = []


title_jobs = soup.find_all('h2',class_='css-m604qf')
company_name = soup.find_all('a',class_='css-17s97q8')
Locations = soup.find_all('span',class_='css-5wys0k')
skills = soup.find_all('div',class_='css-y4udm8')

for i in range(len(title_jobs)):
    title_job.append(title_jobs[i].text)
    job_description.append(company_name[i].text)
    Location.append(Locations[i].text)
    skill.append(skills[i].text)
print(title_job)
print(job_description)
print(Location)
print(skill)
file_list  = [title_job,job_description,Location,skill ]
exported = zip_longest(*file_list)

# 
with open('D:\Projects\Web Scriping\Projects\wuzzuf2.csv' ,'w') as file:
    wr = csv.writer(file)
    wr.writerow(['title_job', 'company name' , 'location' , 'skills'] )
    wr.writerows(exported)

