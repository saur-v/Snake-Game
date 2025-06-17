# 🐍 Classic Snake Game

A modern implementation of the classic Snake arcade game built with Python's Turtle graphics library. Guide your snake to eat food, grow longer, and achieve the highest score possible while avoiding collisions with walls and yourself!

## 🎮 Game Features

- **Classic Gameplay**: Navigate the snake to eat food and grow
- **Score Tracking**: Real-time score display that increases with each food eaten
- **Smooth Controls**: Responsive arrow key controls with collision prevention
- **Progressive Difficulty**: Snake grows longer with each food consumed
- **Collision Detection**: Game ends when hitting walls or the snake's own body
- **Clean Graphics**: Minimalist black background with white snake and pink food
- **Game Over Screen**: Clear indication when the game ends

## 🕹️ How to Play

### Controls
- **↑ Up Arrow**: Move snake up
- **↓ Down Arrow**: Move snake down  
- **← Left Arrow**: Move snake left
- **→ Right Arrow**: Move snake right

### Gameplay Rules
1. **Objective**: Eat the pink food circles to grow your snake and increase your score
2. **Movement**: The snake moves continuously in the direction you choose
3. **Growth**: Each food eaten makes the snake one segment longer
4. **Scoring**: Your score increases by 1 for each food item consumed
5. **Game Over**: The game ends if you hit the walls or collide with your own body
6. **Exit**: Click anywhere on the screen after game over to close

### Tips for High Scores
- Plan your path to avoid trapping yourself
- Use the edges strategically but don't hit the walls
- Think ahead as your snake grows longer
- Stay calm and don't make sudden direction changes

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x
- Turtle graphics library (included with Python)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Run the Game**:
   ```bash
   python main.py
   ```

That's it! No additional dependencies required.

## 📁 Project Structure

```
snake-game/
│
├── main.py           # Main game loop and setup
├── snake.py          # Snake class with movement logic
├── food.py           # Food class with random positioning
├── scoreboard.py     # Score tracking and display
└── README.md         # This file
```

## 🔧 Code Architecture

### Main Components

**main.py** - Game Controller
- Sets up the game screen and coordinates
- Handles the main game loop
- Manages collision detection
- Controls game flow and user input

**snake.py** - Snake Logic
- `Snake` class manages the snake's body segments
- Movement mechanics and direction changes
- Growth functionality when food is eaten
- Prevents illegal moves (e.g., going directly backward)

**food.py** - Food Management  
- `Food` class inherits from Turtle
- Randomly positions food on the screen
- Refreshes to new location when eaten

**scoreboard.py** - Score Display
- `Scoreboard` class handles score tracking
- Updates display in real-time
- Shows game over message

### Key Features Implementation

**Collision System**:
```python
# Food collision (within 15 pixels)
if snake.head.distance(food) < 15:
    food.refresh()
    score.increase_score()
    snake.extend()

# Wall collision detection
if head.xcor() > 280 or head.xcor() < -295 or head.ycor() > 295 or head.ycor() < -295:
    game_over()
```

**Movement Logic**:
- Snake body follows the head in sequence
- Each segment moves to the previous segment's position
- Direction changes are restricted to prevent instant death

## 🎨 Customization

### Visual Modifications

**Colors**:
```python
# In snake.py
snake_color = 'white'  # Change snake color

# In food.py  
food_color = 'pink'    # Change food color

# In main.py
screen.bgcolor('black') # Change background color
```

**Game Speed**:
```python
# In main.py - adjust sleep time
time.sleep(0.1)  # Lower = faster, Higher = slower
```

**Screen Size**:
```python
# In main.py
screen.setup(800, 800)  # Make game area larger
```

### Gameplay Modifications

**Food Size**:
```python
# In food.py
self.shapesize(0.7, 0.7)  # Make food larger
```

**Snake Starting Length**:
```python
# In snake.py
starting_positions = [(0,0), (-20,0), (-40,0), (-60,0)]  # Longer starting snake
```

**Scoring System**:
```python
# In scoreboard.py
def increase_score(self):
    self.score += 10  # 10 points per food instead of 1
```

## 🐛 Troubleshooting

### Common Issues

**Game Runs Too Fast/Slow**:
- Adjust the `time.sleep()` value in the main game loop
- Lower values = faster gameplay, higher values = slower

**Snake Doesn't Respond to Keys**:
- Make sure the game window has focus (click on it)
- Check that you're using arrow keys, not WASD

**Import Errors**:
- Turtle graphics comes with Python by default
- If issues persist, try: `pip install turtle`

**Screen Issues**:
- If the game window doesn't appear properly, try running in a different terminal
- Some IDEs may have issues with Turtle graphics

## 🚧 Potential Enhancements

### Easy Additions
- [ ] **High Score Tracking**: Save and display best scores
- [ ] **Sound Effects**: Add audio feedback for eating food and game over
- [ ] **Different Food Types**: Special foods worth more points
- [ ] **Pause Functionality**: Spacebar to pause/resume game

### Advanced Features
- [ ] **Levels**: Increasing speed or obstacles as score increases
- [ ] **Power-ups**: Special abilities like temporary invincibility
- [ ] **Multiplayer**: Two-player snake game
- [ ] **AI Snake**: Computer-controlled opponent
- [ ] **Custom Maps**: Different layouts and obstacles

### Technical Improvements
- [ ] **Better Graphics**: Replace Turtle shapes with custom images
- [ ] **Settings Menu**: Configurable game options
- [ ] **Game Statistics**: Track games played, average score, etc.
- [ ] **Mobile Version**: Touch controls for mobile devices

## 🤝 Contributing

Contributions are welcome! Here are some ways to help:

1. **Bug Reports**: Find and report issues
2. **Feature Requests**: Suggest new game features
3. **Code Improvements**: Optimize performance or add functionality
4. **Documentation**: Improve instructions or add tutorials
5. **Testing**: Test on different Python versions and systems

### Development Guidelines
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`  
3. Test your changes thoroughly
4. Follow the existing code style
5. Submit a pull request with clear descriptions

## 📚 Learning Resources

- [Python Turtle Documentation](https://docs.python.org/3/library/turtle.html)
- [Game Development with Python](https://realpython.com/pygame-a-primer/)
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)


## 🙏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with Python's Turtle graphics library
- Thanks to the Python community for excellent documentation

---

**Happy Snake Gaming! 🐍🎮**

*Challenge yourself to beat your high score and master the art of snake navigation!*
