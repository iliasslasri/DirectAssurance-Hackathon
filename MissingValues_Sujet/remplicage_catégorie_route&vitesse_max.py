## Pour remplir la colonne vitesse max autorisée


vitesses = accidents[accidents["Catégorie Route"].notnull()][["Catégorie Route", "Vitesse Maximale Autorisée"]].drop_duplicates()
vitesses.dropna(inplace=True)

print(vitesses)

def replacing_function(x):
    if x == "Autoroute":
        return 130
    elif x == "Route Nationale":
        return 100
    elif x == "Route Départementale":
        return 75
    elif x == "Voie Communale":
        return (30+50)/2
    else:
        return x

accidents['Vitesse Maximale Autorisée'].fillna(accidents['Catégorie Route'].apply(replacing_function), inplace=True)

# remplir la colonne catégorie de route à partir de la vitesse max autorisée
def replacing_function2(x):
    if x >= 130:
        return "Autoroute"
    elif x == 100:
        return "Route Nationale"
    elif x == 75:
        return "Route Départementale"
    elif x <= 40:
        return "Voie Communale"
    else:
        return x
    
accidents['Catégorie Route'].fillna(accidents['Vitesse Maximale Autorisée'].apply(replacing_function2), inplace=True)
accidents.info()