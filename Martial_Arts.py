# Goal: Martial Arts class has class variables age, weight, rank number.
import Valid_Martial_Arts


class Martial_Arts_Class:
    def __init__(self, user_age=2, user_weight=240.2, user_rank=0):

        self.age = user_age
        self.weight = user_weight
        self.rank_num = user_rank
        self.rank_promote_flag = "False"
        Valid_Martial_Arts.validate(self.age, self.weight, self.rank_num)

    def rank_promote(self):
        rank_counter = str(self.rank_num + 1)  # increment counter
        self.rank_promote_flag = "True"
        match rank_counter:
            case "0":
                print("Rank promoted: White")
            case "1":
                print("Rank promoted: Yellow")
            case "2":
                print("Rank promoted: Blue")
            case "3":
                print("Rank promoted: Green")
            case "4":
                print("Rank promoted: 1st Purple")
            case "5":
                print("Rank promoted: 2nd Purple")
            case "6":
                print("Rank promoted: 1st Brown")
            case "7":
                print("Rank promoted: 2nd Brown")
            case "8":
                print("Rank promoted: 3rd Brown")
            case "9":
                print("Rank promoted: 1st Black")
            case other:
                print("Begginer Rank: White")

    def rank_same(self):
        print("Your Current Rank Number:" + str(self.rank_num))

    def print_class_variables(self):
        if self.rank_promote_flag == "True":
            self.rank_num = self.rank_num + 1
        else:
            pass
        print("Class Variables-")
        print("-----------------")
        print("Age: " + str(self.age))
        print("Weight: " + str(self.weight))
        print("Rank Number: " + str(self.rank_num))
