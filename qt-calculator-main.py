import sys
import math
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QGridLayout, QPushButton, QLineEdit, QLabel)
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QPainter
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Main window setup
        self.setWindowTitle('Advanced Scientific Calculator')
        self.setGeometry(100, 100, 500, 700)
        self.setStyleSheet(self.get_stylesheet())
        
        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Display area
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont('Arial', 24))
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #2c3e50;
                color: white;
                border: 2px solid #34495e;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        main_layout.addWidget(self.display)
        
        # Buttons layout
        buttons_layout = QGridLayout()
        main_layout.addLayout(buttons_layout)
        
        # Button configurations
        buttons = [
            ('C', 0, 0), ('⌫', 0, 1), ('(', 0, 2), (')', 0, 3),
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('^', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('log', 6, 0), ('√', 6, 1), ('π', 6, 2), ('e', 6, 3)
        ]
        
        # Create and add buttons
        for (text, row, col) in buttons:
            button = self.create_button(text)
            buttons_layout.addWidget(button, row, col)
        
        # Add advanced mode toggle
        self.advanced_mode = False
        self.advanced_toggle = QPushButton('Advanced Mode')
        self.advanced_toggle.clicked.connect(self.toggle_advanced_mode)
        main_layout.addWidget(self.advanced_toggle)
        
        # History display
        self.history_label = QLabel('Calculation History')
        self.history_label.setStyleSheet("""
            background-color: #34495e;
            color: white;
            padding: 5px;
            border-radius: 5px;
        """)
        main_layout.addWidget(self.history_label)
        
    def create_button(self, text):
        button = QPushButton(text)
        button.setFont(QFont('Arial', 16))
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        button.clicked.connect(lambda: self.button_click(text))
        
        # Add hover animation
        button.enterEvent = lambda event: self.button_hover_animation(button)
        
        return button
    
    def button_hover_animation(self, button):
        # Create a subtle scale animation
        anim = QPropertyAnimation(button, b"geometry")
        anim.setDuration(100)
        anim.setStartValue(button.geometry())
        anim.setEndValue(QRect(
            button.x() - 5, 
            button.y() - 5, 
            button.width() + 10, 
            button.height() + 10
        ))
        anim.setEasingCurve(QEasingCurve.OutBounce)
        anim.start()
    
    def button_click(self, value):
        try:
            if value == 'C':
                self.display.clear()
            elif value == '⌫':
                self.display.setText(self.display.text()[:-1])
            elif value == '=':
                result = self.calculate()
                self.history_label.setText(f'Last Calculation: {self.display.text()} = {result}')
                self.display.setText(str(result))
            elif value == '√':
                self.display.setText(str(math.sqrt(float(self.display.text() or 0))))
            elif value == 'π':
                self.display.setText(str(math.pi))
            elif value == 'e':
                self.display.setText(str(math.e))
            elif value in ['sin', 'cos', 'tan', 'log']:
                func = getattr(math, value)
                self.display.setText(str(func(float(self.display.text() or 0))))
            else:
                self.display.setText(self.display.text() + value)
        except Exception as e:
            self.display.setText('Error')
    
    def calculate(self):
        try:
            # Replace ^ with power operator
            expression = self.display.text().replace('^', '**')
            return eval(expression)
        except Exception as e:
            return 'Error'
    
    def toggle_advanced_mode(self):
        self.advanced_mode = not self.advanced_mode
        self.advanced_toggle.setText('Advanced Mode: ' + 
                                     ('ON' if self.advanced_mode else 'OFF'))
        # Future: Add more advanced features when mode is toggled
    
    def get_stylesheet(self):
        return """
        QMainWindow {
            background-color: #2c3e50;
        }
        """

def main():
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
