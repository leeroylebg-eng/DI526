from datetime import datetime

def minutes_lived(birthdate_str):
    diff = datetime.now() - datetime.strptime(birthdate_str, "%Y-%m-%d")
    print(f"You have lived approximately {int(diff.total_seconds() / 60)} minutes!")

minutes_lived("1995-06-15")