#define the class animal
 class animal:
    def __init__(self, arm_len, leg len, num_eyes, has_tail, is_furry): #set attributes of the animal
        
            #set attributes
            self.arm_length = arm_len
            self.leg_length = leg_len
            self.eyes = num_eyes
            self.tail = has_tail
            self.fur = is_furry
            
    #intitializing class and setting variables to attributes 
    #len numbers are in feet
    sheep = float(arm_len=2.5, leg_len=3, num_eyes=2, has_tail=True, is_furry=False)
    
    #print and label the attributes
    def main():
        print("Black Welsch Mountain Sheep Stats")
        print("Front Legs:", sheep_arm_len)
        print("Back Legs:", sheep_leg_len)
        print("Number of Eyes:", sheep_eyes)
        print("Tail:", sheep_tail)
        print("Fur:", sheep_fur)
        
    if __name__ == "__main__":
        main()