# views.py

# Function to generate view on the home screen
def generate_home_view():
    return {
        "type": "home",
        "blocks": [
            {"type": "header", "text": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True}},
            {"type": "actions", "elements": [{"type": "button", "text": {"type": "plain_text", "text": "Configuration menu", "emoji": True}, "value": "open_modal_button", "action_id": "open_modal"}]},
        ]
    }

# Function to generate the main menu
def generate_main_menu(user_name):
    return {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
        "close": {"type": "plain_text", "text": "Exit", "emoji": True},
        "blocks": [
            {"type": "section", "text": {"type": "plain_text", "text": f"Hello <@{user_name}>!", "emoji": True}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "Select a location! 📍"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": [{"text": {"type": "plain_text", "text": "Location 1 🌍", "emoji": True}, "value": "location_1"}, {"text": {"type": "plain_text", "text": "Location 2 🌍", "emoji": True}, "value": "location_2"}, {"text": {"type": "plain_text", "text": "Location 3 🌍", "emoji": True}, "value": "location_3"}, {"text": {"type": "plain_text", "text": "Location 4 🌍", "emoji": True}, "value": "location_4"}], "action_id": "location_dropdown"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": "What are you doing❓"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": [{"text": {"type": "plain_text", "text": "Sending commands ⌨️", "emoji": True}, "value": "sending_commands"}, {"text": {"type": "plain_text", "text": "Sending configurations 🧪", "emoji": True}, "value": "sending_configurations"}, {"text": {"type": "plain_text", "text": "Bouncing a port ⛹️‍♂️", "emoji": True}, "value": "bounce_port"}, {"text": {"type": "plain_text", "text": "MAC & IP from port 🕵️‍♂️", "emoji": True}, "value": "find_info"}], "action_id": "template_action"}},
            {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Submit"}, "action_id": "submit_buton", "style": "primary"}}
        ]
    }

# Function to dynamically update the switch selections based off the premise selection
def get_updated_options(selected_option):
    if selected_option == "location_1":
        return [
            { "text": { "type": "plain_text", "text": "💻 Test Closet" }, "value": "test_closet"},
            { "text": { "type": "plain_text", "text": "💻 Closet 1" }, "value": "closet_01" },
            { "text": { "type": "plain_text", "text": "💻 Closet 2" }, "value": "closet_02" },
        ]
    elif selected_option == "location_2":
        return [
            { "text": { "type": "plain_text", "text": "💻 Closet 11" }, "value": "closet_11" },
            { "text": { "type": "plain_text", "text": "💻 Closet 12" }, "value": "closet_12" },
            ]
    elif selected_option == "location_3":
        return [
            { "text": { "type": "plain_text", "text": "💻 Closet 13" }, "value": "closet_13" },
            { "text": { "type": "plain_text", "text": "💻 Closet 14" }, "value": "closet_14" },
        ]
    elif selected_option == "location_4":
        return [
            { "text": { "type": "plain_text", "text": "💻 Closet 17" }, "value": "closet_17" },
            { "text": { "type": "plain_text", "text": "💻 Closet 18" }, "value": "closet_18" },
            ]
    else:
        return []

# Function to generate the view based off chosen action
def generate_second_view(template_action, premises, selected_option):
    if template_action == "sending_commands":
        updated_options = get_updated_options(selected_option)
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "submit": {"type": "plain_text", "text": "Run", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"Select a closet in {premises}!"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": updated_options, "action_id": "closet_dropdown"}},
                {"type": "input", "element": {"type": "plain_text_input", "action_id": "command_input", "placeholder": {"type": "plain_text", "text": "Type a command...", "emoji": True}}, "label": {"type": "plain_text", "text": "Command", "emoji": True}}
            ]
        }
    elif template_action == "sending_configurations":
        updated_options = get_updated_options(selected_option)
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "submit": {"type": "plain_text", "text": "Preview", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"Select a closet in {premises}!"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": updated_options, "action_id": "closet_dropdown"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": "Select a template!"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": [{"text": {"type": "plain_text", "text": "🔄 Default", "emoji": True}, "value": "vlan_2_template"}, {"text": {"type": "plain_text", "text": "📺 DMP", "emoji": True}, "value": "vlan_4_template"}, {"text": {"type": "plain_text", "text": "🌍 Public", "emoji": True}, "value": "vlan_6_template"}, {"text": {"type": "plain_text", "text": "🎥 Video", "emoji": True}, "value": "vlan_8_template"}, {"text": {"type": "plain_text", "text": "🔒 Security Camera", "emoji": True}, "value": "vlan_10_template"}], "action_id": "template_action"}},
                {"type": "input", "element": {"type": "plain_text_input", "action_id": "command_input", "placeholder": {"type": "plain_text", "text": "Type a port ID...", "emoji": True}}, "label": {"type": "plain_text", "text": "Port ID (e.g., g1/0/0)", "emoji": True}},
                {"type": "input", "element": {"type": "plain_text_input", "action_id": "description_input", "placeholder": {"type": "plain_text", "text": "Type a description...", "emoji": True}}, "label": {"type": "plain_text", "text": "Description", "emoji": True}},
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Commit"}, "action_id": "send_config_button", "style": "primary"}}
            ]
        }
    elif template_action == "bounce_port":
        updated_options = get_updated_options(selected_option)
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "submit": {"type": "plain_text", "text": "Run", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"Select a closet in {premises}!"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": updated_options, "action_id": "closet_dropdown"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": "Power Control"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": [{"text": {"type": "plain_text", "text": "Power OFF🪫", "emoji": True}, "value": "power_off"}, {"text": {"type": "plain_text", "text": "Power ON 🔋", "emoji": True}, "value": "power_on"}], "action_id": "template_action"}},
                {"type": "input", "element": {"type": "plain_text_input", "action_id": "command_input", "placeholder": {"type": "plain_text", "text": "Type a port ID...", "emoji": True}}, "label": {"type": "plain_text", "text": "Port ID (e.g., g1/0/0)", "emoji": True}}
            ]
        }
    elif template_action == "find_info":
        updated_options = get_updated_options(selected_option)
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "submit": {"type": "plain_text", "text": "Run", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"Select a closet in {premises}!"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": updated_options, "action_id": "closet_dropdown"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": "Device Identification"}, "accessory": {"type": "static_select", "placeholder": {"type": "plain_text", "text": "Select...", "emoji": True}, "options": [{"text": {"type": "plain_text", "text": "MAC Address🔢", "emoji": True}, "value": "find_mac"}, {"text": {"type": "plain_text", "text": "IP Address 📶", "emoji": True}, "value": "find_ip"}], "action_id": "template_action"}},
                {"type": "input", "element": {"type": "plain_text_input", "action_id": "command_input", "placeholder": {"type": "plain_text", "text": "Type a port ID...", "emoji": True}}, "label": {"type": "plain_text", "text": "Port ID (e.g., g1/0/0)", "emoji": True}}
            ]
        }
    else:
        return None

# Function to display the output of certain actions
def generate_output_modal(command_input, output):
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "close": {"type": "plain_text", "text": "Exit", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "rich_text", "elements": [{"type": "rich_text_section", "elements": [{"type": "text", "text": "Output"}]}, {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"Port ID: {command_input}, Output {output}"}]}]}
            ]
        }

# Genrate the preview message based of of configuration selection
def preview_message(template_action, command_input, description_input):
    if template_action == "vlan_2_templace":
        config_preview = f"interface {command_input}\n description {description_input}\n switchport access vlan 2\nno shutdown\nend"
    elif template_action == "vlan_4_templace":
        config_preview = f"interface {command_input}\n description {description_input}\n switchport access vlan 4\nno shutdown\nend"
    elif template_action == "vlan_6_templace":
        config_preview = f"interface {command_input}\n description {description_input}\n switchport access vlan 6\nno shutdown\nend"
    elif template_action == "vlan_8_templace":
        config_preview = f"interface {command_input}\n description {description_input}\n switchport access vlan 8\nno shutdown\nend"
    elif template_action == "vlan_10_templace":
        config_preview = f"interface {command_input}\n description {description_input}\n switchport access vlan 10\nno shutdown\nend"
    else:
        config_preview = "Invalid template action"
        
    return config_preview

# Display the modal with the current configuration and new configuration as preview       
def generate_preview_modal(template_action, command_input, description_input, output):
    # Generate the configuration preview using preview_message
    config_preview = preview_message(template_action, command_input, description_input)
    
    return {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
        "close": {"type": "plain_text", "text": "Back", "emoji": True},
        "blocks": [
            {"type": "rich_text", "elements": [{"type": "rich_text_section", "elements": [{"type": "text", "text": "Current Configuration"}]}, {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"{output}"}]}]},
            {"type": "rich_text", "elements": [{"type": "rich_text_section", "elements": [{"type": "text", "text": "New Configuration"}]}, {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"{config_preview}"}]}]}
        ]
    }

# Displau modal for a shut and no shut command being sent
def generate_shut_noshut_modal(template_action, command_input, output):
    if template_action == "power_off":
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "close": {"type": "plain_text", "text": "Back", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "rich_text", "elements": [
                    {"type": "rich_text_section", "elements": [
                        {"type": "text", "text": f"Port ID: {command_input} is"},
                        {"type": "text", "text": " SHUT DOWN❗", "style": {"bold": True}}
                    ]},
                    {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"{output}"}]}
                ]}
            ]
        }
    if template_action == "power_on":
        return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "close": {"type": "plain_text", "text": "Back", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "rich_text", "elements": [
                    {"type": "rich_text_section", "elements": [
                        {"type": "text", "text": f"Port ID: {command_input} is"},
                        {"type": "text", "text": " UP AND RUNNING❗", "style": {"bold": True}}
                    ]},
                    {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"{output}"}]}
                ]}
            ]
        }
        
def display_modal_ip_mac(command, output):
    return {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
        "close": {"type": "plain_text", "text": "Back", "emoji": True},
        "blocks": [
            {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
            {"type": "rich_text", "elements": [
                {"type": "rich_text_section", "elements": [{"type": "text", "text": "Output"}]},
                {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"Command: {command}, Output {output}"}]}
            ]}
        ]
    }
               
# Display modal for when sending singular commands
def sending_any_command_modal(command_input, output):
    return {
            "type": "modal",
            "title": {"type": "plain_text", "text": "Slack CRT Terminal", "emoji": True},
            "close": {"type": "plain_text", "text": "Back", "emoji": True},
            "blocks": [
                {"type": "section", "text": {"type": "plain_text", "text": " "}, "accessory": {"type": "button", "text": {"type": "plain_text", "text": "Main menu"}, "action_id": "main_menu_button", "style": "danger"}},
                {"type": "rich_text", "elements": [
                    {"type": "rich_text_section", "elements": [{"type": "text", "text": "Output"}]},
                    {"type": "rich_text_preformatted", "elements": [{"type": "text", "text": f"Command: {command_input}, Output {output}"}]}
                ]}
            ]
        }
