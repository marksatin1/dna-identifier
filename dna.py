## DNA Identifier ##
import csv, sys

if len(sys.argv) != 3:
  sys.exit("dna.py requires two arguments to run")

if (sys.argv[1].endswith('.txt')):
  sys.exit("Must include a database CSV as first argument")

if (sys.argv[2].endswith('csv')):
  sys.exit("Must include a text file as second argument")

database = []
with open(sys.argv[1]) as db_file:
  reader = csv.reader(db_file)
  for row in reader:
    database.append(row)

STRs = []
for str_type in database[0][1:]:
  STRs.append(str_type)

with open(sys.argv[2]) as dna_file:
  sequence = dna_file.read()

# Determine the longest consecutive chain
# of each STR in the DNA sample
counts = [0]*(len(STRs))
counter = 0
for i in range(len(STRs)):
  str_length = len(STRs[i])
  for j in range(len(sequence)):
    while j <= len(sequence) - str_length:
      substring = sequence[j: j + str_length]
      if substring == STRs[i]:
        counter += 1
        j += str_length
      else:
        if counter > counts[i]:
          counts[i] = counter
        counter = 0
        j += 1
        break

# Match STRs counts to each person in database
match = 0
del database[0]
for row in database:
  for i in range(len(counts)):
    if int(row[i + 1]) == counts[i]:
      match += 1
      if match == len(counts):
        print(row[0])
        sys.exit(0)
    else:
      match = 0
      break
sys.exit("No match")