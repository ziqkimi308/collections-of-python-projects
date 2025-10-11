# Import 
import requests
from bs4 import BeautifulSoup

# Main code
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
eo_website_text = response.text

soup = BeautifulSoup(eo_website_text, "html.parser")
# print(soup.prettify())

# Slice the first heading
heading_all = soup.find_all("h2")[1:]
# print(heading_all)

heading = [title.getText() for title in heading_all]

# Reverse the list
heading.reverse()

# Create a list of top movies
with open("./movies.txt", "w") as file:
	for title in heading:
		file.write(f"{title}\n")
print("List successfully written!")
