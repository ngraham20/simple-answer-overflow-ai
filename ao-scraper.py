import requests
from bs4 import BeautifulSoup

url = "https://www.answeroverflow.com/m/1283590358617296896"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
thread = soup.find('div', {"class": "flex flex-col gap-4"})

history = []
for comment in thread.find_all("div", {"class": "p-2"}):
    # print(comment)
    user = comment.select('a[href*="/u/"]')[0].text
    response = comment.find('div', {"class": "text-primary"}).text
    history.append((user, response))


for comment in history:
    print(f"{comment[0]}: {comment[1]}")

solution = soup.select('div[id*="solution-"]')[0]
solution_user = solution.select('a[href*="/u/"]')[0].text
solution_response = solution.find('div', {"class": "text-primary"}).text

print("----- SOLUTION -----")
print(f"{solution_user}: {solution_response}")

