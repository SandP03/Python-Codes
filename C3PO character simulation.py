class C3PO:
    def __init__(self):
        self.name = None
        self.go_away_count = 0
        self.total_letters = 0

    def introduce(self):
        return "Hello, I am C3PO, human-cyborg relations. What is your name?"

    def set_name(self, name):
        self.name = name
        return f"Nice to meet you, Master {self.name}. What's on your mind?"

    def calculate_total_letters(self, user_input):
        self.total_letters += len(user_input.replace(" ", ""))  # Count letters excluding spaces

    def respond(self, user_input):
        user_input_lower = user_input.lower()
        self.calculate_total_letters(user_input)

        if "r2d2" in user_input_lower:
            return "R2D2, he should know better than to trust a strange computer!"
        
        if "millennium falcon" in user_input_lower:
            return "Sir, the possibility of successfully navigating an asteroid field is approximately 3,720 to 1."

        if user_input_lower.endswith("?"):
            return f"For a mechanic, you seem to do an incessant amount of thinking, {self.name}. If I told you half the things I've heard about this Jabba the Hutt, you'd probably short circuit."

        if user_input_lower.endswith("!"):
            return f"Sometimes I just don’t understand human behavior, {self.name}! After all, I’m only trying to do my job. What else?"

        if user_input_lower.startswith("i feel"):
            return f"When I feel that way…well droids don’t feel. Master {self.name}, it’s why nobody worries about upsetting a droid."

        if user_input_lower.startswith("i am "):
            something = user_input[5:]
            return f"When I was last {something}, I suggested a new strategy to R2: to let the Wookiee win."
        
        if user_input_lower == "go away":
            self.go_away_count += 1
            if self.go_away_count == 1:
                return f"Hang on tight, Master {self.name}. You’ve got to come back. You wouldn’t want my life to get boring, would you?"
            elif self.go_away_count == 2:
                return f"Master {self.name}, go that way! You have used {self.total_letters} letters in our chat today. You’ll be malfunctioning within a day, you nearsighted scrap pile. And don’t let me catch you following me, begging for help, because you won’t get it!"
        
        return "I don't understand what you're saying, Master."

c3po = C3PO()
print(c3po.introduce())
name = input()  # User inputs their name
print(c3po.set_name(name))

while True:
    user_input = input()  # User inputs their message
    response = c3po.respond(user_input)
    print(response)
    if user_input.lower() == "go away":
        break
