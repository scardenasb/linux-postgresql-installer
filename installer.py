import os


# Create the file repository configuration:
os.system('sudo sh -c - echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list')

# Import the repository signing key:
os.system('wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -')

# Update the package lists:
os.system('sudo apt-get update')

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
os.system('sudo apt-get -y install postgresql')
