class WeightCalc:
    def ConvertWeight(self, given_weight:float, type:str)->float:
        if type.lower() == "l": # means convert to Kgs
            print("Weight in Kg: ", end="")
            return given_weight*0.453592
        elif type.lower() == "k": # means convert to Lbs
            print("Weight in Lbs: ", end="")
            return given_weight*2.20462
        else:
            print("Undefined Weight or weight type. Please try again...")

if __name__ == "__main__":
    S = WeightCalc()
    weight = float(input("Enter your weight: "))
    type = input("(K)g or (L)bs: ")
    print(S.ConvertWeight(weight, type))