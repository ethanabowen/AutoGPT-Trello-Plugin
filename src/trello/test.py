import os

from dotenv import load_dotenv

from trello_plugin import Trello

load_dotenv()

trello = Trello()

def test_create_card():
    data = {
        "name": "Python Card",
        "description": "AS A Python card\nI WANT TO blank\nSO THAT I can be done!"
    }
    trello.create_trello_card(data["name"], data["description"])

def test_create_cards():
    data = {
        "cards": [
            {
            "name": "Agile Methodology",
            "description": "Agile methodology is a project management approach that emphasizes flexibility and collaboration to deliver high-quality products quickly and efficiently."
            },
            {
            "name": "DevOps",
            "description": "DevOps is a set of practices that combines software development and IT operations to shorten the systems development life cycle while delivering features, fixes, and updates frequently in close alignment with business objectives."
            }
        ]
    }

    trello.create_trello_cards(data)

#test_create_cards()