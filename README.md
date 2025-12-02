# Todo Manager

#### Video Demo: https://youtu.be/Ow-YrAVDjCk

#### Description:
Todo Manager is my CS50 final project: a web-based application built with Python and Flask designed to help users efficiently manage their daily tasks. It allows users to create, update, delete, mark tasks as complete, and filter tasks based on their status. The project uses SQLite as a lightweight, self-contained database, demonstrating fundamental CRUD operations, routing, templating, and state management. This project aims to showcase a fully functional, minimal, and polished web application while applying core concepts learned throughout CS50’s curriculum.

The decision to use Flask was deliberate due to its lightweight nature and flexibility. Flask allows developers to focus on implementing core functionalities such as routing, templates, database integration, and form handling without the overhead of larger frameworks. SQLite was chosen over other databases like PostgreSQL to keep the project self-contained, easy to set up, and directly runnable on any machine. This decision mirrors CS50’s emphasis on simplicity and efficiency in problem sets, ensuring that the project remains accessible while demonstrating real-world web application development concepts.

The database schema is simple yet functional, containing essential fields for a task: id (unique identifier), text (task description), created_at (timestamp of creation using Python’s datetime module), completed (boolean status), and priority (low, medium, high). Priority levels are color-coded in the UI to give users immediate visual feedback. While I considered adding additional fields like due dates or user accounts, I intentionally kept the scope minimal to emphasize CRUD operations and core application logic, reflecting CS50’s focus on building functional and clean solutions.

The application structure follows best practices for Flask projects. The main file, app.py, handles all routing and request processing. It includes routes for the homepage (/), adding tasks (/add), editing tasks (/edit/<int:id>), marking tasks as complete (/complete/<int:id>), deleting tasks (/delete/<int:id>), and filtering tasks using URL parameters. Each route uses redirects after POST requests to prevent form resubmission issues. By centralizing routing logic, the project remains organized and maintainable.

Database operations are modularized in database.py, which contains functions such as init_db() for table creation, get_tasks() with optional filtering, add_task(), update_task(), toggle_complete(), and delete_task(). This separation promotes code reusability and simplifies testing. I debated including object-relational mapping (ORM) tools like SQLAlchemy but decided to use raw SQLite queries to provide a clear, hands-on demonstration of SQL integration, as emphasized in CS50’s web track lectures.

Frontend templates are implemented using Jinja2, enabling dynamic rendering of tasks. index.html loops over all tasks, displaying each with conditional formatting based on completion status and priority. add.html and edit.html pre-populate forms where applicable, demonstrating data flow from backend to frontend. Static files in the static/ folder, including style.css and script.js, provide responsive design and interactive features. For example, flash messages automatically fade using JavaScript’s setTimeout() function, enhancing the user experience. The UI emphasizes clarity and accessibility, with minimalistic design, intuitive navigation, and responsive layouts suitable for mobile and desktop devices.

Input validation is handled server-side to prevent empty or invalid submissions. Flash messages are categorized by type—success, error, and info—and styled consistently for easy user feedback. Filtering leverages both SQL queries and Python list comprehension for flexibility, allowing users to view all tasks, only pending tasks, or only completed tasks. These features demonstrate key CS50 skills such as conditional logic, error handling, dynamic content rendering, and user-centric design.

Testing was performed manually by creating tasks with various priorities, marking them complete, editing text, deleting tasks, and verifying that filtering worked correctly. Additionally, the project was tested in multiple browsers to ensure responsive behavior and cross-browser compatibility. Challenges encountered included ensuring correct updates to task states and properly handling flash messages after redirects. These issues were resolved through careful debugging and code modularization, reinforcing CS50’s lessons on problem-solving and iterative development.

The project includes a requirements.txt file that lists dependencies, primarily Flask and its associated packages. To run the project, a user simply needs to clone the repository, create a virtual environment, install dependencies, and launch the Flask development server. This ease of setup ensures that the project is fully reproducible, a key consideration in CS50’s project guidelines.

Overall, Todo Manager demonstrates a comprehensive understanding of full-stack development concepts, integrating database management, backend routing, frontend rendering, and responsive UI design into a cohesive, functional application. While the project’s scope is intentionally limited, it reflects thoughtful design choices, attention to user experience, and adherence to best practices, making it a practical and polished example of applying CS50 lessons to real-world web development.

# Features
- Add tasks with priority levels (low/medium/high)
- Edit and delete tasks
- Mark tasks as complete/incomplete
- Filter tasks (All / Pending / Completed)
- Flash messages for success/error/info with auto-fade JS
- Responsive UI with CSS (mobile-friendly)

# Tech Stack
- Python 3.x
- Flask (web framework)
- SQLite (database)
- Jinja2 (templating)
- HTML5, CSS3, Vanilla JavaScript

# How to Run
1. Clone the repository:
    git clone https://github.com/omarnagy1/Todo-Manager
2. Create and activate a virtual environment:
    python -m venv venvvenv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux)
3. Install dependencies:
    pip install -r requirements.txt
4. Run the server:
    flask run
5. Open in browser:
    http://127.0.0.1:5000/

## Screenshots

### Home Page
![Home Page](https://github.com/omarnagy1/Todo-Manager/blob/main/home.png)

### Add Task Page
![Add Task](https://github.com/omarnagy1/Todo-Manager/blob/main/add_task.png)

## Help

You can reach out to me if you have any questions
```
omarnagyyali@gmail.com
```

## Author
Omar Nagy
[My LinkedIn Profile](
https://www.linkedin.com/in/omar-nagy-7652b0364?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BUgMH%2B24ySY2P429J7iwdAA%3D%3D)

## Version History

* 1.0.0 — 2025-11-30
    * Initial commit


## License
This project is licensed under the MIT License - see the LICENSE file for details


