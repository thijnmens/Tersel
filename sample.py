from tersel import Tersel


class TerselTestClass:
    def __init__(self):
        self.text = "Custom"

    def __str__(self):
        return self.text


if __name__ == '__main__':
    print(
        Tersel("Select a framework", [
            "ASP.net",
            "Django",
            ["React", ["Typescript", "Javascript"]],
            TerselTestClass(),
        ], 4)
        .show()
    )
