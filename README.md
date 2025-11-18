# DigitalAlarmClock-Python_PBL

⏰ Digital Alarm Clock (Python)
This project is a simple, functional Digital Alarm Clock application built using Python. It provides a user interface to display the current time and allows the user to set a specific time for an alarm.

✨ Key Features
Real-time Clock Display: Shows the current local time in HH:MM:SS format.

Alarm Setting: Allows the user to input a specific time for the alarm (hour, minute, and AM/PM).

Alarm Notification: Plays a sound or displays a message when the current time matches the set alarm time.

Graphical User Interface (GUI): Built with Python's Tkinter library for an intuitive experience.

Category,Component
Language,Python 3.x
GUI Framework,Tkinter (Standard Python library)
Core Modules,"datetime, time"
Optional (for sound),playsound or pygame

🚀 Installation and Setup
Follow these steps to get the project running on your local machine.

Prerequisites
You must have Python 3.x installed.

Steps
Clone the repository:

Bash

git clone https://github.com/yourusername/digital-alarm-clock.git
cd digital-alarm-clock
Install dependencies (if you are using a third-party library for sound): If you used the playsound library, run:

Bash

pip install playsound
Run the application:

Bash

python alarm_clock.py  # or whatever you named your main script
The alarm clock GUI window should open.

💡 How to Use
The main window will continuously display the current time.

Use the input fields (or dropdown menus) to set your desired Hour, Minute, and AM/PM.

Click the "Set Alarm" button.

The alarm will wait in the background. When the current time matches the set time, the alarm sound will play, and/or a notification will appear.

📁 File Structure
alarm_clock.py: The main script containing the GUI logic and the alarm checking function.

alarm.mp3 or alarm.wav: The sound file used for the alarm notification (if applicable).

README.md: Project description (this file).

🤝 Contributing
Feel free to fork this project and submit pull requests. Any contributions are welcome!
