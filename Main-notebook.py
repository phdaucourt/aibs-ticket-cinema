import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Ticket de cinéma
    """)
    return


@app.cell
def _():
    import marimo as mo
    from datetime import datetime
    import locale
    from ticket_svg import générer_ticket

    return datetime, générer_ticket, locale, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Saisie de l'âge du client
    """)
    return


@app.cell
def _(mo):
    age = mo.ui.slider(1,100,1, label="Âge du client", show_value=True, value=50, debounce=True)
    age
    return (age,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Détermination du prix du ticket selon l'âge du client
    """)
    return


@app.cell
def _(age):
    if age.value < 12:
        categorie = "ENFANT"
        prix = 5.00
    elif 12 <= age.value <= 25:
        categorie = "ÉTUDIANT"
        prix = 7.00
    elif 25 < age.value <= 65:
        categorie = "NORMAL"
        prix = 10.00
    else:
        categorie = "SÉNIOR"
        prix = 6.00
    return categorie, prix


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Création de la date du jour
    """)
    return


@app.cell
def _(datetime, locale):
    locale.setlocale(locale.LC_TIME, 'fr_CH.UTF-8') #Suisse romande

    date = datetime.now().strftime('%A %d %B %Y').capitalize()
    return (date,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Affichage du ticket
    """)
    return


@app.cell
def _(categorie, date, générer_ticket, mo, prix):
    mo.Html(générer_ticket(date, categorie, prix))
    return


if __name__ == "__main__":
    app.run()
