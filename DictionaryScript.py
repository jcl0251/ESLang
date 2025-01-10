import re
from bs4 import BeautifulSoup
import requests
import csv
import sqlite3

connection = sqlite3.connect("C:/Users/colli/OneDrive/Desktop/learnToCode/SQL/db/myDatabase.db")
cursor = connection.cursor()

url = "http://www.cubamania.it/argot-cubano-dizionario"

ñ = "n-2"


#pattern = re.compile("(?<=\<strong\>)(.*)(?=\.- \<\/strong\>)")

with open('C:/Users/colli/OneDrive/Desktop/learnToCode/book1.csv', 'w', encoding='utf-8', errors='ignore', newline='') as f:
    writer = csv.writer(f)
    for page in range(97, 123):
        print(page)
        html_text = requests.get(f"{url}/{chr(page)}/?lang=en")
        soup = BeautifulSoup(html_text.text, 'lxml')
        rows = soup.find_all("p", style="text-align: justify;")
        
        newRows = []
        for row in rows:
            data = row.get_text().split(".- ")

            if len(data)==2:
                newRows.append(data)

            print(data)

        writer.writerows(newRows)
        cursor.executemany("INSERT INTO Definitions VALUES (?, ?)", newRows)

    print("165")
    html_text = requests.get(f"{url}/{ñ}/?lang=en")
    soup = BeautifulSoup(html_text.text, 'lxml')
    rows = soup.find_all("p", style="text-align: justify;")
    newRows = []
    for row in rows:
        data = row.get_text().split(".- ")

        if len(data)==2:
            newRows.append(data)

        print(data)
    writer.writerows(newRows)
    cursor.executemany("INSERT INTO Definitions VALUES (?, ?)", newRows)

with open('C:/Users/colli/OneDrive/Desktop/learnToCode/book1.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    no_records = 0
    for row in csv_reader:
        connection.commit()
        no_records += 1
connection.close()
print('\n{} Records Transferred'.format(no_records))
        






#<p style="text-align: justify;"><strong>Baba.- </strong>Padre</p>



