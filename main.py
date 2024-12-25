# main.py

# Standard imports
import json
import os
import re
import ssl
# Third-Party imports
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
# Local imports
from netmiko_utils import *
from slack_views import *

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()
oauth_token = os.getenv("OATH_TOKEN")
app = Flask(__name__)
client = WebClient(token=oauth_token)
user_name = None

@app.route("/events", methods=["POST"])
def slack_events():
    event_data = request.json
    if "challenge" in event_data:
        return jsonify({"challenge": event_data["challenge"]})
    elif "event" in event_data and event_data["event"]["type"] == "app_home_opened":
        event = event_data["event"]
        user_id = event["user"]
        home_view = generate_home_view()
        if home_view:
            try:
                client.views_publish(user_id=user_id, view=home_view)
            except SlackApiError as e:
                print(f"Error: {e.response['error']}")
    return jsonify({"status": "success"})

def main_menu(payload=None):
    global user_name
    if payload:
        trigger_id = payload["trigger_id"]
        user_name = payload["user"]["username"]
    else:
        trigger_id = request.form["trigger_id"]
    
    main_menu_modal = generate_main_menu(user_name)
    try:
        client.views_open(trigger_id=trigger_id, view=main_menu_modal)
        return ""
    except SlackApiError as e:
        error_message = f"Error opening modal: {e.response['error']}"
        return jsonify({"error": error_message}), 500

@app.route("/interactive", methods=["POST", "GET"])
def interactive():
    global user_name
    payload = json.loads(request.form.get("payload", "{}"))
    if "trigger_id" in payload:
        trigger_id = payload["trigger_id"]
    if "user" in payload and "username" in payload["user"]:
        user_name = payload["user"]["username"]
    else:
        user_name = "Guest"
    if payload.get("type") == "block_actions":
        for action in payload.get("actions", []):
            if action.get("action_id") == "open_modal":
                return main_menu(payload)
            elif action["action_id"] == "submit_buton":
                state_values = payload["view"]["state"]["values"]
                selected_option = None
                template_action = None

                for block_id, block_data in state_values.items():
                    if "location_dropdown" in block_data:
                        selected_option = block_data["location_dropdown"]["selected_option"]["value"]
                        premises = block_data["location_dropdown"]["selected_option"]["text"]["text"]
                        updated_options = get_updated_options(selected_option)
                for block_id, block_data in payload["view"]["state"]["values"].items():
                    if "template_action" in block_data:
                        template_action = block_data["template_action"]["selected_option"]["value"]

                # Ensure template_action is assigned before generating the second view
                if template_action is None:
                    return jsonify({"error": "Template action is missing or invalid"}), 400
                
                updated_view = generate_second_view(template_action, premises, selected_option)
                
                if updated_view:
                    try:
                        client.views_update(
                            view_id=payload["view"]["id"],
                            hash=payload["view"]["hash"],
                            view=updated_view
                        )
                        return ""
                    except SlackApiError as e:
                        error_message = f"Error updating view: {e.response['error']}"
                        return jsonify({"error": error_message}), 500
                else:
                    return jsonify({"error": "Invalid template action"}), 500
                        
            elif action["action_id"] == "send_config_button":
                if action["action_id"] == "send_config_button":
                    state_values = payload["view"]["state"]["values"]
                    selected_option = None
                    command_input = None
                    template_action = None
                    description_input = None

                for block_id, block_data in state_values.items():
                    if "closet_dropdown" in block_data:
                        selected_option = block_data["closet_dropdown"]["selected_option"]["value"]
                    elif "command_input" in block_data:
                        command_input = block_data["command_input"]["value"]
                    elif "description_input" in block_data:
                        description_input = block_data["description_input"]["value"]
                    elif "template_action" in block_data:
                        template_action_data = block_data.get("template_action")
                        if template_action_data and "selected_option" in template_action_data:
                            template_action = template_action_data["selected_option"]["value"]

                if template_action == "vlan_2_templace":
                    switch_config = all_switch_configs[selected_option]
                    config_commands = [
                        f'interface {command_input}',
                        f'description {description_input}',
                        'switchport access vlan 2',
                        'no shutdown',
                        'exit',
                    ]
                    output = send_set_config(switch_config, config_commands)
                    output_view = generate_output_modal(command_input, output)
                    
                    if output_view:
                        try:
                            client.views_update(
                                view_id=payload["view"]["id"],
                                hash=payload["view"]["hash"],
                                view=output_view
                            )
                            return ""
                        except SlackApiError as e:
                            error_message = f"Error updating view: {e.response['error']}"
                            return jsonify({"error": error_message}), 500
                    else:
                        return jsonify({"error": "Invalid template action"}), 500

                elif template_action == "vlan_4_templace":
                    switch_config = all_switch_configs[selected_option]
                    config_commands = [
                        f'interface {command_input}',
                        f'description {description_input}',
                        'switchport access vlan 4',
                        'no shutdown',
                        'exit',
                    ]
                    output = send_set_config(switch_config, config_commands)
                    output_view = generate_output_modal(command_input, output)

                    if output_view:
                        try:
                            client.views_update(
                                view_id=payload["view"]["id"],
                                hash=payload["view"]["hash"],
                                view=output_view
                            )
                            return ""
                        except SlackApiError as e:
                            error_message = f"Error updating view: {e.response['error']}"
                            return jsonify({"error": error_message}), 500
                    else:
                        return jsonify({"error": "Invalid template action"}), 500
                
                elif template_action == "vlan_6_templace":
                    switch_config = all_switch_configs[selected_option]
                    config_commands = [
                        f'interface {command_input}',
                        f'description {description_input}',
                        'switchport access vlan 6',
                        'no shutdown',
                        'exit',
                    ]
                    output = send_set_config(switch_config, config_commands)
                    output_view = generate_output_modal(command_input, output)

                    if output_view:
                        try:
                            client.views_update(
                                view_id=payload["view"]["id"],
                                hash=payload["view"]["hash"],
                                view=output_view
                            )
                            return ""
                        except SlackApiError as e:
                            error_message = f"Error updating view: {e.response['error']}"
                            return jsonify({"error": error_message}), 500
                    else:
                        return jsonify({"error": "Invalid template action"}), 500
                
                elif template_action == "vlan_8_templace":
                    switch_config = all_switch_configs[selected_option]
                    config_commands = [
                        f'interface {command_input}',
                        f'description {description_input}',
                        'switchport access vlan 8',
                        'no shutdown',
                        'exit',
                    ]
                    output = send_set_config(switch_config, config_commands)
                    output_view = generate_output_modal(command_input, output)

                    if output_view:
                        try:
                            client.views_update(
                                view_id=payload["view"]["id"],
                                hash=payload["view"]["hash"],
                                view=output_view
                            )
                            return ""
                        except SlackApiError as e:
                            error_message = f"Error updating view: {e.response['error']}"
                            return jsonify({"error": error_message}), 500
                    else:
                        return jsonify({"error": "Invalid template action"}), 500
                
                elif template_action == "vlan_10_templace":
                    switch_config = all_switch_configs[selected_option]
                    config_commands = [
                        f'interface {command_input}',
                        f'description {description_input}',
                        'switchport access vlan 10',
                        'no shutdown',
                        'exit',
                    ]
                    output = send_set_config(switch_config, config_commands)
                    output_view = generate_output_modal(command_input, output)

                    if output_view:
                        try:
                            client.views_update(
                                view_id=payload["view"]["id"],
                                hash=payload["view"]["hash"],
                                view=output_view
                            )
                            return ""
                        except SlackApiError as e:
                            error_message = f"Error updating view: {e.response['error']}"
                            return jsonify({"error": error_message}), 500
                    else:
                        return jsonify({"error": "Invalid template action"}), 500
                
            elif action["action_id"] == "main_menu_button":
                main_menu_modal = generate_main_menu(user_name)
                if main_menu_modal:
                    try:
                        client.views_update(
                            view_id=payload["view"]["id"],
                            hash=payload["view"]["hash"],
                            view=main_menu_modal
                        )
                        return ""
                    except SlackApiError as e:
                        error_message = f"Error updating view: {e.response['error']}"
                        return jsonify({"error": error_message}), 500
                else:
                    return jsonify({"error": "Invalid template action"}), 500
        else:
            return ""
    
    elif payload["type"] == "view_submission":
        state_values = payload["view"]["state"]["values"]
        selected_option = None
        command_input = None
        template_action = None

        for block_id, block_data in state_values.items():
            if "closet_dropdown" in block_data:
                selected_option = block_data["closet_dropdown"]["selected_option"]["value"]
            elif "command_input" in block_data:
                command_input = block_data["command_input"]["value"]
            elif "description_input" in block_data:
                description_input = block_data["description_input"]["value"]
            elif "template_action" in block_data:
                template_action_data = block_data.get("template_action")
                if template_action_data and "selected_option" in template_action_data:
                    template_action = template_action_data["selected_option"]["value"]

        if template_action == "vlan_2_templace":
            switch_config = all_switch_configs[selected_option]
            command = f"sh run int {command_input}"
            output = send_command(switch_config, command)
            preview_config = generate_preview_modal(template_action, command_input, description_input, output)
            return jsonify({"response_action": "push", "view": preview_config})
        
        elif template_action == "vlan_4_templace":
            switch_config = all_switch_configs[selected_option]
            command = f"sh run int {command_input}"
            output = send_command(switch_config, command)
            preview_config = generate_preview_modal(template_action, command_input, description_input, output)
            return jsonify({"response_action": "push", "view": preview_config})

        elif template_action == "vlan_6_templace":
            switch_config = all_switch_configs[selected_option]
            command = f"sh run int {command_input}"
            output = send_command(switch_config, command)
            preview_config = generate_preview_modal(template_action, command_input, description_input, output)
            return jsonify({"response_action": "push", "view": preview_config})
        
        elif template_action == "vlan_8_templace":
            switch_config = all_switch_configs[selected_option]
            command = f"sh run int {command_input}"
            output = send_command(switch_config, command)
            preview_config = generate_preview_modal(template_action, command_input, description_input, output)
            return jsonify({"response_action": "push", "view": preview_config})
        
        elif template_action == "vlan_10_templace":
            switch_config = all_switch_configs[selected_option]
            command = f"sh run int {command_input}"
            output = send_command(switch_config, command)
            preview_config = generate_preview_modal(template_action, command_input, description_input, output)
            return jsonify({"response_action": "push", "view": preview_config})
        
        elif template_action == "power_off":
            switch_config = all_switch_configs[selected_option]
            config_commands = [
                f'interface {command_input}',
                'shut',
                'exit',
            ]
            send_set_config(switch_config, config_commands)
            output = show_int(switch_config, command_input)
            output_view = generate_shut_noshut_modal(template_action, command_input, output)

            return jsonify({"response_action": "push", "view": output_view})

        elif template_action == "power_on":
            switch_config = all_switch_configs[selected_option]
            config_commands = [
                f'interface {command_input}',
                'no shut',
                'exit',
            ]
            send_set_config(switch_config, config_commands)
            output = show_run_int(switch_config, command_input)
            output_view = generate_shut_noshut_modal(template_action, command_input, output)

            return jsonify({"response_action": "push", "view": output_view})
        
        elif template_action == "find_mac":
            switch_config = all_switch_configs[selected_option]
            command = f"sh mac add int {command_input}"
            output = send_command(switch_config, command)
            output_view = display_modal_ip_mac(command, output)

            return jsonify({"response_action": "push", "view": output_view})
        
        elif template_action == "find_ip":
            switch_config = all_switch_configs[selected_option]
            command1 = f"sh mac add int {command_input}"
            output1 = send_command(switch_config, command1)

            mac_address_pattern = re.compile(r'([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})')
            mac_address_match = mac_address_pattern.search(output1)
            mac_address = mac_address_match.group(0)
            command = f"sh ip arp {mac_address}"

            output = send_command(switch_config, command)
            output_view = display_modal_ip_mac(command, output)

            return jsonify({"response_action": "push", "view": output_view})

        
        else:
            # Handles submission of sending a regular command
            if selected_option and command_input:
                if selected_option in all_switch_configs:
                    switch_config = all_switch_configs[selected_option]
                    output = send_command(switch_config, command_input)

                    output_view = sending_any_command_modal(command_input, output)

                    return jsonify({"response_action": "push", "view": output_view})
    else:
        return ""

    return ""

if __name__ == "__main__":
    app.run(debug=True, port=9999)
