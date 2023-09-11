# discord-message-scraper
simple discord message scraper using the API

* go to discord.com in your browser
* 
* go to your desire server
* 
- press ctrl+shift+i to open the development console
- 
- then go to network -> headers and start typing then you'll see messages?=limit=50
- 
- click on it and goto headers and grab the Authorization token that will be under Accept-Language if you scroll down
- 
- It'll look similar to a token
- 
- paste that into the authorization string
- 
- then grab your channel id so this would be like general -> copy channel id and then paste it into the retrieve_messages within the ' '
- 
- run the file and it'll catch every message that gets sent there 
