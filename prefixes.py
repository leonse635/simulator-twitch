prefixes = ["MODERATOR", "BOOSTER", "DEFAULT", "VIP"]

def add_prefix(new_prefix):
    if new_prefix not in prefixes:
        prefixes.append(new_prefix)
