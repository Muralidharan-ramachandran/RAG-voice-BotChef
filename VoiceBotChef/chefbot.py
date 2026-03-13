import speech_recognition as sr
from pdf_loader import load_recipes
from retriever import RecipeRetriever
from voice import speak
from llm import ask_llm

# Load recipe book
recipes = load_recipes("South-Indian_cook_book.pdf")
retriever = RecipeRetriever(recipes)

r = sr.Recognizer()

print("ChefBot is ready! Speak now...")

while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=6)

        # Speech to text
        query = r.recognize_google(audio)
        print("User:", query)

        # Retrieve recipe context
        context = retriever.search(query)
        print("\nRetrieved recipe context:\n", context[:500])  # debug print

        # Ask LLM
        answer = ask_llm(context, query)
        print("\nChefBot:", answer)

        # Speak answer
        speak(answer)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")

    except sr.WaitTimeoutError:
        print("No speech detected. Please speak again.")

    except Exception as e:
        print("Actual error:", e)