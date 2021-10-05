class Jungle:
    def __init__(self, name="Unknown"):
         self.visitorName = name

    def welcomeMessage(self):
        print("welcome to jungle ",self.visitorName)
j = Jungle("ravi")
j.welcomeMessage()