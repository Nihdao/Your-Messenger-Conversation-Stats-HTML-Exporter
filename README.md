# Your Messenger Conversation Stats HTML Exporter

[![Screen](https://github.com/Nihdao/Your-Messenger-Conversation-Stats-HTML-Exporter/blob/main/assets/screen.png?raw=true "Screen")](https://github.com/Nihdao/Your-Messenger-Conversation-Stats-HTML-Exporter/blob/main/assets/screen.png?raw=true "Screen")

## Overview
Your Messenger Conversation Stats HTML Exporter is a Python project that allows you to analyze and aggregate statistics from your personnal Facebook Messenger conversations in a HTML file. Originally an introductory project during my time at school, I've revisited it to refresh my Python skills.

In summary :
- General - Statistics
- Media Statistics (photos, videos, files, audiofiles, gifs )
- Reactions Statistics (top reactions by conversation and user)
- Message Statistics (swear words, longest message, ...)

## Prerequisites
Before using this tool, ensure you have the following:

- Facebook Messenger Data: Download your Messenger data from Facebook. You’ll need this to extract conversation information. (https://accountscenter.facebook.com/info_and_permissions/dyi/)

- Python 3: Make sure you have Python 3 installed on your system. (https://www.python.org/downloads/)

## Usage
### Data Preparation & Customisation
>src/main.py

```python
config = {
    'path': './data/tlrs/message_*.json', # './data/message_*.json'
    'language': 'en', # 'en' (default) or 'fr'
}
generate_statistics_html(config)
```
**path**

Place your Messenger conversation exports (in the format messages_*.json) into the data folder of this project. You can also modify the path in the configuration if needed. The code will aggregate and sort the conversations.

**language**

By default, the tool analyzes conversations for profanity in English. You can change the language by modifying the configuration.

### Run
Navigate to the src folder.
Execute in terminal `$ python3 main.py ` to start the analysis.
It should take less than 1 or 2 minute depending of the volume to get the extraction in ./dist/output



## Credits
I’d like to acknowledge the following repositories for their contributions to the profanity detection feature:

[French Badwords List](http://https://github.com/darwiin/french-badwords-list/tree/master?tab=readme-ov-file "French Badwords List")

[Web Mech Badwords](https://github.com/web-mech/badwords/tree/main/src "Web Mech Badwords")

Feel free to explore and enhance this project further! 🚀

