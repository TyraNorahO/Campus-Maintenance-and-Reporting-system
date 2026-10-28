
from nicegui import ui


def show_home():
    # Navigation bar
    with ui.row().classes(
        "w-full items-center justify-between px-8 py-4"
    ).style("background:#173B68; color:white"):

        ui.label("CampusCare").classes("text-2xl font-bold")

        with ui.row().classes("items-center gap-3"):
            ui.button(
                "Home",
                on_click=lambda: ui.navigate.to("/")
            ).props("flat color=white")

            ui.button(
                "Login",
                on_click=lambda: ui.navigate.to("/student-dashboard")
            ).props("flat color=white")

            ui.button(
                "Register",
                on_click=lambda: ui.notify(
                    "Registration page coming soon"
                )
            ).props("outline color=white")

    # Hero section
    with ui.column().classes(
        "w-full items-center text-center px-6 py-24 gap-5"
    ).style("background:#F3F6FB"):

        ui.label(
            "CAMPUS MAINTENANCE MADE SIMPLE"
        ).classes(
            "text-sm font-bold tracking-widest"
        ).style("color:#3B82F6")

        ui.label(
            "A Better Campus Starts Here"
        ).classes(
            "text-5xl font-bold"
        ).style("color:#173B68")

        ui.label(
            "A smarter way to report campus problems, monitor repairs "
            "and create a better learning environment."
        ).classes(
            "text-lg max-w-2xl"
        ).style("color:#526174")

        with ui.row().classes("gap-4 mt-4"):
            ui.button(
                "Report an Issue",
                on_click=lambda: ui.navigate.to("/report")
            ).props(
                "unelevated color=primary"
            ).classes("px-5")

            ui.button(
                "Track Reports",
                on_click=lambda: ui.navigate.to("/my-reports")
            ).props(
                "outline color=primary"
            ).classes("px-5")

    # Features section
    with ui.column().classes(
        "w-full items-center px-6 py-16 gap-4"
    ):
        ui.label(
            "How CampusCare Helps"
        ).classes(
            "text-3xl font-bold"
        ).style("color:#173B68")

        ui.label(
            "Everything you need to keep campus facilities in good condition."
        ).classes(
            "text-center text-gray-600"
        )

        with ui.row().classes(
            "w-full justify-center gap-6 flex-wrap mt-6"
        ):
            features = [
                (
                    "campaign",
                    "Report Issues",
                    "Report broken equipment, plumbing problems "
                    "and other campus maintenance concerns."
                ),
                (
                    "track_changes",
                    "Track Progress",
                    "Keep up with the progress and status of "
                    "your maintenance reports."
                ),
                (
                    "build",
                    "Faster Repairs",
                    "Help maintenance teams organise issues "
                    "and prioritise necessary repairs."
                ),
            ]

            for symbol, title, description in features:
                with ui.card().classes(
                    "w-80 p-6"
                ).style("border-radius:14px"):
                    ui.icon(
                        symbol, size="2.5rem"
                    ).style("color:#3B82F6")

                    ui.label(title).classes(
                        "text-xl font-bold"
                    )

                    ui.label(description).classes(
                        "text-gray-600"
                    )

    # Footer
    with ui.row().classes(
        "w-full justify-center p-5"
    ).style("background:#173B68; color:white"):
        ui.label(
            "CampusCare © 2026 | Campus Maintenance and Reporting System"
        )
