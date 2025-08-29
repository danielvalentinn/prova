import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = 'TODO List'

    todos = [
        {"task": "Create Flet app", "completed": False},
        {"task": "Final touches", "completed": False},
        {"task": "Deploy app", "completed": False},
    ]

    filter_mode = "all"  # all, active, completed

    task_list = ft.Column(spacing=10, width=600)

    def update_list():
        task_list.controls.clear()

        if filter_mode == "all":
            filtered_todos = todos
        elif filter_mode == "active":
            filtered_todos = [t for t in todos if not t["completed"]]
        else:  # completed
            filtered_todos = [t for t in todos if t["completed"]]

        for idx, todo in enumerate(filtered_todos):
            checkbox = ft.Checkbox(
                label=todo["task"],
                value=todo["completed"],
                on_change=lambda e, i=idx: toggle_complete(i, filtered_todos),
                expand=True,
            )
            edit_button = ft.IconButton(
                icon=ft.Icons.EDIT,
                tooltip="Edit",
                on_click=lambda e, i=idx: edit_task(i, filtered_todos),
            )
            delete_button = ft.IconButton(
                icon=ft.Icons.DELETE,
                tooltip="Delete",
                on_click=lambda e, i=idx: delete_task(i, filtered_todos),
            )
            row = ft.Row(
                controls=[checkbox, edit_button, delete_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
            task_list.controls.append(row)

        active_count.value = f"{len([t for t in todos if not t['completed']])} active item(s) left"
        page.update()

    def toggle_complete(index, current_list):
        # Descobre o índice real no todos
        todo = current_list[index]
        todo_index = todos.index(todo)
        todos[todo_index]["completed"] = not todos[todo_index]["completed"]
        update_list()

    def delete_task(index, current_list):
        todo = current_list[index]
        todos.remove(todo)
        update_list()

    def edit_task(index, current_list):
        def save_edit(e):
            todo = current_list[index]
            todo_index = todos.index(todo)
            todos[todo_index]["task"] = edit_input.value
            dialog.open = False
            update_list()

        todo = current_list[index]
        edit_input = ft.TextField(value=todo["task"], width=300)
        save_button = ft.ElevatedButton(text="Save", on_click=save_edit)
        dialog = ft.AlertDialog(
            title=ft.Text("Edit Task"),
            content=edit_input,
            actions=[save_button],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def add_task(e):
        task = input_todo.value.strip()
        if task:
            todos.append({"task": task, "completed": False})
            input_todo.value = ""
            update_list()
            page.update()

    def clear_completed(e):
        nonlocal todos
        todos = [t for t in todos if not t["completed"]]
        update_list()

    def on_tab_change(e: ft.ControlEvent):
        nonlocal filter_mode
        filter_mode = ["all", "active", "completed"][tabs.selected_index]
        update_list()

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=200,
        on_change=on_tab_change,
        width=600,
        indicator_color=ft.Colors.BLUE,
        label_color=ft.Colors.BLUE,
        unselected_label_color=ft.Colors.BLACK54,
        tabs=[
            ft.Tab(text="all"),
            ft.Tab(text="active"),
            ft.Tab(text="completed"),
        ],
    )

    input_todo = ft.TextField(
        label='What needs to be done?',
        width=500,
        border_radius=10,
        focused_border_color=ft.Colors.GREY_100,
        filled=True,
        fill_color=ft.Colors.GREY_100,
        content_padding=10,
    )

    add_button = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.GREY_800,
        bgcolor=ft.Colors.GREY_200,
        on_click=add_task,
    )

    input_row = ft.Row(
        controls=[input_todo, add_button],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
        width=600,
    )

    active_count = ft.Text()

    clear_button = ft.ElevatedButton(
        text="Clear completed",
        on_click=clear_completed,
        style=ft.ButtonStyle(
            padding=ft.padding.only(left=20, right=20),
        ),
    )

    bottom_row = ft.Row(
        controls=[active_count, clear_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=600,
    )

    page.add(input_row, tabs, task_list, bottom_row)

    update_list()

ft.app(target=main)
