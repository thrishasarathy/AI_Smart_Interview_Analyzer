import random



class InterviewDatabase:

    def __init__(self):

        self.database = {

            "Python Developer": {

                "3-5 LPA": [

                    {"question":"What is Python?",
                     "answer":"Python is a high level interpreted programming language."},

                    {"question":"Explain OOP.",
                     "answer":"Object Oriented Programming is based on classes and objects."},

                    {"question":"What is List Comprehension?",
                     "answer":"List comprehension is a concise way to create lists."},

                    {"question":"What is Lambda Function?",
                     "answer":"Lambda is an anonymous function."},

                    {"question":"Difference between List and Tuple?",
                     "answer":"Lists are mutable while tuples are immutable."},

                    {"question":"What is Dictionary?",
                     "answer":"Dictionary stores data in key value pairs."},

                    {"question":"Explain For Loop.",
                     "answer":"For loop is used for iteration."},

                    {"question":"What is Function?",
                     "answer":"Function is a reusable block of code."}

                ],

                "5-8 LPA":[

                    {"question":"Explain Decorators.",
                     "answer":"Decorators modify the behaviour of functions."},

                    {"question":"What is Generator?",
                     "answer":"Generator yields values one by one."},

                    {"question":"What is Multithreading?",
                     "answer":"Multithreading executes multiple threads simultaneously."},

                    {"question":"Explain Exception Handling.",
                     "answer":"Exception handling manages runtime errors."},

                    {"question":"Difference between Process and Thread.",
                     "answer":"Process has separate memory while threads share memory."},

                    {"question":"Explain Modules.",
                     "answer":"Modules are reusable python files."},

                    {"question":"What is API?",
                     "answer":"API allows communication between applications."}

                ]

            },

            "AI Engineer":{

                "5-8 LPA":[

                    {"question":"What is Machine Learning?",
                     "answer":"Machine learning enables computers to learn from data."},

                    {"question":"Difference between AI and ML?",
                     "answer":"Machine learning is a subset of Artificial Intelligence."},

                    {"question":"What is Deep Learning?",
                     "answer":"Deep learning uses neural networks."},

                    {"question":"What is NLP?",
                     "answer":"Natural Language Processing enables computers to understand language."},

                    {"question":"What is Overfitting?",
                     "answer":"Overfitting happens when the model memorizes training data."},

                    {"question":"What is Underfitting?",
                     "answer":"Underfitting occurs when the model cannot learn patterns."},

                    {"question":"What is Supervised Learning?",
                     "answer":"Supervised learning uses labelled data."}

                ]

            }

        }

    def get_questions(self, job, package):
        return self.database[job][package]




class Evaluator:

    def calculate_score(self, user_answer, correct_answer):

        user_words = set(user_answer.lower().split())
        answer_words = set(correct_answer.lower().split())

        matched = len(user_words.intersection(answer_words))
        score = (matched / len(answer_words)) * 100

        return score




class InterviewSession:

    def __init__(self):

        self.db = InterviewDatabase()
        self.eval = Evaluator()

        self.name = ""
        self.job = ""
        self.package = ""
        self.final = 0

    def start(self):

        print("="*50)
        print("      AI SMART INTERVIEW ANALYZER")
        print("="*50)

        self.name = input("\nEnter Candidate Name : ")

        print("\nChoose Job Role")
        print("1. Python Developer")
        print("2. AI Engineer")

        job_choice = input("\nEnter Choice : ")

        if job_choice == "1":
            self.job = "Python Developer"
        elif job_choice == "2":
            self.job = "AI Engineer"
        else:
            print("Invalid Job Choice")
            return

        print("\nChoose Package")

        if self.job == "Python Developer":

            print("1. 3-5 LPA")
            print("2. 5-8 LPA")

            package_choice = input("Enter Choice : ")

            if package_choice == "1":
                self.package = "3-5 LPA"
            elif package_choice == "2":
                self.package = "5-8 LPA"
            else:
                print("Invalid Package")
                return

        else:

            print("1. 5-8 LPA")

            package_choice = input("Enter Choice : ")

            if package_choice == "1":
                self.package = "5-8 LPA"
            else:
                print("Invalid Package")
                return

        questions = self.db.get_questions(self.job, self.package)

        selected = random.sample(questions, 5)

        total = 0

        print("\nInterview Started...\n")

        for i, q in enumerate(selected, 1):

            print("-"*50)
            print(f"Question {i}")
            print(q["question"])

            user = input("\nYour Answer : ")

            score = self.eval.calculate_score(user, q["answer"])

            total += score

            print("\nExpected Answer :")
            print(q["answer"])
            print("Score :", round(score, 2), "%")
            print("-"*50)

        self.final = total / 5

        print("\n" + "="*50)
        print("Interview Completed")
        print("="*50)

        print("Candidate :", self.name)
        print("Job :", self.job)
        print("Package :", self.package)
        print("Overall Score :", round(self.final, 2), "%")

        if self.final >= 85:
            print("Result : Excellent")
        elif self.final >= 70:
            print("Result : Good")
        elif self.final >= 50:
            print("Result : Average")
        else:
            print("Result : Needs Improvement")




obj = InterviewSession()
obj.start()

print("\n" + "="*50)
print("INTERVIEW RESULT")
print("="*50)

print("Candidate Name    :", obj.name)
print("Applied Role      :", obj.job)
print("Expected Package  :", obj.package)
print("Overall Score     :", round(obj.final, 2), "%")

print("-"*50)

if obj.final >= 90:
    print("🎉 Congratulations!")
    print("Status : SELECTED")
    print("You have successfully cleared the interview.")
    print("Our HR team will contact you within 24 hours.")
    print("Welcome to the next round!")

elif obj.final >= 75:
    print("✅ Congratulations!")
    print("Status : SHORTLISTED")
    print("You performed well in the interview.")
    print("Our HR team will contact you for the next technical round.")

elif obj.final >= 60:
    print("📞 Status : ON HOLD")
    print("Thank you for attending the interview.")
    print("Your profile is under review.")
    print("We will get back to you within 3-5 working days.")

else:
    print("❌ Status : NOT SELECTED")
    print("Thank you for attending the interview.")
    print("We encourage you to improve your technical skills")
    print("and apply again in the future.")

print("="*50)
print("Thank you for using AI Smart Interview Analyzer.")
print("="*50)