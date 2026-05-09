import reflex as rx
 
# ── Colores ───────────────────────────────────────────────────────────────────
MINT   = "#7EC8A4"
LILA   = "#C9B8E8"
CREAM  = "#F5F0E8"
ORANGE = "#E8502A"
BLACK  = "#1A1A1A"
WHITE  = "#FFFFFF"
 
BTN = dict(
    background=MINT,
    color=BLACK,
    font_weight="700",
    font_size="0.82rem",
    padding="0.5rem 1.4rem",
    border_radius="20px",
    border=f"2px solid {BLACK}",
    cursor="pointer",
)
 
BTN_DARK = {**BTN, "background": BLACK, "color": WHITE}
 
LINK = dict(
    color=BLACK,
    font_size="0.82rem",
    font_weight="500",
    text_decoration="none",
    _hover={"text_decoration": "underline"},
)
 
 
# ══════════════════════════════════════════════════════════════════════════════
# PÁGINAS SIMPLES
# ══════════════════════════════════════════════════════════════════════════════
 
def pago() -> rx.Component:
    return rx.box(
        rx.text("Pagina de pago", font_size="2rem", font_weight="900", color=BLACK),
    )
 
 
def suscripcion() -> rx.Component:
    return rx.box(
        rx.text("Pagina de suscripcion", font_size="2rem", font_weight="900", color=BLACK),
    )
 
 
# ══════════════════════════════════════════════════════════════════════════════
# COMPONENTES PÁGINA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
 
def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("COD", font_weight="900", font_size="1.3rem", color=BLACK),
        rx.hstack(
            rx.link("Inicio",        **LINK, href="#inicio"),
            rx.link("Cómo funciona", **LINK, href="#como-funciona"),
            rx.link("Precios",       **LINK, href="#precios"),
            rx.link("FAQ",           **LINK, href="#faq"),
            spacing="5",
        ),
        rx.link(rx.button("GET A BUNDLE", **BTN), href="#precios"),
        justify="between",
        align="center",
        width="100%",
        padding="1rem 3rem",
        border_bottom=f"2px solid {BLACK}",
        background=WHITE,
        position="sticky",
        top="0",
        z_index="99",
    )
 
 
def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "CONTENT ON:DEMAND",
                font_size="5rem",
                font_weight="900",
                line_height="0.95",
                letter_spacing="-2px",
                color=BLACK,
            ),
            rx.text(
                "We take your content stress away, so you can focus on the bigger picture.",
                font_size="1rem",
                color=BLACK,
                max_width="460px",
            ),
            rx.link(rx.button("CHECK OUT BUNDLES", **BTN), href="#precios"),
            align_items="start",
            spacing="4",
        ),
        id="inicio",
        background=LILA,
        padding="5rem 3rem 4rem",
        border_bottom=f"2px solid {BLACK}",
    )
 
 
def countdown_section() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("5, 4, 3, 2, 1", font_size="1.6rem",
                        font_weight="900", color=BLACK),
                rx.text(
                    "That's how quickly\nwe turn around\nyour IG feed!",
                    font_size="2.4rem",
                    font_weight="900",
                    line_height="1.1",
                    color=BLACK,
                    white_space="pre-line",
                ),
                rx.text(
                    "Tú decides cuándo, qué y con qué frecuencia publicar. "
                    "Nosotros nos encargamos de que tu feed esté siempre lleno de contenido fresco y on-brand.",
                    font_size="0.88rem",
                    color="#444",
                    max_width="340px",
                    line_height="1.7",
                ),
                rx.link(rx.button("VER BUNDLES", **BTN), href="#precios"),
                align_items="start",
                spacing="3",
            ),
            rx.vstack(
                rx.box(
                    rx.text("BUSINESS OWNERS", font_weight="800",
                            font_size="0.78rem", color=BLACK, margin_bottom="0.5rem"),
                    rx.vstack(
                        *[rx.text(f"✦  {i}", font_size="0.77rem", color=BLACK)
                          for i in [
                              "Lanzar un nuevo producto",
                              "Preparar una venta",
                              "Educar a tu audiencia",
                              "Mantener tu página activa",
                          ]],
                        align_items="start",
                        spacing="1",
                    ),
                    background=CREAM,
                    border=f"2px solid {BLACK}",
                    border_radius="10px",
                    padding="1.2rem",
                    min_width="220px",
                ),
                rx.box(
                    rx.text("SOCIAL MEDIA MANAGERS", font_weight="800",
                            font_size="0.78rem", color=BLACK, margin_bottom="0.5rem"),
                    rx.vstack(
                        *[rx.text(f"✦  {i}", font_size="0.77rem", color=BLACK)
                          for i in [
                              "Mantener el calendario lleno",
                              "Preparar contenido con anticipación",
                              "Ser más creativo",
                          ]],
                        align_items="start",
                        spacing="1",
                    ),
                    background=MINT,
                    border=f"2px solid {BLACK}",
                    border_radius="10px",
                    padding="1.2rem",
                    min_width="220px",
                ),
                spacing="4",
            ),
            spacing="8",
            align_items="start",
            flex_wrap="wrap",
        ),
        padding="5rem 3rem",
        border_bottom=f"2px solid {BLACK}",
    )
 
 
def how_it_works() -> rx.Component:
    steps = [
        ("1", "Elige tu bundle",       "Mini (3 posts) o Signature (9 posts)."),
        ("2", "Llena el cuestionario", "Para que el contenido esté 100% on-brand."),
        ("3", "Publica cuando quieras","Recibes tu bundle listo para publicar."),
    ]
    return rx.box(
        rx.vstack(
            rx.text("¿Cómo funciona?", font_size="2.5rem",
                    font_weight="900", color=BLACK),
            rx.vstack(
                *[
                    rx.hstack(
                        rx.box(
                            rx.text(n, font_weight="900", color=WHITE, font_size="0.9rem"),
                            background=BLACK,
                            border_radius="50%",
                            width="28px",
                            height="28px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            flex_shrink="0",
                        ),
                        rx.vstack(
                            rx.text(t, font_weight="700", font_size="0.85rem", color=BLACK),
                            rx.text(d, font_size="0.78rem", color="#555", line_height="1.4"),
                            align_items="start",
                            spacing="1",
                        ),
                        spacing="3",
                        align_items="start",
                    )
                    for n, t, d in steps
                ],
                spacing="4",
                align_items="start",
            ),
            rx.link(rx.button("VER PRECIOS", **BTN), href="#precios"),
            align_items="start",
            spacing="4",
        ),
        id="como-funciona",
        background=CREAM,
        padding="5rem 3rem",
        border_bottom=f"2px solid {BLACK}",
    )
 
 
def testimonials() -> rx.Component:
    return rx.box(
        rx.text("Lo que dicen nuestros clientes",
                font_size="2rem", font_weight="900",
                color=BLACK, text_align="center"),
        rx.hstack(
            *[
                rx.box(
                    rx.text(txt, font_size="0.82rem", color=fg, line_height="1.6"),
                    rx.text(autor, font_size="0.75rem", font_weight="700",
                            color=fg, margin_top="0.8rem"),
                    background=bg,
                    border=f"2px solid {BLACK}",
                    border_radius="12px",
                    padding="1.2rem",
                    flex="1",
                    min_width="200px",
                )
                for txt, autor, bg, fg in [
                    ("Nada más positivo. El equipo es increíble y el resultado fue perfecto.",
                     "— Cliente feliz", MINT, BLACK),
                    ("El copywriting fue tan bueno que lo usé de inmediato. Muy recomendado.",
                     "— Otro cliente", ORANGE, WHITE),
                    ("La atención al detalle en cada post fue impresionante.",
                     "— Gran cliente", WHITE, BLACK),
                ]
            ],
            spacing="4",
            flex_wrap="wrap",
            margin_top="2rem",
        ),
        padding="5rem 3rem",
        border_bottom=f"2px solid {BLACK}",
    )
 
 
def pricing() -> rx.Component:
    def card(title, price, features, btn_label, btn_style, href, featured=False):
        return rx.box(
            rx.text(title, font_weight="800", font_size="1rem", color=BLACK),
            rx.text(price, font_size="2rem", font_weight="900",
                    color=BLACK, margin_y="0.6rem"),
            rx.vstack(
                *[
                    rx.hstack(
                        rx.text("✓" if ok else "✕",
                                color=MINT if ok else ORANGE,
                                font_weight="700"),
                        rx.text(f, font_size="0.78rem", color=BLACK),
                        spacing="2",
                    )
                    for f, ok in features
                ],
                spacing="1",
                align_items="start",
            ),
            rx.link(
                rx.button(btn_label, margin_top="1rem", **btn_style),
                href=href,
            ),
            background=WHITE,
            border=f"{'3' if featured else '2'}px solid {BLACK}",
            border_radius="14px",
            padding="1.8rem",
            flex="1",
            min_width="220px",
            box_shadow=f"5px 5px 0 {BLACK}" if featured else "none",
        )
 
    return rx.box(
        rx.vstack(
            rx.text("Elige tu Content Bundle 🚀",
                    font_size="2rem", font_weight="900",
                    color=BLACK, text_align="center"),
            rx.hstack(
                card(
                    "The Mini Bundle", "120 USD",
                    [("5-day turnaround", True), ("1 revisión", False),
                     ("Add-ons", False), ("Figma files", False)],
                    "COMPRAR MINI", BTN, "/pago",
                ),
                card(
                    "The Signature Bundle", "400 USD",
                    [("5-day turnaround", True), ("1 revisión", True),
                     ("Add-ons", True), ("Figma files", True)],
                    "COMPRAR SIGNATURE", BTN_DARK, "/pago",
                    featured=True,
                ),
                spacing="6",
                flex_wrap="wrap",
                justify_content="center",
                align_items="start",
            ),
            spacing="6",
            align_items="center",
        ),
        id="precios",
        background=LILA,
        padding="5rem 3rem",
        border_top=f"2px solid {BLACK}",
        border_bottom=f"2px solid {BLACK}",
    )
 
 
class FAQState(rx.State):
    open_index: int = -1
 
    def toggle(self, i: int):
        self.open_index = -1 if self.open_index == i else i
 
 
def faq_section() -> rx.Component:
    questions = [
        ("¿Cómo aseguran la consistencia de marca?",
         "Nos basamos en tu guía de estilo y cuestionario para mantener coherencia en cada post."),
        ("¿En qué formatos entregan los posts?",
         "Recibirás imágenes optimizadas para redes sociales y archivos editables si lo solicitas."),
        ("¿Ofrecen contenido por industria?",
         "Sí, adaptamos el contenido a tu sector para que sea relevante."),
        ("¿Cómo es el proceso de comunicación?",
         "Nos comunicamos por email y entregamos un cuestionario inicial para entender tu marca."),
        ("¿Qué pasa si no estoy feliz con mi bundle?",
         "Incluimos revisiones para ajustar el contenido hasta que estés satisfecho."),
        ("¿Cuándo recibo mis posts?",
         "El tiempo de entrega es de 5 días hábiles después de completar el cuestionario."),
        ("¿Puedo pedir templates editables?",
         "Sí, podemos entregarte archivos editables en Figma o similares."),
    ]
 
    return rx.box(
        rx.hstack(
            rx.text(
                "¿Tienes más\npreguntas?\n¡Te tenemos!",
                font_size="2.4rem",
                font_weight="900",
                line_height="1.1",
                color=BLACK,
                white_space="pre-line",
            ),
            rx.vstack(
                *[
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text(q, font_size="0.85rem",
                                        font_weight="600", color=BLACK, flex="1"),
                                rx.text(
                                    rx.cond(FAQState.open_index == i, "⌄", "›"),
                                    font_size="1.2rem",
                                    color=BLACK,
                                    font_weight="700",
                                ),
                                justify_content="space-between",
                                align_items="center",
                                padding="0.85rem 1rem",
                                cursor="pointer",
                                on_click=FAQState.toggle(i),
                            ),
                            rx.cond(
                                FAQState.open_index == i,
                                rx.text(a, font_size="0.78rem", color="#555",
                                        padding="0 1rem 0.8rem"),
                            ),
                        ),
                        border_bottom=f"1.5px solid {BLACK}",
                    )
                    for i, (q, a) in enumerate(questions)
                ],
                border=f"2px solid {BLACK}",
                border_radius="12px",
                overflow="hidden",
                spacing="0",
                align_items="stretch",
                flex="1",
                min_width="300px",
            ),
            spacing="8",
            align_items="start",
            flex_wrap="wrap",
        ),
        id="faq",
        background=MINT,
        padding="5rem 3rem",
        border_top=f"2px solid {BLACK}",
        border_bottom=f"2px solid {BLACK}",
    )
 
 
def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("COD", font_weight="900", font_size="1.2rem", color=WHITE),
                rx.text(
                    "Came for the content,\nstayed for the flow! 🌊",
                    font_size="1rem",
                    font_weight="700",
                    color=WHITE,
                    white_space="pre-line",
                ),
                rx.hstack(
                    rx.link("Inicio",        color=WHITE, font_size="0.78rem", href="#inicio"),
                    rx.link("Cómo funciona", color=WHITE, font_size="0.78rem", href="#como-funciona"),
                    rx.link("Precios",       color=WHITE, font_size="0.78rem", href="#precios"),
                    rx.link("FAQ",           color=WHITE, font_size="0.78rem", href="#faq"),
                    spacing="4",
                ),
                align_items="start",
                spacing="3",
            ),
            rx.vstack(
                rx.text("Newsletter", font_size="0.85rem",
                        font_weight="700", color=WHITE),
                rx.input(
                    placeholder="Email",
                    border=f"1.5px solid {WHITE}",
                    border_radius="8px",
                    background="transparent",
                    color=WHITE,
                    width="260px",
                    font_family="inherit",
                ),
                rx.link(
                    rx.button("SUBSCRIBE", **BTN, width="260px"),
                    href="/suscripcion",
                ),
                spacing="2",
                align_items="start",
            ),
            justify_content="space-between",
            align_items="start",
            flex_wrap="wrap",
            spacing="8",
        ),
        rx.divider(border_color="#444", margin_y="1.5rem"),
        rx.text("© COD. All rights reserved.", font_size="0.72rem", color="#aaa"),
        background=BLACK,
        padding="3rem 3rem 2rem",
    )
 
 
# ══════════════════════════════════════════════════════════════════════════════
# INDEX
# ══════════════════════════════════════════════════════════════════════════════
 
def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        countdown_section(),
        how_it_works(),
        testimonials(),
        pricing(),
        faq_section(),
        footer(),
        font_family="'DM Sans', sans-serif",
        background=WHITE,
    )
 
 
# ══════════════════════════════════════════════════════════════════════════════
# APP
# ══════════════════════════════════════════════════════════════════════════════
 
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap"
    ],
)
app.add_page(index,       route="/",           title="Content On Demand")
app.add_page(pago,        route="/pago",        title="Pago — COD")
app.add_page(suscripcion, route="/suscripcion", title="Suscripción — COD")