# EduGenie - Gemini Learning Assistant
# Simple Python demonstration

print("=" * 50)
print("       EduGenie - Learning Assistant")
print("=" * 50)
print("Ask a study question. Type 'exit' to stop.\n")

while True:
    question = input("Student: ")

    if question.lower() == "exit":
        print("EduGenie: Thank you! Keep learning!")
        break

    if "python" in question.lower():
        answer = "Python is a high-level programming language used for software development, data science and automation."

    elif "computer" in question.lower():
        answer = "A computer is an electronic device that processes data and produces useful information."

    elif "ai" in question.lower() or "artificial intelligence" in question.lower():
        answer = "Artificial Intelligence is technology that enables computers to perform tasks that normally require human intelligence."

    elif "algorithm" in question.lower():
        answer = "An algorithm is a step-by-step procedure used to solve a problem."

    else:
        answer = "EduGenie: This is a study question. Please explore the topic and learn the concept step by step."

    print("EduGenie:", answer)
    print()
