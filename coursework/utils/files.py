import json


def get_dict_from_json(json_path: str) -> dict:
    with open(json_path, 'r') as json_file:
        current_status_dict = json.load(json_file)
    return current_status_dict


def update_json(json_path: str, input_dict: dict) -> None:
    with open(json_path, 'w') as json_file:
        json.dump(input_dict, json_file, indent=2)