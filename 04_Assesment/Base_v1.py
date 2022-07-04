from decorator_v3 import decorator
import intchecker
from choicechecker_v1 import choice_check
from rules_v1 import instructions

# Valid answers for future questio

yesno_ans = ["yes", "no"]
diff_list = ["easy", "medium", "hard", "custom"]

# Welcome to quiz messagge
decorator( "~", 4, 20, "|+=--", "--=+|","Welcome to The Worlds Hardest Quiz", "(it's not really)")

# Asks user if theyve played before
played_before = choice_check("\n|+=-- ~~~~ Have you played before? ~~~~ --+|", yesno_ans, "|+=-- ~~~~ Please answer yes or no ~~~~ --+|")

# If the player has played before they arent shown the instructions
if played_before == "no":
    instructions()

else:
    print()

difficulty = choice_check()