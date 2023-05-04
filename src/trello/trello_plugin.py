
from trello import TrelloClient
import os

class Trello(object):
    def create_trello_card(self, name, description):
        api_key = os.getenv("api_key")
        api_secret = os.getenv("api_secret")
        token = os.getenv("token")
        board_id = os.getenv("board_id")

        # create a Trello client object
        client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            token=token
        )

        # get the board object for the specified board ID
        board = client.get_board(board_id)

        # create a new card on the board with the specified name and description
        lists = board.list_lists()
        list = board.get_list(lists[0].id)
        card = list.add_card(name, description)

        # print the URL of the new card
        print("New Trello card created:", card.url)



# trello = Trello()
# data = {
#     "name": "Python Card",
#     "description": "AS A Python card\nI WANT TO blank\nSO THAT I can be done!"
# }
# trello.create_trello_card(data["name"], data["description"])