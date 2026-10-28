
from nicegui import ui
from pages.home import show_home
from pages.student_dashboard import show_student_dashboard

@ui.page("/")
def home_page():
    show_home()

@ui.page("/student-dashboard")
def student_dashboard_page():
    show_student_dashboard()
    
ui.run(
    title="CampusCare | Campus Maintenance System",
    port=8080,
    reload=False
)
