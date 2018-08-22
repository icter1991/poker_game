# text_poker.py -- video dice poker using a text-based interface.

from pokerdie import PokerApp
from text_interface import TextInterface

inter = TextInterface()
app = PokerApp(inter)
app.run()
