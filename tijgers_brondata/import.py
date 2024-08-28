#!/usr/bin/env python
import MySQLdb
import csv

columns = [
    'ID',
    'T_ID',
    'T_Gen',
    'T_sex',
    'Month',
    'Season',
    'Year',
    'Location',
    'Beat',
    'Prey_code_DV',
    'P_Sp_code',
    'P_species',
    'Age_group',
    'P_Sex_Code',
    'P_Sex',
    'Remarks',
    'reserve_cl',
    'reserve_nm',
    '2km_OF_Village',
    '250_OF_water'
];

conn = MySQLdb.connect( host='localhost', user='root', passwd='root', db='tigers')

incidents = []
locations = {}
species = {}
tigers = {}

sex = {
        '1' : 'male',
        '2' : 'female',
        '3' : 'unknown',
}

seasons = {
    'S' : 'summer',
    'W' : 'winter',
    'R' : 'rainy',
}

with open('DATA_DATA.csv', 'rb') as csvfile:
    tigerdata = csv.reader(csvfile, delimiter=';')
    isFirstLine = False
    for line in tigerdata:
        if not isFirstLine:
            isFirstLine = True
            continue

        incidents.append({
            'id' : line[0],
            'tiger' : line[1],
            'month' : line[4],
            'season' : seasons[line[5]],
            'year' : line[6],
            'location' : line[7],
            'prey_type' : line[9],
            'prey_species' : line[11],
            'prey_age' : line[12],
            'prey_sex' : sex[line[13]],
            'remarks' : line[15],
        })
        
        tigers[line[1]] = {
                'id' : line[1],
                'sex' : sex[line[3]],
                'generation' : line[2]
                }

        locations[line[7].upper()] = True
        species[line[11].upper()] = True

    csvfile.close()

    #for incident in incidents:
        #print incident
    #exit()

    cursor = conn.cursor()
    for tiger  in  tigers:
        cursor.execute("INSERT INTO TIGERS (id, sex, generation) VALUES (%s, %s, %s)", (
                tigers[tiger]['id'],
                tigers[tiger]['sex'],
                tigers[tiger]['generation']))

    for speciesName in species:
        cursor.execute("INSERT INTO species (species) VALUES (%s)", [speciesName])

    for location in locations:
        cursor.execute("INSERT INTO locations (location) VALUES (%s)", [location])

    for incident in incidents:
        cursor.execute("INSERT INTO incidents(id, tiger, month, season, year, location, prey_type, prey_species, prey_age, prey_sex, remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            incident['id'],
            incident['tiger'],
            incident['month'],
            incident['season'],
            incident['year'],
            incident['location'],
            incident['prey_type'],
            incident['prey_species'],
            incident['prey_age'],
            incident['prey_sex'],
            incident['remarks']
        ))




    cursor.close()
    conn.commit()


conn.close()
