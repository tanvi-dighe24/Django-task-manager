# Django Task Manager 📝:



-simple, functional Task Management application built to practice Full-Stack development using Python, Django, and SQL.

⚙️ How It Works (The Technical Flow):


✅
-This application follows the MVT (Model-View-Template) architecture, which is the standard for Django development. Here is the step-by-step journey of a "Task":

1. The Data Layer (Model & SQL)
The application defines a Task object in models.py. When a task is created, Django translates this Python object into a row in the SQLite database.

Fields stored: Title, Description, Completion Status, and a Timestamp.

2. The Logic Layer (View)
When a user visits the homepage, the views.py function (the "Brain") acts as a bridge:

It queries the database: Task.objects.all().

It packages that data into a "Context" dictionary.

It sends that package to the HTML template.

3. The Presentation Layer (Template & Static)
The index.html file uses Django Template Language (the {% for %} loops) to dynamically generate a list of tasks.

CSS (style.css): Provides the layout, ensuring the app is clean and responsive.

JavaScript (script.js): Handles the "Client-Side" logic. When you click "delete," JavaScript removes the element from the screen instantly for a smooth user experience.

4. The Routing Layer (URLs)
The urls.py files in both the project and app folders act as the "GPS." They ensure that when a user types in your web address, they are directed to the correct view logic.

#🚀 Technologies Used
* Backend: Python 3.x, Django Framework
* Database: SQLite (SQL)
* Frontend: HTML5, CSS3 (Flexbox), JavaScript (Vanilla)

# 📂 Project Structure
This project follows the Django MVT (Model-View-Template) architecture:


task_manager/
│
├── myproject/          # Project configuration (settings.py, urls.py)
├── tasks/              # App logic (models.py, views.py, urls.py)
├── templates/          # HTML files (index.html)
└── static/             # Assets (style.css, script.js)
