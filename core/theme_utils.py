def highlight_buttons(buttons, match_fn):
    for btn in buttons:
        if match_fn(btn):
            btn.setProperty("class", "highlight")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

def clear_highlights(buttons, restore_class_fn):
    for btn in buttons:
        original = restore_class_fn(btn)
        btn.setProperty("class", original)
        btn.style().unpolish(btn)
        btn.style().polish(btn)
        