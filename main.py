import time
import os

def get_report_path():
    # Save report in the user's home directory
    return os.path.join(os.path.expanduser("~"), "wellbeing_check_report.txt")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("==============================================")
    print("   🧠 WELLBEING CHECK-IN | PSYCH-LOGIC v1.0   ")
    print("==============================================\n")
    print("This is a general wellbeing check-in, not a medical diagnosis.\n"
          "If you feel unsafe or overwhelmed, please reach out to a mental health\n"
          "professional or someone you trust.\n")

def ask_questions():
    questions = [
        "1. Over the past 2 weeks, how often have you felt little interest or pleasure in doing things?",
        "2. Over the past 2 weeks, how often have you felt down, sad, or hopeless?",
        "3. Over the past 2 weeks, how often have you felt nervous, anxious, or on edge?",
        "4. Over the past 2 weeks, how often have you found it hard to control your worrying?",
        "5. Over the past 2 weeks, how often have you had trouble sleeping (falling asleep, staying asleep, or sleeping too much)?",
        "6. Over the past 2 weeks, how often have you felt tired or had little energy?",
        "7. Over the past 2 weeks, how often have you felt bad about yourself or felt like a failure?",
        "8. Over the past 2 weeks, how often have you had trouble concentrating (e.g., reading, work, or studies)?",
        "9. Over the past 2 weeks, how often have you avoided activities or people because of anxiety or low mood?",
        "10. Over the past 2 weeks, how often have your emotions interfered with your daily life (home, work, or relationships)?"
    ]

    print("\nAnswer each question with a number:")
    print("0 = Not at all | 1 = Several days | 2 = More than half the days | 3 = Nearly every day\n")

    total_score = 0
    for q in questions:
        print(q)
        while True:
            try:
                ans = int(input("Your answer (0–3): "))
                if ans in [0, 1, 2, 3]:
                    total_score += ans
                    break
                else:
                    print("Please enter 0, 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number (0–3).")
        print()
    return total_score

def interpret_score(total_score):
    if total_score <= 7:
        level = "LOW DISTRESS"
        summary = (
            "Your answers suggest relatively low levels of emotional distress.\n"
            "Keep taking care of your mental and physical wellbeing and stay aware of changes."
        )
    elif 8 <= total_score <= 17:
        level = "MODERATE DISTRESS"
        summary = (
            "Your answers suggest a moderate level of emotional distress.\n"
            "It might help to talk to someone you trust and consider speaking with a mental health professional."
        )
    else:
        level = "HIGH DISTRESS"
        summary = (
            "Your answers suggest a high level of emotional distress.\n"
            "This is not a diagnosis, but it would be a good idea to reach out to a mental health professional\n"
            "or a trusted person in your life for support as soon as you can."
        )
    return level, summary

def save_report(name, total_score, level):
    try:
        path = get_report_path()
        with open(path, "a", encoding="utf-8") as f:
            f.write(f"Name: {name} | Score: {total_score} | Status: {level}\n")
        print(f"\n✅ Report saved to: {path}")
    except Exception as e:
        print(f"\n❌ Could not save report: {e}")

def start_assessment():
    clear_screen()
    print_header()

    name = input("Enter Participant Name: ")

    total_score = ask_questions()

    print("\n[ANALYZING RESPONSES...]")
    time.sleep(2)

    level, summary = interpret_score(total_score)

    print("\n================= RESULT SUMMARY =================")
    print(f"Participant: {name}")
    print(f"Total Score: {total_score} (max 30)")
    print(f"Wellbeing Status: {level}")
    print("\nInterpretation:")
    print(summary)
    print("\nReminder: This tool does NOT replace professional evaluation or treatment.\n")

    save_report(name, total_score, level)

if __name__ == "__main__":
    start_assessment()
