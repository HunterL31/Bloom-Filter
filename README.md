# CS-370
## Introduction to Security

### Bloom Filter
This is a simple bloom filter implemented in Python. It creates two different bloom filters, one with 3 hash functions and one with 5 hash functions and populates their bit arrays using the words in the text file specified by the -d flag. After the bloom filters are generated and populated, the words in the text file specified by the -i flag are each ran through both filters to determine if they are good or bad. The results are stored in the two text files specified by the -o flag.

Usage:
`python main.py -d dictionary.txt -i input.txt -o output3.txt output5.txt`
