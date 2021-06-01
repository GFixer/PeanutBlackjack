import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, \
    QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5 import QtCore
from cardplay import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.window = QWidget()

    def initUI(self):
        """All the buttons and labels defined"""
        self.label1 = QLabel(self)
        self.label1.setText(str("   ".join(hand.hand_variable)))
        self.label2 = QLabel(self)
        self.label2.setText(str(hand.hand_score))
        self.labelwin = QLabel(self)
        self.labelwin.setText("----------------------")
        self.label3 = QLabel(self)
        self.label3.setText("##   " + str("   ".join(comp_hand.hand_shown_variable)))
        self.label4 = QLabel(self)
        self.label4.setText(str(comp_hand.visible_score) + "+")

        self.btn1 = QPushButton("Deal another")
        self.btn1.setCheckable(True)
        self.btn1.clicked.connect(self.dealAnother)
        self.btn2 = QPushButton("Pass")
        self.btn2.clicked.connect(self.passTurn)
        self.btn3 = QPushButton("Restart")
        self.btn3.clicked.connect(lambda: self.restartGame())
        self.btn4 = QPushButton("Exit")
        self.btn4.clicked.connect(QApplication.instance().quit)

    def dealAnother(self):
        """Add another card to player's hand"""
        hand.add_handcard(deck, 1)
        self.label1.setText(str("   ".join(hand.hand_variable)))
        hand.count_hand()
        self.label2.setText(str(hand.hand_score))
        self.checkInstantEnd()

    def passTurn(self):
        """Pass the move to the computer"""
        self.computerMoves()
        self.checkWin()

    def computerMoves(self):
        if comp_hand.hand_score < 17:
            comp_hand.add_handcard(deck, 1)
            comp_hand.count_hand()
            comp_hand.count_visible_hand()
            self.label3.setText(str("   ".join(comp_hand.hand_variable)))
            self.label4.setText(str(comp_hand.visible_score) + "+")
            self.computerMoves()

    def checkInstantEnd(self):
        if hand.hand_score == 21:
            self.labelwin.setText("-------You won!-------")
            self.btn1.setDisabled(True)
            self.btn2.setDisabled(True)
            self.label4.setText(str(comp_hand.hand_score))
            self.label3.setText(str("   ".join(comp_hand.hand_variable)))
        if hand.hand_score > 21:
            self.labelwin.setText("-------You lost!------")
            self.btn1.setDisabled(True)
            self.btn2.setDisabled(True)
            self.label4.setText(str(comp_hand.hand_score))
            self.label3.setText(str("   ".join(comp_hand.hand_variable)))

    def checkWin(self):
        if hand.hand_score > comp_hand.hand_score or comp_hand.hand_score > 21:
            self.labelwin.setText("-------You won!-------")
            self.btn1.setDisabled(True)
            self.btn2.setDisabled(True)
            self.label4.setText(str(comp_hand.hand_score))
            self.label3.setText(str("   ".join(comp_hand.hand_variable)))
        elif hand.hand_score < comp_hand.hand_score:
            self.labelwin.setText("-------You lost!------")
            self.btn1.setDisabled(True)
            self.btn2.setDisabled(True)
            self.label4.setText(str(comp_hand.hand_score))
            self.label3.setText(str("   ".join(comp_hand.hand_variable)))
        else:
            self.labelwin.setText("-----It's a draw!-----")
            self.btn1.setDisabled(True)
            self.btn2.setDisabled(True)
            self.label4.setText(str(comp_hand.hand_score))
            self.label3.setText(str("   ".join(comp_hand.hand_variable)))

    @staticmethod
    def restartGame():
        """Hard resetting the app. May change later to soft reset"""
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)

    def updateWindow(self):
        """Create the window"""
        self.setWindowTitle('Peanut Blackjack')
        self.setGeometry(1400, 1200, 680, 80)
        # window.move(600, 715)

        # The outer layout is defined
        self.outerLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.midLayout = QVBoxLayout()
        self.mid1lay = QHBoxLayout()
        self.mid2lay = QHBoxLayout()
        self.midwinlay = QHBoxLayout()
        self.mid3lay = QHBoxLayout()
        self.mid4lay = QHBoxLayout()
        self.lowerLayout = QHBoxLayout()

        # Inner layouts are defined
        self.topLayout.addWidget(QLabel('<h2>Peanut Blackjack</h2>'))

        self.mid1lay.addWidget(QLabel("Your cards: "))
        self.mid1lay.addWidget(self.label1)
        self.mid2lay.addWidget(QLabel("Your score: "))
        self.mid2lay.addWidget(self.label2)

        self.midwinlay.addWidget(self.labelwin)

        self.mid3lay.addWidget(QLabel("Opponent cards: "))
        self.mid3lay.addWidget(self.label3)
        self.mid4lay.addWidget(QLabel("Opponent score: "))
        self.mid4lay.addWidget(self.label4)

        self.lowerLayout.addWidget(self.btn1)
        self.lowerLayout.addWidget(self.btn2)
        self.lowerLayout.addWidget(self.btn3)
        self.lowerLayout.addWidget(self.btn4)

        # Build the outer layout using inner layouts
        self.outerLayout.addLayout(self.topLayout)
        self.outerLayout.addLayout(self.midLayout)
        self.outerLayout.addLayout(self.lowerLayout)
        self.midLayout.addLayout(self.mid1lay)
        self.midLayout.addLayout(self.mid2lay)
        self.midLayout.addLayout(self.midwinlay)
        self.midLayout.addLayout(self.mid3lay)
        self.midLayout.addLayout(self.mid4lay)
        self.setLayout(self.outerLayout)


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)


def main():
    pass


if __name__ == "__main__":
    # game = GameLogic()
    deck = Deck()
    hand = Hand()
    comp_hand = CompHand()
    deck.shuffle_deck()
    hand.add_handcard(deck, 2)
    hand.count_hand()
    comp_hand.add_handcard(deck, 2)
    comp_hand.count_hand()
    comp_hand.count_visible_hand()

    app = QApplication([])
    window = MyWindow()
    window.initUI()
    window.updateWindow()

    window.show()
    sys.exit(app.exec_())
