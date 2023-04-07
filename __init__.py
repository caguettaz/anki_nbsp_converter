from aqt import gui_hooks

def nbsp_to_space(text: str) -> str:
    return text.replace("&nbsp;", " ")

def on_editor_will_munge_html(text: str, editor_instance) -> str:
    return nbsp_to_space(text)

gui_hooks.editor_will_munge_html.append(on_editor_will_munge_html)
