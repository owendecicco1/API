from urllib import response
import requests
import json

# Make an API call and store the response.
#API = Application Program Interface
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open("output.json","w")

response_dict = r.json()

print(response_dict)

json.dump(response_dict,outfile,indent = 4)

list_of_repos = response_dict["items"]

print(f"Number of Repos: {len(list_of_repos)}")

#Explore First Repo
first_repo = list_of_repos[0]

print(first_repo)

#Print number of Keys
print(f"Number of Keys: {len(first_repo)}")

#Print each of the keys
for record in first_repo:
    print(record)

print("\nSelected information about first repository:")

print(f"Name: {first_repo['name']}")
print(f"login: {first_repo['owner']['login']}")
print(f"Stars: {first_repo['stargazers_count']}")
print(f"Html_url: {first_repo['html_url']}")
print(f"Created: {first_repo['created_at']}")
print(f"Updated: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}")
print()
print()

#print out same info for first ten
for repo in list_of_repos[:10]:
    try:
        print(f"Name: {repo['name']}")
        print(f"login: {repo['owner']['login']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Html_url: {repo['html_url']}")
        print(f"Created: {repo['created_at']}")
        print(f"Updated: {repo['updated_at']}")
        print(f"Description: {repo['description']}")  
        print()
        print()
    except:
        pass

from plotly.graph_objs import bar
from plotly import offline

repo_names, stars = [], []

# top 10 repos 

for repo in list_of_repos[:10]:
    repo_names.append(repo["name"])
    stars.append(repo["stargazers_count"])


data = [
    {
        "type": "bar",
        "x": repo_names,
        "y": stars,
        "marker": {
            "color": "rgb(60, 100, 150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
        },
        "opacity": 0.6
    }
]

my_layout = {
    "title": "Most-Starred Pytthon Projects on GitHub",
    "xaxis": {"title": "Repository"},
    "yaxis": {"title": "Stars"},
}
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename = "python_repos.html")

