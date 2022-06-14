import sys
from KubicLogic import *

from PyQt5.QtCore import Qt, QRect, QRectF, QLine
from PyQt5.QtGui import QColor, QPainter, QBrush, QFont, QTextOption
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class PyQtGame(QWidget):
    def __init__(self):
        super(PyQtGame, self).__init__()
        self.game = Kubic(4)
        self.colors = {
            1: QColor(0xFF0000),
            2: QColor(0xFFFF00),
            3: QColor(0x00FF00),
            4: QColor(0x0000FF)
        }
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 700)
        self.centerWindow()
        self.setWindowTitle("KubicaRubika")
        self.show()

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    """
    Управление:
    -стрелки перемещение
    -WASD вращение
    !!!Только англ.раскладка!!!
    """
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.game.up()
        elif e.key() == Qt.Key_Down:
            self.game.down()
        elif e.key() == Qt.Key_Left:
            self.game.left()
        elif e.key() == Qt.Key_Right:
            self.game.right()
        elif e.key() == Qt.Key_D:
            self.game.right_shift()
        elif e.key() == Qt.Key_S:
            self.game.down_shift()
        elif e.key() == Qt.Key_A:
            self.game.left_shift()
        elif e.key() == Qt.Key_W:
            self.game.up_shift()
        elif e.key() == Qt.Key_R:
            self.game.reset_game()
        self.update()

    def mousePressEvent(self, e):
        self.last_point = e.pos()

    def mouseReleaseEvent(self, e):
        self.shuffleRect = QRect(QRect(300, 600, 240, 60))
        if self.shuffleRect.contains(e.pos().x(), e.pos().y()) \
                and self.shuffleRect.contains(self.last_point.x(), self.last_point.y()):
            self.game.reset_game()
            self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        painter.setBrush(QBrush(QColor(0xFFFFFF)))
        painter.drawRect(self.rect())

        painter.setBrush(QBrush(QColor(0x999999)))
        painter.drawRoundedRect(QRect(20, 20, 750, 650), 10, 10)

        painter.setBrush(QBrush(QColor(0xffffff)))
        painter.drawRoundedRect(QRect(200, 295, 408, 5), 3, 3)
        painter.drawRoundedRect(QRect(404, 95, 5, 408), 3, 3)

        self.drawRectangles(painter)

        if self.game.isWin:
            painter.setBrush(QBrush(QColor(80, 80, 80, 150)))
            painter.drawRoundedRect(QRect(20, 20, 750, 650), 10, 10)

            painter.setFont(QFont("Franklin Gothic Medium", 35))
            painter.setPen(QColor(0xffffff))
            painter.drawText(QRectF(QRect(300, 300, 400, 50)), "YOU WIN!!!", QTextOption(Qt.AlignLeft))
            painter.setPen(Qt.NoPen)
        else:
            painter.setBrush(QBrush(QColor(255, 255, 255, 150)))
            painter.drawRoundedRect(
                QRect(195, 85 + (self.game.entry.y ) * 110, 420, 90), 10, 10)
            painter.drawRoundedRect(
                QRect(195 + (self.game.entry.x) * 110, 85, 90, 420), 10, 10)


        painter.setFont(QFont("Franklin Gothic Medium", 40))
        painter.setPen(QColor(0xffffff))
        painter.drawText(QRectF(QRect(300, 600, 240, 60)), "RESTART", QTextOption(Qt.AlignLeft | Qt.AlignVCenter))

    def drawRectangles(self, painter):
        for i in range(self.game.size):
            for j in range(self.game.size):
                painter.setBrush(QColor(0, 0, 0))
                painter.drawRoundedRect(QRect(200 + j * 110, 90 + i * 110, 80, 80), 10, 10)

                painter.setBrush(self.colors[self.game.field[i][j]])
                painter.drawRoundedRect(QRect(202 + j * 110, 92 + i * 110, 76, 76), 10, 10)

                painter.setBrush(Qt.NoBrush)
                painter.setPen(Qt.NoPen)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = PyQtGame()
    sys.exit(app.exec_())
