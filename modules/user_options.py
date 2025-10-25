def choose_option(prompt, options):
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    choice = int(input("Select a number: ")) - 1
    return list(options)[choice]
