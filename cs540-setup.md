# If any of the below don't work, you can try

adding "sudo" in front of the command
switching "pip" for "pip3"

# WSL

## GitHub
```
ssh-keygen  # then hit Enter until all the prompts are done
cat ~/.ssh/id_rsa.pub  # Copy the output of this command where GitHub asks you for an SSH key
```

## Python
```
sudo apt-get update  # update your installer so the Pip installation works
sudo apt install python3-pip  # install pip, which manages python packages
pip3 install flask
pip3 install requests
pip3 install python-dotenv
```

## PostgreSQL setup
```
sudo apt install postgresql
sudo service postgresql start
sudo -u postgres psql  # just testing that psql is installed. You should get an interactive prompt. Quit by entering "\q"
pip3 install psycopg2-binary
pip3 install Flask-SQLAlchemy
```

## React/Node
```
sudo apt update
sudo apt install npm
npx create-react-app my-first-app  # this will install the create-react-app tool
```
If you get an error about your node version being out of date, try
```
sudo npm install -g n
sudo n latest
```

If that still doesn't work, try the instructions [here](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/react-on-wsl).


# Mac

## GitHub
```
ssh-keygen  # then hit Enter until all the prompts are done
cat ~/.ssh/id_rsa.pub  # Copy the output of this command where GitHub asks you for an SSH key
```

## Python
```
python3 -m ensurepip --upgrade  # install pip, which manages python packages
pip3 install flask
pip3 install requests
pip3 install python-dotenv
```


## PostgreSQL setup
```
brew install postgresql
brew services start postgresql
psql -h localhost  # this is just to test out that postgresql is installed okay - type "\q" to quit
# if the above command gives you an error like "database <user> does not exist," try the workaround in this link: https://stackoverflow.com/questions/17633422/psql-fatal-database-user-does-not-exist
pip3 install psycopg2-binary
pip3 install Flask-SQLAlchemy
```

## React/Node
```
brew update
brew install node
npx create-react-app my-first-app  # this will install the create-react-app tool
```