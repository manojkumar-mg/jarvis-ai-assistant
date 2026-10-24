TOPIC_ALIASES = {
    "python programming": "python",
    "python language": "python",
    "java programming": "java",
    "java language": "java",
    "c programming": "c",
    "c language": "c",
    "sql language": "sql",
    "sql programming": "sql",
    "structured query language": "sql"
}


KNOWLEDGE_BASE = {
    "python": {
        "more": "Python is a high-level, interpreted programming language known for its simple syntax and readability.",
        "use": "Python is used for web development, automation, data science, artificial intelligence, and scripting.",
       "examples": [
                "For example, print('Hello, World!') displays Hello, World! on the screen.",
                "For example, name = 'Manoj'; print(name) stores and displays a name.",
                "For example, sum = 10 + 20; print(sum) calculates and displays 30."
                ],
        "simple": "Python is a programming language that lets you give instructions to a computer using simple, readable code.",
        "benefits": "Python is easy to learn, has a large community, offers many libraries, and supports several areas of development.",
        "disadvantages": "Python can be slower than compiled languages, may use more memory, and is not always ideal for mobile applications.",
        "how": "Python code is interpreted by the Python runtime, which executes your instructions to produce the required output.",
        
        "comparison": {
            "ease": "Python is generally easier for beginners because its syntax is readable and concise.",
            "ai": "Python is widely used for AI and machine learning because of libraries such as PyTorch, TensorFlow, and scikit-learn.",
            "performance": "Python is generally slower for CPU-intensive tasks than compiled languages, though optimized libraries can run operations efficiently."
        }

    },

    "c": {
        "more": "C is a general-purpose procedural programming language known for speed, efficiency, and low-level memory control.",
        "use": "C is used for operating systems, embedded systems, system software, and performance-critical applications.",
        "examples": [
                "For example, printf(\"Hello, World!\"); prints Hello, World! on the screen.",
                "For example, int age = 20; printf(\"%d\", age); displays 20.",
                "For example, int sum = 10 + 20; printf(\"%d\", sum); displays 30."
            ],
        "simple": "C is a programming language that gives you detailed control over how a computer works.",
        "benefits": "C is fast, efficient, portable, and provides direct memory access.",
        "disadvantages": "C requires careful memory management and does not provide some high-level features found in modern languages.",
        "how": "C source code is compiled into machine code, which the computer can execute directly.",
        
        "comparison": {
            "ease": "C is often harder for beginners because it requires careful handling of pointers, memory, and low-level details.",
            "ai": "C is useful for performance-critical AI components, but it is less commonly used than Python for everyday AI development.",
            "performance": "C can deliver high performance and fine-grained memory control when code is implemented efficiently."
        }

    },  
    
"sql": {
    "more": "SQL stands for Structured Query Language and is used to work with relational databases.",
    "use": "SQL is used to retrieve, insert, update, and delete data in relational databases.",
    "examples": [
            "For example, SELECT * FROM students; retrieves all records from the students table.",
            "For example, SELECT name FROM students; retrieves only the name column.",
            "For example, SELECT * FROM students WHERE age > 18; retrieves students older than 18."
        ],
    "simple": "SQL is a language that helps us store, find, and manage data in databases.",
    "benefits": "SQL makes data retrieval efficient, supports structured queries, and works with many database systems.",
    "disadvantages": "SQL databases can require careful schema design and may need additional strategies to scale across distributed systems.",
    "how": "SQL statements are sent to a database system, which processes the query and returns results or performs the requested operation.",
    
    "comparison": {
        "ease": "SQL is often approachable for beginners learning database queries, though advanced queries can be challenging.",
        "ai": "SQL is useful for retrieving and preparing data for AI, but it is not a general-purpose machine learning language.",
        "performance": "SQL performance depends heavily on query design, indexes, database configuration, and data size."
    }

},


    "java": {
        "more": "Java is a high-level, object-oriented programming language designed to be portable and reliable.",
        "use": "Java is used for backend development, Android applications, enterprise software, and distributed systems.",
        "examples": [
            "For example, System.out.println(\"Hello, World!\"); prints Hello, World! on the screen.",
            "For example, int age = 20; System.out.println(age); displays 20.",
            "For example, int sum = 10 + 20; System.out.println(sum); displays 30."
            ],
        "simple": "Java is a programming language that lets you build applications using classes and objects.",
        "benefits": "Java is portable, object-oriented, secure, widely used, and has a large ecosystem.",
        "disadvantages": "Java can use more memory than some languages and may require more code for simple tasks.",
        "how": "Java source code is compiled into bytecode, which runs on the Java Virtual Machine.",
        
        "comparison": {
            "ease": "Java has more explicit syntax and requires understanding classes and types, which may make it harder for some beginners.",
            "ai": "Java can be used for AI, but Python is more commonly chosen for experimentation and machine learning workflows.",
            "performance": "Java often performs well for long-running applications because the JVM can optimize code at runtime."
        }

    }

}



import re


def find_topic(query):
    topic = query.lower().strip()
    topic = re.sub(r"[^\w\s]", " ", topic)
    topic = " ".join(topic.split())

    # Check longer aliases first
    for alias in sorted(TOPIC_ALIASES, key=len, reverse=True):
        normalized_alias = " ".join(alias.lower().split())

        if f" {normalized_alias} " in f" {topic} ":
            return TOPIC_ALIASES[alias]

    # Match complete words, not letters inside unrelated words
    words = set(topic.split())

    for keyword in sorted(KNOWLEDGE_BASE, key=len, reverse=True):
        if keyword in words:
            return keyword

    return None


def find_topics(query):
    topic = re.sub(r"[^\w\s]", " ", query.lower())
    topic = " ".join(topic.split())
    found_topics = []

    for alias in sorted(TOPIC_ALIASES, key=len, reverse=True):
        normalized_alias = " ".join(alias.lower().split())

        if f" {normalized_alias} " in f" {topic} ":
            actual_topic = TOPIC_ALIASES[alias]

            if actual_topic not in found_topics:
                found_topics.append(actual_topic)

    words = set(topic.split())

    for keyword in KNOWLEDGE_BASE:
        if keyword in words and keyword not in found_topics:
            found_topics.append(keyword)

    return found_topics


def compare_topics(query, follow_up_type="simple"):
    topics = find_topics(query)

    if len(topics) < 2:
        return None

    labels = {
        "simple": "Overview",
        "use": "Main Use",
        "benefits": "Advantages",
        "disadvantages": "Limitations",
        "how": "How It Works"
    }

    rows = []

    for detail, label in labels.items():
        answers = []

        for topic in topics:
            knowledge = KNOWLEDGE_BASE.get(topic, {})
            answer = knowledge.get(detail)

            if answer:
                answers.append(answer.replace("|", "\\|"))
            else:
                answers.append("Not available")

        if any(answer != "Not available" for answer in answers):
            rows.append((label, answers))

    headers = [
        topic.upper() if topic == "sql" else topic.title()
        for topic in topics
    ]

    table = [
        "| Feature | " + " | ".join(headers) + " |",
        "|" + "---|" * (len(topics) + 1)
    ]

    for label, answers in rows:
        table.append(
            "| " + label + " | " + " | ".join(answers) + " |"
        )

    return "\n".join(table)
