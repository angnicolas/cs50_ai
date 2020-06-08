from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


knowledgeBase = And(
    Or(AKnight,AKnave), 
    Not(And(AKnight,AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight,BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight,CKnave)),

)


def check_statement(person,statement):
    if person == 'A':
        sentence = Or(
            And(AKnight, statement ),
            And(AKnave, Not(statement))
        )
        return sentence
    elif person == 'B':
        sentence = Or(
            And(BKnight, statement ),
            And(BKnave, Not(statement)) )
        return sentence
    elif person == 'C':
        sentence = Or(
            And(CKnight, statement ),
            And(CKnave, Not(statement))
        )
        return sentence


# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    knowledgeBase,
    check_statement('A', And(AKnight,AKnave))
)
    




# knowledge0.add( Not(AKnight))


# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    knowledgeBase,
    check_statement('A',And(AKnave,BKnave))
)
 



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    knowledgeBase,
    check_statement('A', Or( And(AKnave,BKnave), And(AKnight, BKnight))),
    check_statement('B', Or( And(AKnave,BKnight), And(AKnight, BKnave)))
    

)
    


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

knowledge3 = And(
    knowledgeBase,
    Or(check_statement('A',AKnight),check_statement('A',AKnave)),
    Not(And(check_statement('A',AKnight),check_statement('A',AKnave))),
    check_statement('B',check_statement('A',AKnave)),
    check_statement('B',CKnave),
    check_statement('C',AKnight)
)

    


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
