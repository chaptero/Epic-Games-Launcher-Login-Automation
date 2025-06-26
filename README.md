# Epic Games Login Automation

This project automates the login process for the Epic Games Launcher, allowing users to switch between multiple accounts easily. The program supports up to five accounts and handles the logout and login process, pausing for two-factor authentication if required.

## Project Structure

```
epic-login-automation
├── src
│   ├── main.py          # Entry point of the application
│   ├── accounts.py      # Manages multiple Epic Games accounts
│   ├── epic_launcher.py  # Automates the login process
│   └── utils.py         # Utility functions for the project
├── requirements.txt      # Lists project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd epic-login-automation
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Open a terminal and navigate to the project directory.
2. Run the application:
   ```
   python src/main.py
   ```
3. Follow the prompts to select an account and initiate the login process.

## Notes

- Ensure that the Epic Games Launcher is installed and accessible on your system.
- The program may require additional permissions to control the Epic Games Launcher.
- Two-factor authentication will need to be completed manually if prompted.

## Contributing

Feel free to submit issues or pull requests to improve the functionality of this project.