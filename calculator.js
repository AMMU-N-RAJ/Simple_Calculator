document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');

    // Enhanced calculation function with comprehensive error handling
    function calculate() {
        try {
            // Comprehensive mathematical expression processing
            let expression = display.value
                // Handle power/exponentiation
                .replace(/\^/g, '**')
                
                // Trigonometric functions with radian conversion
                .replace(/sin\(/g, 'Math.sin(Math.PI/180 * ')
                .replace(/cos\(/g, 'Math.cos(Math.PI/180 * ')
                .replace(/tan\(/g, 'Math.tan(Math.PI/180 * ')
                
                // Ensure closure of trigonometric function parentheses
                .replace(/Math\.(sin|cos|tan)\(Math\.PI\/180 \* ([^)]+)\)/g, 'Math.$1(Math.PI/180 * $2)');

            // Security: Remove any potentially malicious characters
            expression = expression.replace(/[^0-9+\-*\/().,\s]/g, '');

            // Safe evaluation using Function constructor
            const result = new Function(`return (${expression})`)();
            
            // Round result to prevent floating-point precision issues
            display.value = Number(result.toFixed(10));
        } catch (error) {
            display.value = 'Error';
            console.error('Calculation Error:', error);
        }
    }

    // Universal display append function
    function appendToDisplay(value) {
        // Special handling for scientific functions
        if (['sin', 'cos', 'tan'].includes(value)) {
            display.value += `${value}()`;
            
            // Position cursor between parentheses
            const lastIndex = display.value.length - 1;
            display.setSelectionRange(lastIndex, lastIndex);
        } else {
            display.value += value;
        }
    }

    // Attach functions to window for HTML onclick compatibility
    window.appendToDisplay = appendToDisplay;
    window.calculate = calculate;
    window.clearDisplay = () => display.value = '';
    window.deleteLastChar = () => display.value = display.value.slice(0, -1);

    // Keyboard support
    display.addEventListener('keydown', (event) => {
        const allowedKeys = /^[0-9+\-*/().^]$/;
        
        if (allowedKeys.test(event.key)) {
            event.preventDefault();
            appendToDisplay(event.key);
        } else if (event.key === 'Enter') {
            calculate();
        } else if (event.key === 'Backspace') {
            deleteLastChar();
        } else if (event.key === 'Escape') {
            clearDisplay();
        }
    });
});
