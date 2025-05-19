#!/bin/bash

# Check if username and token are provided as arguments
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <username> <personal_access_token>"
  exit 1
fi

username="$1"
token="$2"

# Make the curl request to the GitHub API
curl -H "Accept: application/vnd.github+json" \
  -H "Authorization: token ${token}" \
  -H "User-Agent: ${username}" \
  https://api.github.com/users/amokawa > user.json

echo "User data saved to user.json"

# executar o chmod +x http_client.sh
# para executar o sh no terminal usar ./http_client.sh