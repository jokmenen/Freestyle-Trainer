import panel as pn
from pathlib import Path

def create_tabs_from_md():
    drill_folder = Path() / 'drills'
    md_files = drill_folder.glob('*.md')
    tabs = pn.Tabs()
    for file_path in md_files:
        with open(file_path, encoding='utf-8') as fp:
            drill = fp.read()

        tabs.append(pn.pane.Markdown(drill, name=file_path.stem))
    return tabs

def define_sidebar_component(sidebar):
    # Sidebar toggle button
    closed_text = '<'
    open_text = '>'
    toggle_button = pn.widgets.Button(name=open_text, width=20)

    # This function toggles the visibility of the sidebar
    def toggle_sidebar(event):
        sidebar.visible = not sidebar.visible
        toggle_button.name = open_text if sidebar.visible else closed_text

    toggle_button.on_click(toggle_sidebar)

    # Initial state of the sidebar is visible
    sidebar.visible = True

    sidebar_column = pn.Column(toggle_button, sidebar)
    return sidebar_column

if __name__ == '__main__':
    tabs = create_tabs_from_md()
    define_sidebar_component(tabs)