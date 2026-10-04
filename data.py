# ==========================================================
# LEARNGRAPH AI - DATA
# ==========================================================

# ----------------------------------------------------------
# SKILLS / GRAPH NODES
# ----------------------------------------------------------

SKILLS = [
    "Python",
    "Data Structures",
    "Algorithms",
    "Mathematics",
    "Statistics",
    "Machine Learning",
    "Deep Learning",
    "Generative AI"
]


# ----------------------------------------------------------
# GRAPH RELATIONSHIPS
# ----------------------------------------------------------
# (prerequisite, next skill)

PREREQUISITES = [
    ("Python", "Data Structures"),
    ("Data Structures", "Algorithms"),
    ("Algorithms", "Machine Learning"),
    ("Statistics", "Machine Learning"),
    ("Machine Learning", "Deep Learning"),
    ("Deep Learning", "Generative AI")
]


# ----------------------------------------------------------
# LEARNING MATERIALS
# ----------------------------------------------------------

LEARNING_MATERIALS = {

    "Python": {
        "description": "Learn the fundamentals of Python programming.",
        "topics": [
            "Variables and Data Types",
            "Conditions and Loops",
            "Functions",
            "Lists, Tuples and Dictionaries",
            "Object-Oriented Programming"
        ],
        "resources": [
            ("Python Official Tutorial", "https://docs.python.org/3/tutorial/")
        ],
        "projects": [
            "Build a Calculator",
            "Create a To-Do List",
            "Build a Number Guessing Game"
        ],
        "hours": 10
    },


    "Data Structures": {
        "description": "Learn how data can be organized and efficiently accessed.",
        "topics": [
            "Arrays and Lists",
            "Stacks",
            "Queues",
            "Hash Tables",
            "Trees",
            "Graphs"
        ],
        "resources": [
            ("GeeksforGeeks Data Structures",
             "https://www.geeksforgeeks.org/data-structures/")
        ],
        "projects": [
            "Build a Stack",
            "Build a Queue",
            "Implement a Binary Search Tree"
        ],
        "hours": 12
    },


    "Algorithms": {
        "description": "Learn fundamental algorithms and problem-solving techniques.",
        "topics": [
            "Searching Algorithms",
            "Sorting Algorithms",
            "Recursion",
            "Breadth First Search",
            "Depth First Search",
            "Shortest Path Algorithms"
        ],
        "resources": [
            ("Algorithms - GeeksforGeeks",
             "https://www.geeksforgeeks.org/fundamentals-of-algorithms/")
        ],
        "projects": [
            "Build a Sorting Visualizer",
            "Build a Maze Solver",
            "Implement BFS and DFS"
        ],
        "hours": 15
    },


    "Mathematics": {
        "description": "Learn mathematical foundations useful for AI and machine learning.",
        "topics": [
            "Linear Algebra",
            "Vectors",
            "Matrices",
            "Functions",
            "Probability Basics"
        ],
        "resources": [
            ("Khan Academy Mathematics",
             "https://www.khanacademy.org/math")
        ],
        "projects": [
            "Matrix Calculator",
            "Probability Simulator"
        ],
        "hours": 15
    },


    "Statistics": {
        "description": "Learn statistics required for understanding machine learning.",
        "topics": [
            "Mean and Median",
            "Variance and Standard Deviation",
            "Probability",
            "Distributions",
            "Correlation",
            "Hypothesis Testing"
        ],
        "resources": [
            ("Khan Academy Statistics",
             "https://www.khanacademy.org/math/statistics-probability")
        ],
        "projects": [
            "Analyze a Dataset",
            "Build a Statistics Dashboard"
        ],
        "hours": 15
    },


    "Machine Learning": {
        "description": "Learn how machines learn patterns from data.",
        "topics": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Linear Regression",
            "Classification",
            "Decision Trees",
            "Model Evaluation"
        ],
        "resources": [
            ("Scikit-learn Documentation",
             "https://scikit-learn.org/stable/")
        ],
        "projects": [
            "House Price Predictor",
            "Spam Email Classifier",
            "Customer Classification System"
        ],
        "hours": 20
    },


    "Deep Learning": {
        "description": "Learn neural networks and deep learning concepts.",
        "topics": [
            "Neural Networks",
            "Activation Functions",
            "Backpropagation",
            "CNNs",
            "RNNs",
            "Model Training"
        ],
        "resources": [
            ("Deep Learning with PyTorch",
             "https://pytorch.org/tutorials/")
        ],
        "projects": [
            "Image Classifier",
            "Handwritten Digit Recognition",
            "Simple Neural Network"
        ],
        "hours": 25
    },


    "Generative AI": {
        "description": "Learn how modern AI systems generate text, images and other content.",
        "topics": [
            "Large Language Models",
            "Transformers",
            "Attention Mechanism",
            "Prompt Engineering",
            "Retrieval Augmented Generation",
            "AI Agents"
        ],
        "resources": [
            ("Hugging Face",
             "https://huggingface.co/learn")
        ],
        "projects": [
            "Build a Chatbot",
            "Build a Mini RAG System",
            "Build an AI Question Answering System"
        ],
        "hours": 30
    }
}