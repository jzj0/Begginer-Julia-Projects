function play_mad_libs()

    print("Enter a verb (action): ")
    verb1 = readline()

    print("Enter an adjective (descriptive word): ")
    adj1 = readline()

    print("Enter a noun (person place or thing): ")
    noun1 = readline()

    print("Enter another noun (person place or thing): ")
    noun2 = readline()

    print("Enter a catchphrase (something like 'hands up!'): ")
    phrase1 = readline()
    
    base_sentence = "Julia was $verb1 yesterday, talking to her $adj1 $noun1. When all of a 
    sudden, a $noun2 fell and said $phrase1"
    print("\n\n", base_sentence)
end

play_mad_libs()
