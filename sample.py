from tersel import Tersel


class TerselTestClass:
    def __init__(self):
        self.text = "Option 5"

    def __str__(self):
        return self.text


if __name__ == '__main__':
    Tersel("Test options", [
        "Option 1",
        2,
        ["Option 3", "Option 4"],
        TerselTestClass()
    ], 2).show()
