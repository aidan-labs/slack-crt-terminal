<video src="https://github.com/user-attachments/assets/344e5757-9dc8-4c6b-aee3-6c7f3d561a1f" controls></video>
---
# Project Overview

This project is a proof-of-concept for a Slack app integration designed to manage and configure Cisco switches without requiring direct knowledge of the Cisco IOS command line. The app provides an intuitive interface for tasks like sending configurations, executing commands, managing ports, and retrieving device information, all from within Slack. While the current implementation showcases a functional prototype, it is intended as a proof-of-concept rather than a production-ready solution. Key areas for improvement include:

1. **Security Enhancements**:
   - Implement Multi-Factor Authentication for accessing switches, potentially integrated with the Cisco Identity Services Engine.

2. **Code Refactoring**:
   - Improve code organization and formatting for better readability and maintainability.
    - Enhance the user interface with more granular configuration options.
---
# Installation and Running

1. **Install Dependencies and Setup**:
   - Clone this repository somewhere on your system:
   - Create a virtual environment in the root directory (`slack-crt-terminal/`) to isolate dependencies:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```
   - Install the required dependencies using:
     ```bash
     pip3 install -r requirements.txt
     ```
   - Run the script with the following command:
     ```bash
     python3 main.py
     ```
   - Install [ngrok](https://ngrok.com/download) and run the following command to start a forwarding URL:  
     ```bash
     ngrok http 9999
     ```
   - Create a Slack App:
     - Visit the [Slack API portal](https://api.slack.com/apps) and click "Create New App".
     - In "Oath & Permissions" add the following scopes to the "Bot Token Scopes":
       - `commands`
       - `chat:write`
     - Install the app to the Slack workspace, then copy the OAuth token provided.  
       Save it in a `.env` file at the root of the project:
       ```bash
       OATH_TOKEN=oauth-token-here
       ```
   - Enable Interactivity:
     - Go to the "Interactivity & Shortcuts" section of the Slack app settings.
     - Enable Interactivity and paste the forwarding URL followed by `/interactive` as the Request URL.  

   - Add Event Subscriptions:
     - In the "Event Subscriptions" section, enable events and paste the forwarding URL followed by `/events` as the Request URL.  
     - Under "Subscrive to bot events" add `app_home_opened`

   - Enable the Home Tab:
     - Navigate to the "App Home" section of the Slack app settings and eable the Home Tab by toggling the option on.
---
# Execution Flow

1. `main.py` - The Main Controller
   - Handles incoming Slack requests and routes them to the appropriate response function.

2. `views.py` - Dynamic Views and Modals
   - Generates Slack modals and dynamically updates options based on previous selections.
     - Location and Closet Selection: Dynamically updates closet options based on the selected location.
     - Action Selection: Provides options like sending configurations, executing commands, bouncing ports, or finding MAC/IP addresses.
     - Command Previews: Displays a preview of commands before execution.

3. `netmiko_utils.py` - SSH Functions
   - Processes configurations and templates.
   - Communicates with the Cisco IOS CLI with the selected switches and retrieves output.