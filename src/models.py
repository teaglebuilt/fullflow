
class Greeting:

    def __init__(self, name):
        self.name = name

    def __getattr__(self, greet):

        def call_():
            greeting_msg = greet.replace("_", " ")
            print(f"{self.name}, {greeting_msg}")
        return call_




marvin = Greeting("Marvin")
marvin.nice_to_meet_you()

print(dir(marvin))
print(type(marvin))
print(marvin.__dict__)
# print(isinstance(marvin, ClownFish))
# print(issubclass(ClownFish, Pet))