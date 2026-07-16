import requests
from bs4 import  BeautifulSoup
url = "https://www.empireonline.com/movies/features/best-movies-2/"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")

with open("best_movies.txt","w") as file:
    for movies in reversed(soup.find_all("h2")):
        file.write(movies.get_text() + "\n")

