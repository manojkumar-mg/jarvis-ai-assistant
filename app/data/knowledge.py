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
        "example": "For example, print('Hello, World!') displays Hello, World! on the screen.",
        "simple": "Python is a programming language that lets you give instructions to a computer using simple, readable code.",
        "benefits": "Python is easy to learn, has a large community, offers many libraries, and supports several areas of development.",
        "disadvantages": "Python can be slower than compiled languages, may use more memory, and is not always ideal for mobile applications.",
        "how": "Python code is interpreted by the Python runtime, which executes your instructions to produce the required output."
    },

    "c": {
        "more": "C is a general-purpose procedural programming language known for speed, efficiency, and low-level memory control.",
        "use": "C is used for operating systems, embedded systems, system software, and performance-critical applications.",
        "example": "For example, printf(\"Hello, World!\"); prints Hello, World! on the screen.",
        "simple": "C is a programming language that gives you detailed control over how a computer works.",
        "benefits": "C is fast, efficient, portable, and provides direct memory access.",
        "disadvantages": "C requires careful memory management and does not provide some high-level features found in modern languages.",
        "how": "C source code is compiled into machine code, which the computer can execute directly."
    },  
    
"sql": {
    "more": "SQL stands for Structured Query Language and is used to work with relational databases.",
    "use": "SQL is used to retrieve, insert, update, and delete data in relational databases.",
    "example": "For example, SELECT * FROM students; retrieves all records from the students table.",
    "simple": "SQL is a language that helps us store, find, and manage data in databases.",
    "benefits": "SQL makes data retrieval efficient, supports structured queries, and works with many database systems.",
    "disadvantages": "SQL databases can require careful schema design and may need additional strategies to scale across distributed systems.",
    "how": "SQL statements are sent to a database system, which processes the query and returns results or performs the requested operation."
},


    "java": {
        "more": "Java is a high-level, object-oriented programming language designed to be portable and reliable.",
        "use": "Java is used for backend development, Android applications, enterprise software, and distributed systems.",
        "example": "For example, System.out.println(\"Hello, World!\"); prints Hello, World! on the screen.",
        "simple": "Java is a programming language that lets you build applications using classes and objects.",
        "benefits": "Java is portable, object-oriented, secure, widely used, and has a large ecosystem.",
        "disadvantages": "Java can use more memory than some languages and may require more code for simple tasks.",
        "how": "Java source code is compiled into bytecode, which runs on the Java Virtual Machine."
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
