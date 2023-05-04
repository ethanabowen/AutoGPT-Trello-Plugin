import os

from dotenv import load_dotenv

from trello_plugin import Trello

load_dotenv()

trello = Trello()
data = {
    "name": "Python Card",
    "description": "AS A Python card\nI WANT TO blank\nSO THAT I can be done!"
}
trello.create_trello_card(data["name"], data["description"])