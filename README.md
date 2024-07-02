# Instagram Poster
This is a automated posting application that creates images (1080x1080) with quotes and author, sends an email to confirm that it is okay to post, once it receives a Y or N, it will post it to instgram for you or regenerate a new image.

## Installation & Usage
This can be run in 3 different ways: 1. Locally, 2. Docker & 3. Github Actions
To get it working 1. Locally:
```bash
# Run this command in your cmd:
pip install -r requirements.txt

# Ensure that the config.ini is populated with the required fields. 
# You will need to fill out instagram, email username/password as well as recipient email.
# Refer to line 38 in the posts.py file and change the path directories
# Also change how it fetches the credentials from the os to the config.ini

# Run the Python command to run the application
python app.py
```

To get it working 2. Docker:
```bash
# Ensure that the config.ini is populated with the required fields. 
# You will need to fill out instagram, email username/password as well as recipient email.
# Refer to line 38 in the posts.py file and change the path directories to /app/posts
# Also change how it fetches the credentials from the os to the config.ini

# Run the Docker build command to create the docker image (ensure youre in the working dir):
docker build -t my-python-app .

#Run the docker container
docker run -d -p 80:80 -v "C:\path\to\Directory\posts:/app/posts" my-python-app
# In my case it was docker run -d -p 80:80 -v "C:\Users\Steven\Documents\All things Code\Insta Poster\posts:/app/posts" my-python-app
```

To get it working 3. Github Actions:
```bash
# The repo is already configured to run in Github Actions at 8am UTC Monday and Thursday

# Poopulate your github secrets, the following must be filled out
INSTAGRAM_USERNAME
INSTAGRAM_PASSWORD
EMAIL_USERNAME
EMAIL_PASSWORD
# Github Secrets: Repo > Settings > Secrets and variables > Actions > Repostiory secrets.
```