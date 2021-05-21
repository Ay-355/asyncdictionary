class Definition:
    def __init__(self, data):
        self.definition = data.get("definition")
        self.example = data.get("example")
        self.synonyms = data.get("synonyms")
