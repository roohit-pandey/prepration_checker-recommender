# Placement Prep Recommender

questions = [
    # Searching
    {
        "question": "Time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
        "answer": "2",
        "topic": "Searching"
    },

    # Stack
    {
        "question": "Which uses LIFO?",
        "options": ["Queue", "Stack", "Array", "Graph"],
        "answer": "2",
        "topic": "Stack"
    },

    # Graphs
    {
        "question": "DFS is used in?",
        "options": ["Graphs", "Arrays", "Sorting", "Math"],
        "answer": "1",
        "topic": "Graphs"
    },

    # Arrays
    {
        "question": "Index of first element in array?",
        "options": ["0", "1", "-1", "Depends"],
        "answer": "1",
        "topic": "Arrays"
    },

    # Sorting
    {
        "question": "Worst case of bubble sort?",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(n log n)"],
        "answer": "3",
        "topic": "Sorting"
    },

    # Queue
    {
        "question": "Queue follows?",
        "options": ["LIFO", "FIFO", "Random", "None"],
        "answer": "2",
        "topic": "Queue"
    },

    # Recursion
    {
        "question": "Recursion uses?",
        "options": ["Loop", "Stack", "Queue", "Array"],
        "answer": "2",
        "topic": "Recursion"
    },

    # Time Complexity
    {
        "question": "Best case of linear search?",
        "options": ["O(n)", "O(1)", "O(log n)", "O(n^2)"],
        "answer": "2",
        "topic": "Complexity"
    }
]

score = 0
topic_scores = {}

print("=== Placement Preparation Quiz ===\n")

#Quiz
for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")
    
    for idx, opt in enumerate(q["options"], 1):
        print(f"{idx}. {opt}")
    
    ans = input("Enter option number: ")

    topic = q["topic"]
    topic_scores.setdefault(topic, [0, 0])
    topic_scores[topic][1] += 1

    if ans == q["answer"]:
        score += 1
        topic_scores[topic][0] += 1

    print()

#Level detection
if score <= 3:
    level = "Beginner"
elif score <= 6:
    level = "Intermediate"
else:
    level = "Advanced"

#Recommendations
recommendations = {
    "Beginner": ["Arrays", "Searching", "Basic Complexity"],
    "Intermediate": ["Stack", "Queue", "Sorting", "Recursion"],
    "Advanced": ["Graphs", "Dynamic Programming", "Greedy"]
}

#Weak topic detection
weak_topics = []
for topic, (correct, total) in topic_scores.items():
    if correct / total < 0.5:
        weak_topics.append(topic)

#Output
print("=== RESULT ===")
print("Score:", score, "/", len(questions))
print("Level:", level)

print("\n Recommended Topics to Study:")
for t in recommendations[level]:
    print("-", t)

print("\n Your Weak Areas:")
if weak_topics:
    for t in weak_topics:
        print("-", t)
else:
    print("None, good job!")

print("\n Tip:")
if level == "Beginner":
    print("Focus on basics and practice easy problems daily.")
elif level == "Intermediate":
    print("Start solving medium-level DSA problems regularly.")
else:
    print("Practice advanced problems and mock interviews.")