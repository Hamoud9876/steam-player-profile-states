this project is a work in progress.
due to the nature of steam public api avoid using players with high game count as it will most likely fail to retrieve all the data (your access will be temporarely denaid).
to overcome that problem a file with a player data is provided in the repo in data/steam_data.csv.

incase you would like to invoke the apis you can use my humble steam id, the rest of the instruction will be listed in the .env section of this document.

please use the following commands to install and run the application:
******* please make sure to read the make file before running the commands *******
make dev-setup
make run-all


requirements:
you can find all the requirements in the requirments.txt file ready to be installed. Bellow you can find a list detailing of each dependency:
requests 
pytest 
"fastapi[standard]"
postgres
pg8000
python-dotenv
aiohttp
bandit
black
coverage


.env:
this is the format of the .evn file. please fill all the variables and put them in your own .env and don't forget to add it to you .gitignore.
you would also need to get a steam public api key from the following link: https://steamcommunity.com/dev/apikey.

#db info
USERNAME=
PASSWORD=
HOST=
DATABASE=
PORT=

#api Keys
STEAM_KEY=
PLAYER_ID=76561199419972260 (as promised my player id, you can change it with yours if you want too)

