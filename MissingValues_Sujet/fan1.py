# define fill in function
def fill_etat_surface(row):
    if pd.notna(row["Conditions Atmosphériques"]):
        return "Sec" if row["Conditions Atmosphériques"] == "Normal" else "Mouillé"
    else:
        pass
    
def fill_condition_atmo(row):
    if pd.notna(row["Etat Surface"]):
        return "Normal" if row["Etat Surface"] == "Sec" else "Pluie"
    else:
        pass
accidents2["Etat Surface"] = accidents2.apply(fill_etat_surface, axis=1)
accidents2["Conditions Atmosphériques"] = accidents2.apply(fill_condition_atmo, axis = 1)