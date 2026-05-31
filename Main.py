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
    from babel.dates import format_date
    import datetime

    return datetime, format_date, mo


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
def _(datetime, format_date):
    date = format_date(datetime.date.today(), format='long', locale='fr_CH')
    return (date,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Affichage du ticket
    """)
    return


@app.cell
def _(categorie, date, mo, prix):
    svg = f"""
          <svg width="100%" viewBox="0 0 680 320" role="img" xmlns="http://www.w3.org/2000/svg">
      <title>Ticket de cinéma</title>
      <desc>Ticket de cinéma avec catégorie et prix configurables</desc>
      <defs>
        <clipPath id="clip-ticket">
          <rect x="90" y="40" width="500" height="240" rx="12"/>
        </clipPath>
      </defs>

      <!-- Fond principal -->
      <rect x="90" y="40" width="500" height="240" rx="12" fill="#991B1B"/>

      <!-- Bande gauche -->
      <rect x="90" y="40" width="130" height="240" fill="#B91C1C" clip-path="url(#clip-ticket)"/>

      <!-- Séparateur pointillé -->
      <line x1="220" y1="60" x2="220" y2="260" stroke="#FECACA"
            stroke-width="1" stroke-dasharray="6 5" opacity="0.5"/>

      <!-- Demi-cercles de découpe -->
      <circle cx="90"  cy="160" r="16" fill="white"/>
      <circle cx="590" cy="160" r="16" fill="white"/>

      <!-- Icône pellicule -->
      <circle cx="155" cy="140" r="40" fill="none" stroke="#FECACA" stroke-width="2"   opacity="0.6"/>
      <circle cx="155" cy="140" r="28" fill="none" stroke="#FECACA" stroke-width="1.5" opacity="0.4"/>
      <circle cx="155" cy="140" r="10" fill="#FECACA" opacity="0.7"/>
      <circle cx="155" cy="104" r="4"  fill="#FECACA" opacity="0.5"/>
      <circle cx="155" cy="176" r="4"  fill="#FECACA" opacity="0.5"/>
      <circle cx="119" cy="140" r="4"  fill="#FECACA" opacity="0.5"/>
      <circle cx="191" cy="140" r="4"  fill="#FECACA" opacity="0.5"/>

      <!-- Label CINÉMA -->
      <text x="155" y="215" text-anchor="middle"
            font-family="sans-serif" font-size="11" font-weight="500"
            fill="#FECACA" letter-spacing="3" opacity="0.9">CINÉMA</text>

      <!-- Titre du film -->
      <text x="250" y="78"
            font-family="sans-serif" font-size="18" font-weight="500"
            fill="#FEF2F2">2001 Odysée de l'espace</text>
      <text x="250" y="96"
            font-family="sans-serif" font-size="11"
            fill="#FECACA" opacity="0.8">Salle 4 · VF · 2h15</text>

      <!-- Séparateurs -->
      <line x1="240" y1="108" x2="570" y2="108" stroke="#FECACA" stroke-width="0.5" opacity="0.3"/>
      <line x1="240" y1="160" x2="570" y2="160" stroke="#FECACA" stroke-width="0.5" opacity="0.3"/>
      <line x1="240" y1="210" x2="570" y2="210" stroke="#FECACA" stroke-width="0.5" opacity="0.3"/>

      <!-- Date -->
      <text x="250" y="130" font-family="sans-serif" font-size="11" fill="#FECACA" opacity="0.7">DATE</text>
      <text x="250" y="147" font-family="sans-serif" font-size="13" font-weight="500" fill="#FEF2F2">{date}</text>

      <!-- Séance -->
      <text x="420" y="130" font-family="sans-serif" font-size="11" fill="#FECACA" opacity="0.7">SÉANCE</text>
      <text x="420" y="147" font-family="sans-serif" font-size="13" font-weight="500" fill="#FEF2F2">20h30</text>

      <!-- Siège -->
      <text x="250" y="180" font-family="sans-serif" font-size="11" fill="#FECACA" opacity="0.7">SIÈGE</text>
      <text x="250" y="197" font-family="sans-serif" font-size="13" font-weight="500" fill="#FEF2F2">Rang G · Place 14</text>

      <!-- ============================================ -->
      <!-- VARIABLE 1 — CATÉGORIE : modifier ici        -->
      <text x="420" y="180" font-family="sans-serif" font-size="11" fill="#FECACA" opacity="0.7">CATÉGORIE</text>
      <text x="420" y="197" font-family="sans-serif" font-size="13" font-weight="500" fill="#FEF2F2">{categorie}</text>

      <!-- Numéro de billet -->
      <text x="250" y="235" font-family="monospace" font-size="11" fill="#FECACA" opacity="0.6">N° 0042-8817-C</text>

      <!-- ============================================ -->
      <!-- VARIABLE 2 — PRIX : modifier ici             -->
      <text x="570" y="235" text-anchor="end"
            font-family="sans-serif" font-size="22" font-weight="500"
            fill="#FEF2F2">{prix:.2f} CHF</text>
      <!-- ============================================ -->

    </svg>
    """
    mo.Html(svg)
    return


if __name__ == "__main__":
    app.run()
