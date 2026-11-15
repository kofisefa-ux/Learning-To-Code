# Prompt the user for a greeting, strip leading whitespace, and convert to lowercase
greeting = input("Greeting: ").strip().lower()

# Check if the greeting starts with "hello"
if greeting.startswith("hello"):
    print("$0")

# Check if the greeting starts with an "h" (and not "hello")
elif greeting.startswith("h"):
    print("$20")

# Otherwise, output $100
else:
    print("$100")