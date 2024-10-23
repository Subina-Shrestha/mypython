class animal:
    name=""
    leg=0
    lives=""
    def printDetails(self):#class bhitra ko methods lai run garna ko lagi self as a parameter
        print(f"the {self.name} having {self.legs} lives in {self.lives}")
al=animal()
al.name="dog"
al.legs=4
al.lives="land"
al.printDetails()
