from reactpy import component, html, run, hooks

@component
def Gallery(width, height):
    is_show, set_is_show = hooks.use_state(false)
    
    if is_show:
        return html.img(
            {
                "src": f"https://picsum.photos/{width}/{height}",
                "alt": "testing....",
            }
        )
    else:
        return html.h5("gambar akan muncul kalau tombol di klik")
    

@component
def Button():
    def show_image_handler():

@component
def App():
    return html._(
        html.h1("Testing REACTPY"),
        Gallery(width=720, height=480),
    )


run(App)