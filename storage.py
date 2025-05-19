import json
import os
from datetime import datetime

REQUIRED_KEYS = {
    'used',
    'task_number',
    'done',
    'done_with_help',
    'total_time',
    'min_time',
    'max_time',
    'min_task',
    'max_task',
    'history'
}

def load_data(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Błąd: Niepoprawny format JSON w pliku {filename}")
            return None
    if not validate_data(data):
        print(f"Błąd: Brak wymaganych kluczy w pliku {filename}")
        return None
    return data

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def validate_data(data):
    if not isinstance(data, dict):
        return False
    return REQUIRED_KEYS.issubset(data.keys())

def init_new_data():
    return {
        'used': True,
        'task_number': 1,
        'done': 0,
        'done_with_help': 0,
        'total_time': 0,
        'min_time': 10000,
        'max_time': 0,
        'min_task': 0,
        'max_task': 0,
        'history': []
    }

def update_history(history, done_inc, help_inc, seconds_spent):
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_entry = None
    for entry in history:
        if entry['date'] == today_str:
            today_entry = entry
            break
    if today_entry:
        today_entry['done'] += done_inc
        today_entry['help'] += help_inc
        today_entry['seconds'] += seconds_spent
    else:
        history.append({
            'date': today_str,
            'done': done_inc,
            'help': help_inc,
            'seconds': seconds_spent
        })
    return history
