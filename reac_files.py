import csv

cross_link_dict = {}
# Open the first text file for reading
with open('TB9Cs2C1_LIGP_cross_links.txt', 'r') as file1:
    # Read the contents of the first file
    file1_content = file1.readlines()

# Process each line of the first file
for line in file1_content:
    # Split the line by spaces
    words = line.split()

    mRNA = words[3]
    start_mRNA = words[4]
    end_mRNA = words[5]

    cross_link_dict[mRNA] = {
        'start_mRNA': start_mRNA,
        'end_mRNA': end_mRNA,
        'feature_mRNA': ''
    }



    # Do something with the split words
    # For example, you can save them to a list or perform any desired operations
for key, values in cross_link_dict.items():
    print(f"Key: {mRNA}")
    print(f"start_mRNA: {values['start_mRNA']}")
    print(f"end_mRNA: {values['end_mRNA']}")
    print()


summery_dict = {}
# Open the second text file for reading
with open('GeneByLocusTag_Summary.txt', 'r') as file2:
    # Read the contents of the second file
    file2_content = file2.readlines()

# Process each line of the second file
for line in file2_content:
    # Split the line by spaces
    words = line.split()
    words = words[::-1]
    #print(words[::-1])
    UTR5_length = words[0]
    UTR3_length = words[1]
    Transcript_Length = words[2]
    mRNA = words[-1]
    if UTR3_length == "N/A":
        UTR3_length = 0

    if UTR5_length == "N/A":
        UTR5_length = 0
    #end_3URT = int(Transcript_Length) - int(UTR3_length)


    summery_dict[mRNA] = {
        'Transcript Length': Transcript_Length,
        '3UTR length': UTR3_length,
        '5UTR length': UTR5_length
    }


for input_id, values in summery_dict.items():
    print(f"Input ID: {mRNA}")
    print(f"Transcript Length: {values['Transcript Length']}")
    print(f"Annotated 3' UTR length: {values['3UTR length']}")
    print(f"Annotated 5' UTR length: {values['5UTR length']}")
    print()


all_data = []


for line in file1_content:
    array_feartures = []
    # Split the line by spaces
    parameters = line.split()
    #print(words)
    sno = parameters[0]
    sno_start = parameters[1]
    sno_end = parameters[2]

    mRNA = parameters[3]
    mRNA_start = int(parameters[4])
    mRNA_end = int(parameters[5])

    array_feartures.append(sno)
    array_feartures.append(sno_start)
    array_feartures.append(sno_end)
    array_feartures.append(mRNA)
    array_feartures.append(mRNA_start)
    array_feartures.append(mRNA_end)
    array_feartures.append("")

    if mRNA in summery_dict:
        UTR3 = int(summery_dict[mRNA]['Transcript Length']) - int(summery_dict[mRNA]['3UTR length'])
        UTR5 = int(summery_dict[mRNA]['5UTR length'])
        if mRNA_end <= UTR5:
            array_feartures[6] = "5UTR"

        elif mRNA_start >= UTR3:
            array_feartures[6] = "3UTR"

        elif mRNA_start >= UTR5 and mRNA_end <= UTR3:
            array_feartures[6] = "CDS"

        else:
            if mRNA_start <= UTR5 and mRNA_end >= UTR5:
                part_5UTR = UTR5 - mRNA_start
                part_CDS1 = mRNA_end - UTR5
                array_feartures[6] = "5UTR/CDS" + " -- " + "{0}/{1}".format(part_5UTR, part_CDS1)
            elif mRNA_start <= UTR3 and mRNA_end >= UTR3:
                part_3UTR = mRNA_end - UTR3
                part_CDS2 = UTR3 - mRNA_start
                array_feartures[6] = "CDS/3UTR" + " -- " +"{0}/{1}".format(part_CDS2, part_3UTR)
    else:
        array_feartures[6] = "Not Found"

    all_data.append(array_feartures)

for line in all_data:
    print(f"mRNA: {line[3]}")
    print(f"start_mRNA: {line[4]}")
    print(f"end_mRNA: {line[5]}")
    print(f"feature_mRNA: {line[6]}")
    print()



# Define the file name
filename = 'output.csv'

# Write the all_data array to a CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_data)
