import pyjokes

# Define the function to give a neutral joke


def neutral_joke():
    return pyjokes.get_joke()


if __name__ == "__main__":
    print(neutral_joke())
