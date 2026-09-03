import time

print("===== TYPING SPEED TEST =====")

sentence = "Python makes programming fun and interesting"

print("\nType this sentence:")
print(f'"{sentence}"')

input("\nPress Enter when you're ready...")

start_time = time.time()

user_text = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

words = len(user_text.split())
speed = words / (time_taken / 60)

print("\n===== RESULT =====")
print(f"Time taken : {time_taken:.2f} seconds")
print(f"Words typed: {words}")
print(f"Typing speed: {speed:.2f} WPM")

if user_text == sentence:
    print("Accuracy: 100% 🎯")
else:
    print("Accuracy: Needs improvement 💪")

print("\nKeep practicing! 🚀")