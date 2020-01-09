def fix_address(address: str):
    return address \
        .lower() \
        .replace('.', ' ') \
        .replace('  ', ' ') \
        .strip()


def fix_name(name: str):
    return name \
        .lower() \
        .replace("'", ' ') \
        .replace('(', ' ') \
        .replace(')', ' ') \
        .replace('  ', ' ') \
        .strip()


def fix_phone(phone: str):
    return phone \
        .lower() \
        .replace('-', ' ') \
        .replace('/', ' ') \
        .replace('  ', ' ') \
        .strip()


def fix_type(t: str):
    return t \
        .lower() \
        .replace('(', ' ') \
        .replace(')', ' ') \
        .replace('  ', ' ') \
        .replace('/', ' ') \
        .strip()


def fix_city(city: str):
    return city \
        .lower() \
        .replace('.', '') \
        .replace('west ', 'w ') \
        .replace('north ', 'n ') \
        .replace('east ', 'e ') \
        .replace('south ', 's ') \
        .replace('  ', ' ') \
        .strip()


def clean_doc_list(doc_list: list):
    cleaned_list = []
    for item in doc_list:
        i = {
            'name': fix_name(item['name']),
            'address': fix_address(item['address']),
            'city': fix_city(item['city']),
            'phone': fix_phone(item['phone']),
            'type': fix_type(item['type']),
            'id': item['id']
        }
        cleaned_list.append(i)
    return cleaned_list
