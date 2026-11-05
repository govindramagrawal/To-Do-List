# To-Do List

A small task manager built with Django. It lets users create tasks, edit their
details, mark them as done, and delete them.

## Features

- View all tasks, including their descriptions and creation times.
- Add a task with a title, description, and optional done status.
- Edit a task's title, description, and done status.
- Toggle a task's done status directly from the task list.
- Delete a task.

## Requirements

- Python
- Django 6.1.2 (listed in `requirements.txt`)

## Run locally

From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. The project uses SQLite, and Django
creates `db.sqlite3` when the database is migrated.

The settings include a development-only fallback secret key so the project can
run locally without extra configuration. Set the `DJANGO_SECRET_KEY`
environment variable to a private value before deployment; do not use the
development fallback in production.

## How the functionality works

### Viewing tasks

The root URL (`/`) is routed to the `home` view. The view queries all `Task`
objects and passes them to `home.html`. The template loops over them and renders
the task information in a table.

### Adding a task

The Add Task link opens `/add_task/`. The `add_task` view displays `add.html`
for a GET request. When the form is submitted with POST, the view reads the
title and description, checks whether the `done` checkbox was submitted, saves
a new `Task` to the database, and redirects to the task list.

### Editing a task

An Edit link opens `/edit_task/<task_id>/`. The `edit_task` view looks up that
task and supplies it to `edit.html` to prefill the form. On POST, the view
updates the submitted title, description, and done status, saves the task, and
redirects to the list.

### Checkbox and done status

Each task row in `home.html` has a checkbox inside a POST form. Django marks it
checked when `task.done` is true. Changing the checkbox submits the form to
`/toggle_done/<task_id>/`; `toggle_done` reads the submitted checkbox value,
updates the model's `done` field, saves it, and returns to the list.

The Add Task and Edit Task forms use the same checkbox convention: a checked
HTML checkbox submits the value `on`, while an unchecked checkbox is omitted
from the request. The views convert that into a Boolean for the model. The
checkbox's green checked appearance is provided by the `accent-color` rule in
`static/css/home.css`.

### Deleting a task

The Delete link includes the task's ID in `/delete_task/<task_id>/`. The
`delete_task` view retrieves that task, removes it from the database, and
redirects to the list.

## Django MVT structure

Django follows the Model-View-Template pattern:

- **Model** — `todo_list/models.py` defines `Task`, its title, description,
  done status, and creation time. Django ORM uses this model to store and
  retrieve records in SQLite.
- **View** — `todo_list/views.py` contains the functions that handle requests,
  query or update models, and choose a response.
- **Template** — `templates/` contains the HTML pages rendered by the views.
  The templates display data and provide forms and links for user actions.
- **URL routing** — `to_do/urls.py` includes the app routes from
  `todo_list/urls.py`, which connect paths such as `/add_task/` to their views.

For example, adding a task follows this path:
browser form → URL route → `add_task` view → `Task` model / SQLite → redirect
to the list → `home` view → `home.html` template.

## Project layout

```text
manage.py
to_do/                 Project settings and root URL configuration
todo_list/             Task model, views, routes, and database migrations
templates/             Task list, add, edit, and navigation templates
static/css/            Page styling
```
