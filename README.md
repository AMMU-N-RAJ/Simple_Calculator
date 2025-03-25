# 🧮 Multi-Platform Scientific Calculator Project

## Project Overview 📘
A versatile web-based scientific calculator that brings powerful mathematical capabilities right to your browser. This lightweight JavaScript application supports complex calculations with an intuitive, user-friendly interface.Designed to be both powerful and user-friendly, this web calculator brings professional-grade mathematical computation to your fingertips! 🌟

## Project Variants 🚀
1. **Web-based Calculator**
   - Technologies: HTML, CSS, JavaScript
   - Pure frontend implementation
   - Responsive design

2. **Qt5 Desktop Calculator**
   - Technologies: Python, PyQt5
   - Advanced scientific computing
   - Rich GUI with animations

## Web Calculator Features ✨
- Responsive design
- Scientific functions (sin, cos, tan)
- Keyboard support
- Error handling
- Exponentiation support

## Qt5 Calculator Features 🔬
- Advanced scientific calculations
- Hover animations
- Calculation history
- Advanced mode toggle
- Scientific functions
- Error handling

## Technical Architecture 🏗️
### Web Implementation
- **HTML**: Structured layout
- **CSS**: Modern, responsive styling
- **JavaScript**: Interactive calculations
  - Event-driven programming
  - Mathematical expression parsing
  - Error management

### Desktop Implementation
- **PyQt5 Framework**
  - Object-oriented design
  - Signal-slot mechanism
  - Custom widget styling
- **Scientific Libraries**
  - `math` for core calculations
  - `numpy` for advanced computations

## Prerequisites 🛠️
### Web Version
- Modern web browser
- No additional installations required

### Desktop Version
- Python 3.8+
- Dependencies:
  ```bash
  pip install PyQt5 numpy
  ```

## Installation & Running 🚀

### Web Calculator
1. Clone repository
2. Open `index.html` in browser
```bash
# To run in the browser,commands for the terminal
npm install -g http-server

# Then run the server
http-server
```

### Qt5 Calculator
```bash
# Clone repository
git clone https://github.com/AMMU-N-RAJ/scientific-calculator.git

# Navigate to project
cd scientific-calculator

# Install dependencies
pip install -r requirements.txt

# Run application
python qt-calculator-main.py
```

## Project Structure 📂
```
scientific-calculator/
│
├── web-version/
│   ├── index.html
│   ├── calculator.css
│   └── calculator.js
│
└── desktop-version/
    ├── qt-calculator-main.py
    └── requirements.txt
```

## Development Roadmap 🗺️
- [ ] Add more scientific functions
- [ ] Implement memory storage
- [ ] Create unit conversion
- [ ] Enhance error handling
- [ ] Add graphing capabilities

## Contributing 🤝
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## Learning Outcomes 🎓
- Web development techniques
- Desktop GUI programming
- Event handling
- Mathematical expression parsing
- Error management strategies

## License 📄
MIT License - Open source and free to use!

## Screenshots 📸
### Web Calculator

![demo](https://github.com/AMMU-N-RAJ/Simple_Calculator/blob/main/demo3.gif)

### Qt5 Desktop Calculator

![demo](https://github.com/AMMU-N-RAJ/Simple_Calculator/blob/main/demo4.gif)

## Acknowledgements 🙏
- PyQt5 Documentation
- MDN Web Docs
- Open-source community

---

## Technical Deep Dive 💡

### Calculation Strategy
Our calculators implement a robust calculation strategy:
1. Parse input expression
2. Transform mathematical notations
3. Safely evaluate using `eval()` or equivalent
4. Handle potential errors gracefully

### Design Philosophy
- **Modularity**: Separate concerns
- **Extensibility**: Easy to add new features
- **User Experience**: Intuitive interfaces

Happy Calculating! 🧮✨
