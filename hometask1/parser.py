
import sys
import json
import re

from datetime import datetime, timedelta

date_format = re.compile(('^(\d{4}(\-)(0[1-9]|1[0-2])(\-)(0[1-9]|1[0-9]|2[0-9]|3[0-1]))$'), re.IGNORECASE)

def getJsonFile(path):
    with open(path) as jfile:
        jsonFile = json.load(jfile)
        return jsonFile

def getDataFromJsonFileFirstLevel (jfile, data):
    print data + ": " + jfile[data]

def getDataFromJsonFileSecondLevel(jfile, data1, data2):
    print data1 + ": " + jfile[data1][data2]


if __name__ == '__main__':
    filepath = sys.argv[1]

    jsonFile = getJsonFile(filepath)

    getDataFromJsonFileFirstLevel(jsonFile, 'DATE_FROM')
    getDataFromJsonFileFirstLevel(jsonFile, 'DATE_TO')
    getDataFromJsonFileSecondLevel(jsonFile, 'STATION', 'STATION_CALL_LETTERS')
    getDataFromJsonFileSecondLevel(jsonFile, 'STATION', 'STATION_NAME')

    print


    for i in [1,2]:
        date = raw_input("Please, enter the data in form yyyy-mm-dd: ")
        if not re.match(date_format, date):
            print "You entered date in incorrect format"
            continue
        else:
            modified_date = datetime.strptime(date, "%Y-%m-%d")
            dayAfter = (modified_date + timedelta(days=1)).date()
            dayBefore = (modified_date + timedelta(days=-1)).date()

            for dat in [dayBefore,modified_date.date(),dayAfter]:
                count=0
                for item in jsonFile["ITEMS"]:
                    if item["IMPRESSION_DATE"]== str(dat):
                        count = count + item["HH"]
                print str(dat) + ": " + str(count)

            break