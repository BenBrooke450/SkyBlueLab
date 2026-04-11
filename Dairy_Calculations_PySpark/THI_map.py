def map_of_europe():
    import json
    import os
    import plotly.express as px
    import pandas as pd
    import numpy as np

    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "nuts2.geojson")

    with open(file_path) as f:
        regions_geojson = json.load(f)



    valid_prefixes = ["ES", "FR", "DE", "IT", "PL", "UK", "IE", "SE"]

    filtered_features = [
        feature for feature in regions_geojson["features"]
        if any(feature["properties"]["id"].startswith(prefix) for prefix in valid_prefixes)
    ]

    regions_geojson["features"] = filtered_features
    nuts_ids = [feature["properties"]["id"] for feature in regions_geojson["features"]]


    humidity_profiles = {
        "Hyper_Oceanic": [88, 85, 83, 80, 78, 78, 79, 81, 83, 86, 88, 89],
        "Temperate_Maritime": [85, 81, 78, 74, 73, 73, 74, 75, 78, 82, 85, 86],
        "Continental_Standard": [84, 80, 74, 68, 66, 67, 68, 70, 76, 82, 86, 87],
        "Alpine_Boreal": [82, 78, 72, 65, 62, 64, 66, 68, 74, 80, 84, 85],
        "Arid_Continental_South": [78, 70, 60, 55, 48, 38, 30, 32, 45, 62, 74, 80],
        "Mediterranean_Coast": [72, 70, 68, 67, 66, 64, 62, 65, 68, 72, 73, 73],
        "Sub_Mediterranean": [80, 75, 70, 68, 67, 65, 62, 64, 70, 78, 82, 83],
        "Humid_Subtropical_Adriatic": [82, 76, 72, 70, 70, 70, 68, 70, 75, 80, 83, 84]
    }


    region_to_humidity = {
        'ES64': humidity_profiles["Mediterranean_Coast"], # Melilla
        'ES63': humidity_profiles["Mediterranean_Coast"], # Ceuta
        'ES61': humidity_profiles["Arid_Continental_South"], # Andalucía
        'ES62': humidity_profiles["Arid_Continental_South"], # Murcia
        'ES43': humidity_profiles["Arid_Continental_South"], # Extremadura
        'ES42': humidity_profiles["Arid_Continental_South"], # Castilla-La Mancha
        'ES30': humidity_profiles["Arid_Continental_South"], # Madrid
        'ES41': humidity_profiles["Arid_Continental_South"], # Castilla y León
        'ES24': humidity_profiles["Arid_Continental_South"], # Aragón
        'ITF4': humidity_profiles["Arid_Continental_South"], # Puglia
        'ITG1': humidity_profiles["Arid_Continental_South"], # Sicilia (Interior)
        'ITF6': humidity_profiles["Arid_Continental_South"], # Calabria
        'ITF5': humidity_profiles["Arid_Continental_South"], # Basilicata

        # Mediterranean Coastal & Island
        'ES52': humidity_profiles["Mediterranean_Coast"], # Valencia
        'ES53': humidity_profiles["Mediterranean_Coast"], # Baleares
        'ES51': humidity_profiles["Mediterranean_Coast"], # Cataluña
        'FRJ1': humidity_profiles["Mediterranean_Coast"], # Languedoc-Roussillon
        'FRL0': humidity_profiles["Mediterranean_Coast"], # PACA
        'FRM0': humidity_profiles["Mediterranean_Coast"], # Corse
        'ITG2': humidity_profiles["Mediterranean_Coast"], # Sardegna
        'ITC3': humidity_profiles["Mediterranean_Coast"], # Liguria
        'ITF3': humidity_profiles["Mediterranean_Coast"], # Campania
        'ITI1': humidity_profiles["Mediterranean_Coast"], # Toscana
        'ITI3': humidity_profiles["Mediterranean_Coast"], # Marche
        'ITI4': humidity_profiles["Mediterranean_Coast"], # Lazio

        # Atlantic / Hyper-Oceanic
        'IE04': humidity_profiles["Hyper_Oceanic"], # Northern and Western IE
        'IE05': humidity_profiles["Hyper_Oceanic"], # Southern IE
        'IE06': humidity_profiles["Hyper_Oceanic"], # Eastern and Midland IE
        'UKM9': humidity_profiles["Hyper_Oceanic"], 'UKM8': humidity_profiles["Hyper_Oceanic"],
        'UKM7': humidity_profiles["Hyper_Oceanic"], 'UKM5': humidity_profiles["Hyper_Oceanic"],
        'UKM6': humidity_profiles["Hyper_Oceanic"], # Scotland
        'UKN0': humidity_profiles["Hyper_Oceanic"], # Northern Ireland
        'UKL1': humidity_profiles["Hyper_Oceanic"], 'UKL2': humidity_profiles["Hyper_Oceanic"], # Wales
        'UKK3': humidity_profiles["Hyper_Oceanic"], # Cornwall
        'FRH0': humidity_profiles["Hyper_Oceanic"], # Bretagne
        'ES11': humidity_profiles["Hyper_Oceanic"], # Galicia
        'ES12': humidity_profiles["Hyper_Oceanic"], # Asturias
        'ES13': humidity_profiles["Hyper_Oceanic"], # Cantabria

        # Temperate Maritime (Western/Coastal North)
        'ES21': humidity_profiles["Temperate_Maritime"], # País Vasco
        'FRI1': humidity_profiles["Temperate_Maritime"], # Aquitaine
        'FRI3': humidity_profiles["Temperate_Maritime"], # Poitou-Charentes
        'FRG0': humidity_profiles["Temperate_Maritime"], # Pays de la Loire
        'FRD1': humidity_profiles["Temperate_Maritime"], 'FRD2': humidity_profiles["Temperate_Maritime"], # Normandy
        'FRE1': humidity_profiles["Temperate_Maritime"], 'FRE2': humidity_profiles["Temperate_Maritime"], # North FR
        'UKK4': humidity_profiles["Temperate_Maritime"], 'UKK2': humidity_profiles["Temperate_Maritime"],
        'UKJ3': humidity_profiles["Temperate_Maritime"], 'UKK1': humidity_profiles["Temperate_Maritime"],
        'UKI6': humidity_profiles["Temperate_Maritime"], 'UKI3': humidity_profiles["Temperate_Maritime"],
        'UKI4': humidity_profiles["Temperate_Maritime"], 'UKI7': humidity_profiles["Temperate_Maritime"],
        'UKI5': humidity_profiles["Temperate_Maritime"], 'UKJ2': humidity_profiles["Temperate_Maritime"],
        'UKJ4': humidity_profiles["Temperate_Maritime"], 'UKH3': humidity_profiles["Temperate_Maritime"],
        'UKD3': humidity_profiles["Temperate_Maritime"], 'UKD4': humidity_profiles["Temperate_Maritime"],

        # Continental Standard (Central Europe)
        'DE': humidity_profiles["Continental_Standard"], # Default for German DE codes listed
        'PL': humidity_profiles["Continental_Standard"], # Default for Polish PL codes listed
        'FR10': humidity_profiles["Continental_Standard"], # Ile-de-France
        'FRF2': humidity_profiles["Continental_Standard"], # Champagne-Ardenne
        'FRC1': humidity_profiles["Continental_Standard"], # Bourgogne
        'FRB0': humidity_profiles["Continental_Standard"], # Centre
        'ES23': humidity_profiles["Continental_Standard"], # La Rioja
        'ES22': humidity_profiles["Continental_Standard"], # Navarra
        'ITC4': humidity_profiles["Continental_Standard"], # Lombardia
        'ITH5': humidity_profiles["Continental_Standard"], # Emilia-Romagna

        # Alpine & Boreal (High Altitude / Nordic)
        'ITC2': humidity_profiles["Alpine_Boreal"], # Valle d’Aosta
        'ITH1': humidity_profiles["Alpine_Boreal"], # Bolzano
        'ITH2': humidity_profiles["Alpine_Boreal"], # Trento
        'DE21': humidity_profiles["Alpine_Boreal"], # Oberbayern
        'SE11': humidity_profiles["Alpine_Boreal"], 'SE12': humidity_profiles["Alpine_Boreal"],
        'SE21': humidity_profiles["Alpine_Boreal"], 'SE22': humidity_profiles["Alpine_Boreal"],
        'SE33': humidity_profiles["Alpine_Boreal"], 'SE23': humidity_profiles["Alpine_Boreal"],
        'SE31': humidity_profiles["Alpine_Boreal"], 'SE32': humidity_profiles["Alpine_Boreal"],

        # Transitional / Sub-Mediterranean
        'FRJ2': humidity_profiles["Sub_Mediterranean"], # Midi-Pyrénées
        'FRK2': humidity_profiles["Sub_Mediterranean"], # Rhône-Alpes
        'FRK1': humidity_profiles["Sub_Mediterranean"], # Auvergne
        'FRI2': humidity_profiles["Sub_Mediterranean"], # Limousin
        'ITC1': humidity_profiles["Sub_Mediterranean"], # Piemonte
        'ITI2': humidity_profiles["Sub_Mediterranean"], # Umbria
        'ITF2': humidity_profiles["Sub_Mediterranean"], # Molise
        'ITF1': humidity_profiles["Sub_Mediterranean"], # Abruzzo

        # Humid Adriatic / Northern Italy Coastal
        'ITH3': humidity_profiles["Humid_Subtropical_Adriatic"], # Veneto
        'ITH4': humidity_profiles["Humid_Subtropical_Adriatic"], # Friuli-Venezia Giulia
    }

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    region_to_profile = {
        # --- SPAIN (ES) ---
        'ES64': humidity_profiles["Mediterranean_Coast"],       # Ciudad de Melilla
        'ES63': humidity_profiles["Mediterranean_Coast"],       # Ciudad de Ceuta
        'ES61': humidity_profiles["Arid_Continental_South"],    # Andalucía
        'ES62': humidity_profiles["Arid_Continental_South"],    # Región de Murcia
        'ES43': humidity_profiles["Arid_Continental_South"],    # Extremadura
        'ES42': humidity_profiles["Arid_Continental_South"],    # Castilla-La Mancha
        'ES30': humidity_profiles["Arid_Continental_South"],    # Comunidad de Madrid
        'ES41': humidity_profiles["Arid_Continental_South"],    # Castilla y León
        'ES23': humidity_profiles["Continental_Standard"],      # La Rioja
        'ES22': humidity_profiles["Continental_Standard"],      # Comunidad Foral de Navarra
        'ES11': humidity_profiles["Hyper_Oceanic"],             # Galicia
        'ES52': humidity_profiles["Mediterranean_Coast"],       # Comunitat Valenciana
        'ES53': humidity_profiles["Mediterranean_Coast"],       # Illes Balears
        'ES24': humidity_profiles["Arid_Continental_South"],    # Aragón
        'ES51': humidity_profiles["Mediterranean_Coast"],       # Cataluña
        'ES21': humidity_profiles["Temperate_Maritime"],        # País Vasco
        'ES13': humidity_profiles["Hyper_Oceanic"],             # Cantabria
        'ES12': humidity_profiles["Hyper_Oceanic"],             # Principado de Asturias

        # --- FRANCE (FR) ---
        'FRJ1': humidity_profiles["Mediterranean_Coast"],       # Languedoc-Roussillon
        'FRJ2': humidity_profiles["Sub_Mediterranean"],         # Midi-Pyrénées
        'FRL0': humidity_profiles["Mediterranean_Coast"],       # PACA
        'FRI1': humidity_profiles["Temperate_Maritime"],        # Aquitaine
        'FRK2': humidity_profiles["Sub_Mediterranean"],         # Rhône-Alpes
        'FRI2': humidity_profiles["Sub_Mediterranean"],         # Limousin
        'FRM0': humidity_profiles["Mediterranean_Coast"],       # Corse
        'FRK1': humidity_profiles["Sub_Mediterranean"],         # Auvergne
        'FRI3': humidity_profiles["Temperate_Maritime"],        # Poitou-Charentes
        'FRC1': humidity_profiles["Continental_Standard"],      # Bourgogne
        'FRG0': humidity_profiles["Temperate_Maritime"],        # Pays de la Loire
        'FRB0': humidity_profiles["Continental_Standard"],      # Centre — Val de Loire
        'FR10': humidity_profiles["Continental_Standard"],      # Ile-de-France
        'FRF2': humidity_profiles["Continental_Standard"],      # Champagne-Ardenne
        'FRD1': humidity_profiles["Temperate_Maritime"],        # Basse-Normandie
        'FRD2': humidity_profiles["Temperate_Maritime"],        # Haute-Normandie
        'FRE2': humidity_profiles["Temperate_Maritime"],        # Picardie
        'FRH0': humidity_profiles["Hyper_Oceanic"],             # Bretagne
        'FRC2': humidity_profiles["Continental_Standard"],      # Franche-Comté
        'FRF1': humidity_profiles["Continental_Standard"],      # Alsace
        'FRF3': humidity_profiles["Continental_Standard"],      # Lorraine
        'FRE1': humidity_profiles["Temperate_Maritime"],        # Nord-Pas de Calais

        # --- ITALY (IT) ---
        'ITG2': humidity_profiles["Mediterranean_Coast"],       # Sardegna
        'ITC3': humidity_profiles["Mediterranean_Coast"],       # Liguria
        'ITC1': humidity_profiles["Sub_Mediterranean"],         # Piemonte
        'ITC4': humidity_profiles["Continental_Standard"],      # Lombardia
        'ITC2': humidity_profiles["Alpine_Boreal"],             # Valle d’Aosta
        'ITF6': humidity_profiles["Arid_Continental_South"],    # Calabria
        'ITF4': humidity_profiles["Arid_Continental_South"],    # Puglia
        'ITG1': humidity_profiles["Arid_Continental_South"],    # Sicilia
        'ITF5': humidity_profiles["Arid_Continental_South"],    # Basilicata
        'ITF3': humidity_profiles["Mediterranean_Coast"],       # Campania
        'ITF2': humidity_profiles["Sub_Mediterranean"],         # Molise
        'ITI4': humidity_profiles["Mediterranean_Coast"],       # Lazio
        'ITF1': humidity_profiles["Sub_Mediterranean"],         # Abruzzo
        'ITI2': humidity_profiles["Sub_Mediterranean"],         # Umbria
        'ITI3': humidity_profiles["Mediterranean_Coast"],       # Marche
        'ITI1': humidity_profiles["Mediterranean_Coast"],       # Toscana
        'ITH5': humidity_profiles["Continental_Standard"],      # Emilia-Romagna
        'ITH3': humidity_profiles["Humid_Subtropical_Adriatic"],# Veneto
        'ITH2': humidity_profiles["Alpine_Boreal"],             # Trento
        'ITH4': humidity_profiles["Humid_Subtropical_Adriatic"],# Friuli-Venezia Giulia
        'ITH1': humidity_profiles["Alpine_Boreal"],             # Bolzano

        # --- UNITED KINGDOM & IRELAND (UK/IE) ---
        'UKK3': humidity_profiles["Hyper_Oceanic"],             # Cornwall
        'UKK4': humidity_profiles["Temperate_Maritime"],        # Devon
        'UKK2': humidity_profiles["Temperate_Maritime"],        # Dorset and Somerset
        'UKJ3': humidity_profiles["Temperate_Maritime"],        # Hampshire
        'UKK1': humidity_profiles["Temperate_Maritime"],        # Bristol area
        'UKG1': humidity_profiles["Temperate_Maritime"],        # Herefordshire
        'UKJ2': humidity_profiles["Temperate_Maritime"],        # Surrey/Sussex
        'UKJ4': humidity_profiles["Temperate_Maritime"],        # Kent
        'UKI6': humidity_profiles["Temperate_Maritime"],        # Outer London - S
        'UKI3': humidity_profiles["Temperate_Maritime"],        # Inner London - W
        'UKI4': humidity_profiles["Temperate_Maritime"],        # Inner London - E
        'UKI7': humidity_profiles["Temperate_Maritime"],        # Outer London - NW
        'UKI5': humidity_profiles["Temperate_Maritime"],        # Outer London - NE
        'UKJ1': humidity_profiles["Temperate_Maritime"],        # Berkshire/Oxon
        'UKH3': humidity_profiles["Temperate_Maritime"],        # Essex
        'UKH2': humidity_profiles["Temperate_Maritime"],        # Bedfordshire/Herts
        'UKH1': humidity_profiles["Temperate_Maritime"],        # East Anglia
        'UKF2': humidity_profiles["Temperate_Maritime"],        # Leicestershire
        'IE05': humidity_profiles["Hyper_Oceanic"],             # Southern IE
        'UKL2': humidity_profiles["Hyper_Oceanic"],             # East Wales
        'UKL1': humidity_profiles["Hyper_Oceanic"],             # West Wales
        'UKG3': humidity_profiles["Temperate_Maritime"],        # West Midlands
        'UKG2': humidity_profiles["Temperate_Maritime"],        # Shropshire/Staffs
        'UKF1': humidity_profiles["Temperate_Maritime"],        # Derbyshire/Notts
        'UKD6': humidity_profiles["Temperate_Maritime"],        # Cheshire
        'IE06': humidity_profiles["Hyper_Oceanic"],             # Eastern/Midland IE
        'UKE3': humidity_profiles["Temperate_Maritime"],        # South Yorkshire
        'UKD7': humidity_profiles["Temperate_Maritime"],        # Merseyside
        'UKF3': humidity_profiles["Temperate_Maritime"],        # Lincolnshire
        'UKE1': humidity_profiles["Temperate_Maritime"],        # East Yorks
        'UKD3': humidity_profiles["Temperate_Maritime"],        # Greater Manchester
        'UKE4': humidity_profiles["Temperate_Maritime"],        # West Yorkshire
        'UKD4': humidity_profiles["Temperate_Maritime"],        # Lancashire
        'UKE2': humidity_profiles["Temperate_Maritime"],        # North Yorkshire
        'IE04': humidity_profiles["Hyper_Oceanic"],             # Northern/Western IE
        'UKN0': humidity_profiles["Hyper_Oceanic"],             # Northern Ireland
        'UKD1': humidity_profiles["Hyper_Oceanic"],             # Cumbria
        'UKC1': humidity_profiles["Temperate_Maritime"],        # Tees Valley
        'UKC2': humidity_profiles["Temperate_Maritime"],        # Northumberland
        'UKM9': humidity_profiles["Hyper_Oceanic"],             # Southern Scotland
        'UKM8': humidity_profiles["Hyper_Oceanic"],             # West Central Scotland
        'UKM7': humidity_profiles["Hyper_Oceanic"],             # Eastern Scotland
        'UKM5': humidity_profiles["Hyper_Oceanic"],             # NE Scotland
        'UKM6': humidity_profiles["Hyper_Oceanic"],             # Highlands/Islands

        # --- GERMANY (DE) ---
        'DE14': humidity_profiles["Continental_Standard"], 'DE13': humidity_profiles["Continental_Standard"],
        'DE27': humidity_profiles["Continental_Standard"], 'DE12': humidity_profiles["Continental_Standard"],
        'DE11': humidity_profiles["Continental_Standard"], 'DE25': humidity_profiles["Continental_Standard"],
        'DEC0': humidity_profiles["Continental_Standard"], 'DEB3': humidity_profiles["Continental_Standard"],
        'DEB2': humidity_profiles["Continental_Standard"], 'DE71': humidity_profiles["Continental_Standard"],
        'DE26': humidity_profiles["Continental_Standard"], 'DE21': humidity_profiles["Alpine_Boreal"],
        'DE22': humidity_profiles["Continental_Standard"], 'DE23': humidity_profiles["Continental_Standard"],
        'DEB1': humidity_profiles["Continental_Standard"], 'DE72': humidity_profiles["Continental_Standard"],
        'DEA2': humidity_profiles["Continental_Standard"], 'DE73': humidity_profiles["Continental_Standard"],
        'DEA5': humidity_profiles["Continental_Standard"], 'DEA1': humidity_profiles["Continental_Standard"],
        'DEA4': humidity_profiles["Continental_Standard"], 'DEA3': humidity_profiles["Continental_Standard"],
        'DE91': humidity_profiles["Continental_Standard"], 'DE92': humidity_profiles["Continental_Standard"],
        'DE94': humidity_profiles["Continental_Standard"], 'DE93': humidity_profiles["Continental_Standard"],
        'DE50': humidity_profiles["Continental_Standard"], 'DE60': humidity_profiles["Continental_Standard"],
        'DEF0': humidity_profiles["Continental_Standard"], 'DE24': humidity_profiles["Continental_Standard"],
        'DEE0': humidity_profiles["Continental_Standard"], 'DE40': humidity_profiles["Continental_Standard"],
        'DE30': humidity_profiles["Continental_Standard"], 'DE80': humidity_profiles["Continental_Standard"],

        # --- POLAND (PL) ---
        'PL21': humidity_profiles["Continental_Standard"], 'PL82': humidity_profiles["Continental_Standard"],
        'PL22': humidity_profiles["Continental_Standard"], 'PL52': humidity_profiles["Continental_Standard"],
        'PL51': humidity_profiles["Continental_Standard"], 'PL72': humidity_profiles["Continental_Standard"],
        'PL81': humidity_profiles["Continental_Standard"], 'PL71': humidity_profiles["Continental_Standard"],
        'PL92': humidity_profiles["Continental_Standard"], 'PL91': humidity_profiles["Continental_Standard"],
        'PL41': humidity_profiles["Continental_Standard"], 'PL61': humidity_profiles["Continental_Standard"],
        'PL84': humidity_profiles["Continental_Standard"], 'PL62': humidity_profiles["Continental_Standard"],
        'PL63': humidity_profiles["Continental_Standard"], 'PL43': humidity_profiles["Continental_Standard"],
        'PL42': humidity_profiles["Continental_Standard"],

        # --- SWEDEN (SE) ---
        'SE22': humidity_profiles["Alpine_Boreal"], 'SE21': humidity_profiles["Alpine_Boreal"],
        'SE12': humidity_profiles["Alpine_Boreal"], 'SE11': humidity_profiles["Alpine_Boreal"],
        'SE33': humidity_profiles["Alpine_Boreal"], 'SE23': humidity_profiles["Alpine_Boreal"],
        'SE31': humidity_profiles["Alpine_Boreal"], 'SE32': humidity_profiles["Alpine_Boreal"],

        # --- ADDITIONAL GERMAN DISTRICTS (DED) ---
        'DED4': humidity_profiles["Continental_Standard"], # Chemnitz
        'DEG0': humidity_profiles["Continental_Standard"], # Thüringen
        'DED2': humidity_profiles["Continental_Standard"], # Dresden
        'DED5': humidity_profiles["Continental_Standard"], # Leipzig
    }


    data = []

    for nuts_id in nuts_ids:

        rh_list = region_to_humidity.get(nuts_id)

        if rh_list is None:
            rh_list = humidity_profiles["Continental_Standard"]

        for m_idx, month in enumerate(months):
            country_code = nuts_id[:2]

            if country_code in ['ES', 'IT']:
                lat_offset = 15
            elif country_code in ['FR', 'DE']:
                lat_offset = 5
            else:
                lat_offset = 0

            temp = 10 + (15 * np.sin(np.pi * (m_idx - 2) / 10)) + lat_offset

            rh = rh_list[m_idx]

            thi = (1.8 * temp + 32) - (0.55 - 0.0055 * rh) * (1.8 * temp - 26)

            yield_loss = round(max(0, (thi - 68) * 0.4), 2)

            data.append({
                'Region Humidity': rh,
                'NUTS_ID': nuts_id,
                'Month': month,
                'THI': round(thi, 2),
                'Temp': round(temp, 1),
                'Yield_Loss_kg': yield_loss
            })

    df = pd.DataFrame(data)

    fig = px.choropleth(
        df,
        geojson=regions_geojson,
        locations="NUTS_ID",
        featureidkey="properties.id",
        hover_name="NUTS_ID",
        color="THI",
        hover_data={"Yield_Loss_kg": True, "THI": ':.2f'},
        animation_frame="Month",
        scope="europe",
        color_continuous_scale="RdYlGn_r",
        range_color=[40, 90],
        title="European Dairy Heat Stress (THI)"
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(height=600, margin={"r":0,"t":70,"l":0,"b":0})


    return fig


map_of_europe()