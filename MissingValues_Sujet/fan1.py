accidents2 = accidents.copy()
accidents_normal = accidents2[accidents2["Conditions Atmosphériques"]=="Normal"]
accidents_normal["Etat Surface"] = accidents_normal["Etat Surface"].fillna("Sec")
accidents_pluie = accidents2[accidents2["Conditions Atmosphériques"]=="Pluie"]
accidents_pluie["Etat Surface"] = accidents_pluie["Etat Surface"].fillna("Mouillé")
accidents_nanLeft = accidents2[accidents2["Conditions Atmosphériques"].isna()]
frame1 = [accidents_normal, accidents_pluie, accidents_nanLeft]
accidents_fill_fan = pd.concat(frame1)
accidents_sec = accidents_fill_fan[accidents_fill_fan["Etat Surface"] == "Sec"]
accidents_sec["Conditions Atmosphériques"] = accidents_sec["Conditions Atmosphériques"].fillna("Normal")
accidents_mouille = accidents_fill_fan[accidents_fill_fan["Etat Surface"] == "Mouillé"]
accidents_mouille["Conditions Atmosphériques"] = accidents_mouille["Conditions Atmosphériques"].fillna("Pluie")
frame2 = [accidents_sec, accidents_mouille]
accidents_fill_fan2 = pd.concat(frame2)

