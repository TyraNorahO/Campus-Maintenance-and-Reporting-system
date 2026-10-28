
from nicegui import ui


def show_student_dashboard():

    # Page layout
    with ui.row().classes("w-full min-h-screen no-wrap gap-0").style(
        "background:#F4F7FB"
    ):

        # Sidebar
        with ui.column().classes(
            "w-64 min-h-screen p-5 gap-6"
        ).style("background:#173B68; color:white"):

            ui.label("CampusCare").classes("text-2xl font-bold")
            ui.label("STUDENT PORTAL").classes(
                "text-xs tracking-widest"
            ).style("color:#B9D0EC")

            ui.separator().style("background:#49688D")

            ui.button(
                "Dashboard",
                on_click=lambda: ui.navigate.to("/student-dashboard")
            ).props("flat color=white align=left icon=dashboard").classes("w-full")

            ui.button(
                "Report an Issue",
                on_click=lambda: ui.navigate.to("/report")
            ).props("flat color=white align=left icon=add_circle").classes("w-full")

            ui.button(
                "My Reports",
                on_click=lambda: ui.navigate.to("/my-reports")
            ).props("flat color=white align=left icon=assignment").classes("w-full")

            ui.space()

            ui.button(
                "Home",
                on_click=lambda: ui.navigate.to("/")
            ).props("flat color=white align=left icon=home").classes("w-full")

        # Main dashboard area
        with ui.column().classes("flex-1 p-6 md:p-10 gap-6"):

            # Header
            with ui.row().classes(
                "w-full items-center justify-between"
            ):
                with ui.column().classes("gap-1"):
                    ui.label("Student Dashboard").classes(
                        "text-3xl font-bold"
                    ).style("color:#173B68")

                    ui.label(
                        "Welcome back! Here's your maintenance overview."
                    ).classes("text-gray-600")

                ui.icon("account_circle", size="2.8rem").style(
                    "color:#173B68"
                )

            # Summary cards
            with ui.grid(columns=2).classes("w-full md:grid-cols-4 gap-4"):

                cards = [
                    ("Total Reports", "12", "assignment", "#E8F0FE"),
                    ("Pending", "04", "schedule", "#FFF3D6"),
                    ("In Progress", "05", "build", "#E6F4FF"),
                    ("Resolved", "03", "check_circle", "#E3F7EC"),
                ]

                for title, number, symbol, background in cards:
                    with ui.card().classes("p-4").style(
                        "border-radius:14px"
                    ):
                        with ui.row().classes(
                            "w-full items-center justify-between"
                        ):
                            ui.label(title).classes("text-gray-600")
                            ui.icon(symbol).style(
                                f"color:#173B68; background:{background}; "
                                "padding:8px; border-radius:10px"
                            )

                        ui.label(number).classes(
                            "text-3xl font-bold mt-2"
                        ).style("color:#173B68")

            # Main content
            with ui.row().classes("w-full items-start gap-6 flex-wrap"):

                # Recent reports
                with ui.column().classes("flex-1 min-w-64 gap-3"):
                    with ui.row().classes(
                        "w-full items-center justify-between"
                    ):
                        ui.label("Recent Reports").classes(
                            "text-xl font-bold"
                        ).style("color:#173B68")

                        ui.button(
                            "View All",
                            on_click=lambda: ui.navigate.to("/my-reports")
                        ).props("flat color=primary")

                    sample_reports = [
                        ("Broken classroom lights", "Block A, Room 12", "Pending"),
                        ("Leaking water tap", "Student washrooms", "In Progress"),
                        ("Damaged classroom chair", "Block B, Room 4", "Resolved"),
                    ]

                    for title, location, status in sample_reports:
                        with ui.card().classes("w-full p-4"):
                            with ui.row().classes(
                                "w-full items-center justify-between"
                            ):
                                ui.label(title).classes("font-bold")
                                ui.badge(status)

                            ui.label(location).classes("text-gray-600 text-sm")

                # Quick actions
                with ui.card().classes("w-full md:w-64 p-5 gap-3"):
                    ui.label("Quick Actions").classes(
                        "text-xl font-bold"
                    ).style("color:#173B68")

                    ui.label(
                        "Need something fixed on campus?"
                    ).classes("text-gray-600")

                    ui.button(
                        "Report an Issue",
                        on_click=lambda: ui.navigate.to("/report")
                    ).props("unelevated color=primary").classes("w-full")

                    ui.button(
                        "Track My Reports",
                        on_click=lambda: ui.navigate.to("/my-reports")
                    ).props("outline color=primary").classes("w-full")

            ui.label(
                "CampusCare | Campus Maintenance and Reporting System"
            ).classes("text-sm text-gray-500 mt-6")


