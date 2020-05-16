import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

URL = 'https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations/results-previous.html'

res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

scores = [
    int(re.findall(r'\d+', str(p_data))[0])
    for p_data in soup.find_all('p')
    if 'CRS score' in str(p_data)
]
dates = [
    # str(p_data).split('#')[1]
    str(re.findall(r'#(.*)</h3>', str(p_data))[0]).split('–')[0] if '–' in str(p_data) else str(re.findall(r'#(.*)</h3>', str(p_data))[0]).split('-')[0]
    for p_data in soup.find_all('h3')
    if '#' in str(p_data)
]
dates.reverse()
scores.reverse()
plt.plot(dates[-24:], scores[-24:], label="crs_score")
plt.legend()
plt.show()
