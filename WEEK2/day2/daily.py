import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} is out of range. Total pages: {self.total_pages}")
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return "\n".join(self.get_visible_items())


if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("=== get_visible_items ===")
    print(p.get_visible_items())
    # ['a', 'b', 'c', 'd']

    print("\n=== next_page ===")
    p.next_page()
    print(p.get_visible_items())
    # ['e', 'f', 'g', 'h']

    print("\n=== last_page ===")
    p.last_page()
    print(p.get_visible_items())
    # ['y', 'z']

    print("\n=== method chaining ===")
    p.first_page()
    print(p.next_page().next_page().next_page().get_visible_items())
    # ['m', 'n', 'o', 'p']

    print("\n=== __str__ ===")
    p.first_page()
    print(str(p))

    print("\n=== go_to_page ValueError ===")
    try:
        p.go_to_page(10)
    except ValueError as e:
        print(e)

    try:
        p.go_to_page(0)
    except ValueError as e:
        print(e)