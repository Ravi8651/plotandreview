class Jungle:
    def __init__(self, name="Unknown"):
        self.visitorName = name
    def welcomeMessage(self):
        print("Hello %s , Welcome to the Jungle" % self.visitorName)
