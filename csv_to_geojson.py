import csv

# Read in raw data from csv
with open('filename.csv', newline='') as csvfile:
    rawData = csv.reader(csvfile, delimiter=',')

    # the template. where data from the csv will be formatted to geojson
    template = \
    ''' \
    { 
            "type" : "Feature",
            "properties": {
                "id": %s
            },
            "geometry" : {
                "type" : "LineString",
                "coordinates" : %s
            }
        },
    '''


    # the head of the geojson file
    output = \
    ''' \
    { 
        "type" : "FeatureCollection",
        "features" : [
    '''


    # loop through the csv by row
    iter = 1
    for row in rawData:
        length = len(row)
        cordinates = []
        sample = []
        
        #loop through the csv by row skipping the last two
        for i in  range(0,length-2):
            if(i % 2 != 0):
                sample.append(float(row[i]))
                sample.append(float(row[i+1]))
                cordinates.append(sample)
                sample = []

        output += template % (iter, cordinates)
        iter = iter + 1
        cordinates = []

    output += \
    ''' \
    ]

    }
    '''


# opens an geoJSON file to write the output
outFileHandle = open("filename.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()