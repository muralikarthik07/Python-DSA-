class student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    #Setters for name
    def set_name(self, name):
        if name.strip() == "":
            print("Invalid name")
        else:
            self._name = name

    #Getter for name
    def get_name(self):
        return self._name
    
    #setter for roll number
    def set_roll_no (self, roll_no):
        if 1<= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("roll number should be between 1 and 100")

    #Getter for roll number
    def get_roll_no(self):
        return self._roll_no
    
    #Setter for marks
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("marks cannot be negative")

    #Getter for marks
    def get_marks(self):
        return self._marks


s1 = student("karthik", 10, 85)
print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())