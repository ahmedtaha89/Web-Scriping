import pandas as pd
import requests 
import csv 
from bs4 import BeautifulSoup

my_list=[]
for seats in range(900000,900050):
  response = requests.get(f'https://shbabbek.com/natega/{seats}')
  try:
   if response.status_code == 200:
     my_list.append(response)     
    
  except:
    break

print(len(my_list))

sourse = response.content
response.text
soup = BeautifulSoup(sourse,"lxml")


def extraction(response):
    soup = BeautifulSoup(response, 'lxml')
    result = {}
    result["seat_no"]=(soup.find_all("td")[21].get_text().strip())
    result["name"]=soup.find_all("td")[23].get_text().strip()
    result["total_marks"]=(soup.find_all("td")[31].get_text().strip())
    result["percentage"]=(soup.find_all("td")[33].get_text().strip())
    result["sc_name"]=soup.find_all("td")[25].get_text().strip()
    result["edu_administration"]=soup.find_all("td")[27].get_text().strip()
    #check pass or fill
    result["passed"]=1 if(soup.find_all("td")[37].get_text().split()[0]=="ناجح") else[0]
    #select division
    result["select_division"]=soup.find_all("td")[29].get_text().strip()
    #get the result of the fixed subjects
    result["arabic"]=(soup.find_all("td")[39].get_text().strip())
    result["english"]=(soup.find_all("td")[41].get_text().strip())
    result["third_lang"]=(soup.find_all("td")[43].get_text().strip())
    #extracte each division
    if result["select_division"][0]=="أدبى":
      result["history"]=(soup.find_all("td")[47].get_text().strip())
      result["geograpgy"]=(soup.find_all("td")[49].get_text().strip())
      result["philosophy"]=(soup.find_all("td")[51].get_text().strip())
      result["psychology"]=(soup.find_all("td")[53].get_text().strip())
    elif result["select_division"][0]=="علمى علوم":
        result["chemistry"]=(soup.find_all("td")[55].get_text().strip())
        result["biology"]=(soup.find_all("td")[57].get_text().strip())
        result["geology"]=(soup.find_all("td")[61].get_text().strip())
        result["physics"]=(soup.find_all("td")[65].get_text().strip())
    elif result["select_division"][0]=="علمى رياضة":
      result["chemistry"]=(soup.find_all("td")[55].get_text().strip())
      result["physics"]=(soup.find_all("td")[65].get_text().strip())
      result["pure_math"]=(soup.find_all("td")[45].get_text().strip())
      result["applied_math"]=(soup.find_all("td")[63].get_text().strip())
    #abstract addition subjects
    # try:
    #   result["relegion"]=(soup.find_all("td")[69].get_text().strip())
    #   result["nat_edu"]=(soup.find_all("td")[71].get_text().strip())
    #   result["stat_eco"]=(soup.find_all("td")[73].get_text().strip())
    # except:
    #   result['religion'] = pd.NA
    #   result['nat_edu'] = pd.NA 
    #   result['stat_eco'] = pd.NA 
    return result



soup = BeautifulSoup(my_list[0].content, 'lxml')

soup.find_all("td")[2].get_text()

extraction(my_list[3].content)


final = pd.DataFrame()  # Initialize an empty DataFrame
for i in my_list[1:]:
    source = i.content
    result = extraction(source)

    if isinstance(result, dict):
        result = pd.DataFrame(result)  # Convert the dictionary to a DataFrame
    final = pd.concat([final, result], ignore_index=True)
print(final)     
final.to_csv('D:\school\s.csv')
