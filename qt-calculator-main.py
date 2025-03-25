import sys
import math
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QGridLayout, QPushButton, QLineEdit, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.parenthesis_count = 0
        
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
        return button
    
    def button_click(self, value):
        current_text = self.display.text()
        
        try:
            if value == 'C':
                self.display.clear()
                self.parenthesis_count = 0
            elif value == '⌫':
                if current_text:
                    # Track parenthesis count when deleting
                    if current_text[-1] == '(':
                        self.parenthesis_count -= 1
                    elif current_text[-1] == ')':
                        self.parenthesis_count += 1
                    self.display.setText(current_text[:-1])
            elif value == '(':
                # Only allow opening parenthesis if it makes sense
                if not current_text or current_text[-1] in '(+-*/^':
                    self.display.setText(current_text + value)
                    self.parenthesis_count += 1
            elif value == ')':
                # Only close parenthesis if there are unclosed parentheses
                if self.parenthesis_count > 0 and current_text and current_text[-1] not in '(+-*/^':
                    self.display.setText(current_text + value)
                    self.parenthesis_count -= 1
            elif value == '=':
                result = self.calculate()
                self.history_label.setText(f'Last Calculation: {current_text} = {result}')
                self.display.setText(str(result))
                self.parenthesis_count = 0
            elif value == '√':
                self.display.setText(f'sqrt({current_text})')
            elif value == 'π':
                self.display.setText(current_text + 'pi')
            elif value == 'e':
                self.display.setText(current_text + 'e')
            elif value in ['sin', 'cos', 'tan', 'log']:
                self.display.setText(f'{value}({current_text})')
            else:
                # Prevent consecutive operators
                if value in ['+', '-', '*', '/', '^'] and current_text and current_text[-1] in ['+', '-', '*', '/', '^']:
                    self.display.setText(current_text[:-1] + value)
                else:
                    self.display.setText(current_text + value)
        except Exception as e:
            self.display.setText('Error')
    
    def calculate(self):
        try:
            # Comprehensive expression parsing
            expression = self.display.text()
            
            # Replace mathematical constants
            expression = expression.replace('pi', str(math.pi))
            expression = expression.replace('e', str(math.e))
            
            # Replace trigonometric and logarithmic functions
            expression = re.sub(r'sin\(', 'math.sin(', expression)
            expression = re.sub(r'cos\(', 'math.cos(', expression)
            expression = re.sub(r'tan\(', 'math.tan(', expression)
            expression = re.sub(r'log\(', 'math.log10(', expression)
            expression = re.sub(r'sqrt\(', 'math.sqrt(', expression)
            
            # Replace power operator
            expression = expression.replace('^', '**')
            
            # Validate parentheses
            if expression.count('(') != expression.count(')'):
                return 'Invalid Parentheses'
            
            # Safe evaluation
            result = eval(expression)
            return round(result, 10)
        except Exception as e:
            return 'Error'
    
    def toggle_advanced_mode(self):
        self.advanced_mode = not self.advanced_mode
        self.advanced_toggle.setText('Advanced Mode: ' + 
                                     ('ON' if self.advanced_mode else 'OFF'))
    
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
