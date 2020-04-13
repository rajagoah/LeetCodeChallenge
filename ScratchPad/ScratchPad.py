class person():
    def __init__(self, John):
        self.name = John

    def show(self):
        return self.name

if __name__ == "__main__":
    prs = person('John')
    print(prs.show())



