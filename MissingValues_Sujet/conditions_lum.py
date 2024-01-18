accidents['Date'] = pd.to_datetime(accidents['Date'])

accidents["time"] = accidents["Date"].dt.hour 

def remplace_condition_lumineuses(x):
    if 8 <= x <= 17:
        return 'Jour'
    elif 18 <= x <= 23 or 0 <= x < 8:
        return 'Nuit'
    else:
        return None



# Utiliser une lambda function pour remplacer les NaN dans 'conditions_lumineuses'
accidents['Conditions Lumineuses'].fillna(accidents["time"].apply(remplace_condition_lumineuses), inplace=True)

accidents.drop(columns=["time"], inplace=True)

accidents.info()

    