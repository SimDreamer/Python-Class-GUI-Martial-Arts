# Test Martial Arts class.
import Martial_Arts


def main():
    # instance
    martial_art = Martial_Arts.Martial_Arts_Class(20, 240.21, 1)
    martial_art.rank_promote()
    martial_art.rank_same()
    martial_art.print_class_variables()
    martial_art1 = Martial_Arts.Martial_Arts_Class(10, 80.23, 4)
    martial_art1.print_class_variables()
    martial_art1.rank_promote()
    martial_art1.print_class_variables()


# call main.
main()
