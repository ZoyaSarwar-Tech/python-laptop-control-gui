# Python Laptop Control GUI

A simple desktop application built with **Python** and **Tkinter** that allows users to perform basic Windows system operations through a graphical interface.

## Features

- Shutdown the computer
- Restart the computer
- Cancel a scheduled shutdown
- Simple and beginner-friendly GUI
- Lightweight and easy to use

## Technologies Used

- Python 3
- Tkinter
- OS Module

## Project Structure

```
python-laptop-control-gui/
│── main.py
│── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/python-laptop-control-gui.git
```

2. Navigate to the project folder

```bash
cd python-laptop-control-gui
```

3. Run the application

```bash
python main.py
```

## How It Works

The application uses Python's built-in `os` module to execute Windows shutdown commands.

- **Shutdown:** `shutdown /s /t 0`
- **Restart:** `shutdown /r /t 0`
- **Cancel Shutdown:** `shutdown /a`

## Requirements

- Python 3.x
- Windows Operating System

No external libraries are required.

## Warning

This project executes real Windows shutdown and restart commands. Running the Shutdown or Restart button will immediately affect your computer. Test with caution.

## Learning Objectives

This project demonstrates:

- Tkinter GUI development
- Button event handling
- Python functions
- Using the `os` module
- Executing system commands from Python

## License

This project is licensed under the MIT License.
