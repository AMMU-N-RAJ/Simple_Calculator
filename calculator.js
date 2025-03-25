// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
    // Select all buttons
    const buttons = document.querySelectorAll('button');
    const display = document.getElementById('display');

    // Add click event listeners to all buttons
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.textContent;
            
            switch(value) {
                case 'C':
                    clearDisplay();
                    break;
                case '⌫':
                    deleteLastChar();
                    break;
                case '=':
                    calculate();
                    break;
                case 'sin':
                    appendToDisplay('sin(');
                    break;
                case 'cos':
                    appendToDisplay('cos(');
                    break;
                case 'tan':
                    appendToDisplay('tan(');
                    break;
                default:
                    if (button.classList.contains('number') || 
                        button.classList.contains('operator') || 
                        value === '.' || 
                        value === '(' || 
                        value === ')' ||
                        value === '^') {
                        appendToDisplay(value);
                    }
            }
        });
    });

    // Function to append characters to display
    function appendToDisplay(value) {
        display.value += value;
    }

    // Function to clear the display
    function clearDisplay() {
        display.value = '';
    }

    // Function to delete last character
    function deleteLastChar() {
        display.value = display.value.slice(0, -1);
    }

    // Function to calculate result
    function calculate() {
        try {
            // Replace ^ with Math.pow for exponentiation
            let expression = display.value.replace(/\^/g, '**');
            
            // Replace trigonometric functions
            expression = expression.replace(/sin\(/g, 'Math.sin(');
            expression = expression.replace(/cos\(/g, 'Math.cos(');
            expression = expression.replace(/tan\(/g, 'Math.tan(');
            
            // Convert to radians for trigonometric functions
            expression = expression.replace(/Math\.(sin|cos|tan)\(/g, 'Math.$1(Math.PI/180 * ');
            
            // Evaluate the expression
            const result = eval(expression);
            
            // Display the result
            display.value = Number(result.toFixed(10));
        } catch (error) {
            display.value = 'Error';
        }
    }

    // Keyboard support
    document.addEventListener('keydown', (event) => {
        const key = event.key;
        
        // Numeric and basic operator keys
        const validKeys = '0123456789.+-*/()';
        
        if (validKeys.includes(key)) {
            appendToDisplay(key);
        } else if (key === 'Enter') {
            calculate();
        } else if (key === 'Backspace') {
            deleteLastChar();
        } else if (key === 'Escape') {
            clearDisplay();
        }
    });
});