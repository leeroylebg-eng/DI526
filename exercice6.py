# 1️⃣ difference
def difference(a, b):
    return a - b


# 2️⃣ print_day
def print_day(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num)


# 3️⃣ last_element
def last_element(lst):
    if len(lst) == 0:
        return None
    return lst[-1]


# 4️⃣ number_compare
def number_compare(a, b):
    if a > b:
        return "First is greater."
    elif b > a:
        return "Second is greater."
    return "Numbers are equal."


# 5️⃣ single_letter_count
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())


# 6️⃣ multiple_letter_count
def multiple_letter_count(string):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    return result


# 7️⃣ list_manipulation
def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "end":
            return lst.pop() if lst else None
        elif location == "beginning":
            return lst.pop(0) if lst else None

    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
        elif location == "end":
            lst.append(value)
        return lst


# 8️⃣ is_palindrome
def is_palindrome(string):
    cleaned = string.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# 9️⃣ frequency
def frequency(lst, search_term):
    return lst.count(search_term)


# 🔟 flip_case
def flip_case(string, letter):
    result = ""
    for char in string:
        if char.lower() == letter.lower():
            result += char.swapcase()
        else:
            result += char
    return result


# 1️⃣1️⃣ multiply_even_numbers
def multiply_even_numbers(lst):
    product = 1
    for num in lst:
        if num % 2 == 0:
            product *= num
    return product


# 1️⃣2️⃣ mode
def mode(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)


# 1️⃣3️⃣ capitalize
def capitalize(string):
    return string[0].upper() + string[1:] if string else ""


# 1️⃣4️⃣ compact
def compact(lst):
    return [item for item in lst if item]


# 1️⃣5️⃣ partition
def partition(lst, callback):
    true_list = []
    false_list = []
    for item in lst:
        if callback(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return [true_list, false_list]


# 1️⃣6️⃣ intersection
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# 1️⃣7️⃣ once
def once(func):
    has_run = False

    def wrapper(*args, **kwargs):
        nonlocal has_run
        if has_run:
            return None
        has_run = True
        return func(*args, **kwargs)

    return wrapper

