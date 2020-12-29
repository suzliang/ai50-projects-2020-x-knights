from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    
    Implication(AKnight, And(AKnave, AKnight)),
    Implication(AKnave, Or(AKnave, AKnight)),
)
# AKnave

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnave, AKnight),
    Implication(AKnight, Not(AKnave)),
    Or(BKnave, BKnight),
    Implication(BKnight, Not(BKnave)),
    
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(AKnight, And(AKnave, BKnave)),
)
# AKnave and BKnight

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight),
    Implication(AKnight, Not(AKnave)),
    Or(BKnave, BKnight),
    Implication(BKnight, Not(BKnave)),

    Implication(AKnave, And(AKnave, BKnight)),
    Implication(AKnight, And(AKnight, BKnight)),
    Implication(BKnave, And(AKnave, BKnave)),
    Implication(BKnight, And(AKnave, BKnight)),
)
# AKnave, BKnight

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Implication(AKnight, Not(AKnave)),
    Or(BKnave, BKnight),
    Implication(BKnight, Not(BKnave)),
    Or(CKnave, CKnight),
    Implication(CKnight, Not(CKnave)),

    Implication(AKnave, AKnight),
    Implication(AKnight, AKnight),
    Biconditional(BKnave, CKnight),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnave, AKnave), 
    Biconditional(CKnight, AKnight),
    # A can only say 'I am a knight.'
    Implication(BKnave, AKnight),
    Implication(BKnight, AKnave),
)
# AKnight, BKnave, CKnight


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
