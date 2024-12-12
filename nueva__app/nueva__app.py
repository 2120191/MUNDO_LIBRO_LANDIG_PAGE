"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    


def index() -> rx.Component:
    return rx.container(

        rx.color_mode.button(position="top-right"),

        rx.vstack(
            rx.heading("BIENVENIDOS AL MUNDO DEL LIBRO!", size="9",color_scheme="gray"),
            rx.text(
                "La lectura es muy imporatante crea y desarrolla genios",
                size="8",color_scheme="gray"
            ),
            rx.hstack(
                
                rx.link(
                    rx.button("registrate aqui",color_scheme="green"),
                    href="https://forms.gle/Gj2CstmbZuhy1V2c9",
                ),
                rx.link(
                     rx.button(rx.icon(tag="facebook"),color_scheme="blue"),
                     href="https://facebook.com",
                    is_external=True,
                ),
                rx.link(
                     rx.button(rx.icon(tag="youtube"),color_scheme="tomato"),
                     href="https://youtube.com",
                     is_external=True,
                ),
                rx.link(
                     rx.button(rx.icon(tag="instagram"),color_scheme="purple"),
                     href="https://instagram.com",
                     is_external=True,
                ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),   
         height="100vh",
         width="100%",
         background="url('https://wallpaper.forfun.com/fetch/e7/e7bfc1edebf545897f7d266883c4a7f0.jpeg')",
         background_size="cover",
         background_position="center"
        
    )   
       
    

app = rx.App()
app.add_page(index)
