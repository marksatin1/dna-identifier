README

dna.py verifies whether an unidentified DNA sample (such as one found at a crime scene) matches any individuals whose DNA has been sequenced and recorded in a database. It does this by counting the longest consecutive chain of short tandem repeats (STRs) in the found DNA and comparing it to the longest consecutive chains of those repeats in the DNA of each person in the database.

The module takes 2 arguments: a CSV file modeling the database and a txt file containing a long string of DNA alleles. These arguments must be included in this order. If they are not - or if more or less than two arguments are included on the command line - then the program will throw an error and exit.

The variable 'database' is a list of lists. The first internal list is the name and specific STR headings. Each subsequent internal list is a person's name and the number of repeats in the longest consecutive chain of a particular STR present in that person's DNA.

'STRs' is a list of the STR headings.

'sequence' is a string of the unidentified DNA.

'counts' is a list of the number of STRs present in the longest consecutive chain of each STR. It is initialized to a list of zeros.

The module first records the length of the first STR and checks its alleles against the alleles in the corresponding first x alleles in the DNA sequence. If there is a match a counter is incremented by 1 and the next x alleles are read. If there is not a match then dna.py looks for the STR starting at the very next allele.

For example, if an STR has 5 alleles, then dna.py checks alleles 0-4 of the DNA sequence. If a match occurs, the counter increments by 1 and alleles 5-9 of the sequence are checked. If not match occurs, then alleles 1-5 are checked.

If the current count for this particular STR is longer than any previous counts, then this count is added to the proper index in 'counts'. This process continues until there are no more alleles to check.

Once all counts have been tallied, dna.py checks the counts against each person in the DNA database file. If the first STR count in the sample matches the first STR count of a person in the database a match counter is incremented by 1 and the next STR count is checked. If no match occurs the module moves onto the next person.

If all counts match then the corresponding person's name is printed from the database file to the console. If not matches are found then "No match" is printed.

The directory contains two sample databases and ten sample DNA sequences.

EXPECTED OUTPUTS

Ginny
Ron
Harry
No match
