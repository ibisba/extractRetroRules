import sqlite3
import csv
import sys

def main():
    try:
        conn = sqlite3.connect(sys.argv[1])
        c = conn.cursor()
        c.execute('''
            SELECT reactions.mnxr, 
                   chemical_species.mnxm,
                   smarts.smarts_string,
                   ec_reactions.ec_number,
                   rules.diameter,
                   rules.score
            FROM rules 
                LEFT JOIN smarts
                    ON (smarts.id=rules.smarts_id)
                LEFT JOIN reactions
                    ON (reactions.id=rules.reaction_id)
                LEFT JOIN chemical_species
                    ON (chemical_species.id=rules.substrate_id)
                LEFT JOIN ec_reactions
                    ON (ec_reactions.reaction_id=rules.reaction_id)
            WHERE rules.isStereo==0 
                ''')
    except sqlite3.Error as e:
        print('Database error: %s'%e)
    all_rows = c.fetchall()
    all_parsed_row = {}
    for row in all_rows:
        if not row[0]+'_'+row[1]+'_'+str(row[4]) in all_parsed_row:
            all_parsed_row[row[0]+'_'+row[1]+'_'+str(row[4])] = [row[0]+'_'+row[1], 
                                                                row[2], 
                                                                str(row[3]), 
                                                                1, 
                                                                row[4],
                                                                row[5]]
        else:
            all_parsed_row[row[0]+'_'+row[1]+'_'+str(row[4])][2] += ';'+str(row[3])
    #Here we are making the rule ID from the reaction ID and substrate ID
    with open('allRules.csv', 'w') as csvfile:
        wri = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        wri.writerow(['Rule ID','Rule','EC number','Reaction order','Diameter','Score'])
        for row in all_parsed_row:
            wri.writerow(all_parsed_row[row])

main()
