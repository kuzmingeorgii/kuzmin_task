import sys
import random
from PyQt6.QtWidgets import QPushButton, QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.add_circle)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Случайные окружности")

        self.pushButton = QPushButton("Нажми меня", self)
        self.pushButton.setGeometry(10, 10, 113, 32)
        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)

        x = random.randint(0, self.width() - diameter)
        y = random.randint(50, self.height() - diameter)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circles.append((x, y, diameter, color))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(QColor(0, 0, 0))
            painter.drawEllipse(QRect(x, y, diameter, diameter))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
