from trello import TrelloClient
import os

class Trello:
    def __init__(self):
        self.api_key = os.environ.get("TRELLO_API_KEY")
        self.api_secret = os.environ.get("TRELLO_API_SECRET")
        self.token = os.environ.get("TRELLO_TOKEN")
        self.board_id = os.environ.get("TRELLO_BOARD_ID")
    
    def create_trello_card(self, name, description):
        # create a Trello client object
        client = TrelloClient(
            api_key=self.api_key,
            api_secret=self.api_secret,
            token=self.token
        )

        # get the board object for the specified board ID
        board = client.get_board(self.board_id)

        # create a new card on the board with the specified name and description
        lists = board.list_lists()
        list = board.get_list(lists[0].id)
        card = list.add_card(name, description)

        # print the URL of the new card
        print("New Trello card created:", card.url)
