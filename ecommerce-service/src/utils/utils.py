from datetime import datetime, timezone

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def filter_dict(dict, fields):

    filtered_dict = {}

    for key in dict:

        if key in fields:
            filtered_dict[key] = dict[key]

    return filtered_dict

def format_date(datetime):
    

    return datetime.strftime(DATE_FORMAT)

def get_current_datetime():

    
    return datetime.now(timezone.utc)