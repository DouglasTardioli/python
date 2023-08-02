import qdarktheme


def setupTheme():
    qdarktheme.setup_theme(
        theme="dark",
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": "#1e81b0"
            },
            "[light]": {
                "primary": "#1e81b0"
            },
        },
    )