# liveface.py
# A simple text-based mood detector that shows a face emoji

def detect_mood(mood):
    mood = mood.lower()
    faces = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "surprised": "😲",
        "love": "😍",
        "bored": "😐"
    }
    return faces.get(mood, "🤔 (I don't know that mood yet!)")

if __name__ == "__main__":
    user_mood = input("Enter your mood: ")
    print(detect_mood(user_mood))
