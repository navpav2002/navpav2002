# import lib-s
import os
import requests
import matplotlib.pyplot as plt

# configure matplotlib to use a non-GUI backend
import matplotlib
matplotlib.use('Agg')

# set the plot style to dark background
plt.style.use('dark_background')

# retrieve the STATS_TOKEN environment variable
token = os.getenv('STATS_TOKEN')
# define headers for the GitHub API request, including authorization token
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

# list of private repositories to analyze
repos = [
    'navpav2002/react-int',
    'navpav2002/Assembly',
    'navpav2002/Docker_INT',
    'navpav2002/JS-AA1',
    'navpav2002/Web_prog',
    'navpav2002/TestAppCPP1',
    'navpav2002/eth_smart-con-0.0.1',
    'navpav2002/ThreeJS-Blender-React-Fiber-TestWeb',
    'navpav2002/AppVS'
]

# initialize a dictionary to store language data
all_languages = {}

# loop through each repository
for repo in repos:
    # make a request to GitHub API to get languages data for the repo
    response = requests.get(f'https://api.github.com/repos/{repo}/languages', headers=headers)
    # if request is successful
    if response.ok:
        repo_languages = response.json()
        # update all_languages dictionary with data from this repo
        for language, size in repo_languages.items():
            all_languages[language] = all_languages.get(language, 0) + size
    else:
        # print an error message if request failed
        print(f"Error fetching data for repo {repo}: {response.text}")

# define custom colors for the bars in the bar chart
colors = ['#33FFF3', '#008000', '#0000ff', '#ffff00', '#FF33F0', '#ff0000', '#FFA500', '#adff2f', '#ECF0F1', '#DE3163']

# extract languages and their sizes to lists for plotting
languages = list(all_languages.keys())
sizes = list(all_languages.values())

# create a figure and axis for the bar chart
fig, ax = plt.subplots(figsize=(10, 8))
# plot the bar chart
bars = ax.bar(languages, sizes, color=colors)

# set the background color of the axis
ax.set_facecolor('black')

# set the color of the axis ticks to white
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
# set the labels and title with white color
plt.xlabel('Languages', color='white')
plt.ylabel('Bytes of Code', color='white')
plt.title('Programming Languages Usage', color='white')

# add text labels above the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{int(yval)}', va='bottom', ha='center', color='white')

# set the color of the axis spines to white
for spine in ax.spines.values():
    spine.set_color('white')
    
# hide the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# add major and minor grid lines with custom style
ax.grid(which='major', linestyle='--', linewidth=0.5, color='grey')  
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='grey') 

# define the path to save the bar chart
diagram_path = 'languages_usage_chart.png'
# save the figure with a black background
plt.savefig(diagram_path, bbox_inches='tight', facecolor='black')

# check if the file was successfully saved
if os.path.exists(diagram_path):
    print(f"Bar chart saved as {diagram_path}.")
else:
    print("Error saving the bar chart.")
