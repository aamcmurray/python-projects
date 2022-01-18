import string
import pandas as pd

# Script to find the frequency of occurence of words in a file

def strip_punctuations(line):
	for character in string.punctuation:
		line=line.replace(character, "")
	return line

def word_counter(afilepath):
	word_count={}
	with open(afilepath, encoding='utf-8') as fi:
		for line in fi:
			line=strip_punctuations(line)
			words = line.split()
			for word in words:
				word=word.lower()
				if word not in word_count:
					word_count[word]=0
				word_count[word]+=1
	fi.close()
	return word_count

def data_frame(results):
	newlist=[]
	for key, value in results.items():
		newlist.append([key, value])
	df=pd.DataFrame(newlist, columns=['words', 'frequency'])
	return df

def main():
	filepath="path_goes_here/file_to_analyse.txt"
	values=word_counter(filepath)
	df=data_frame(values)
	df.to_csv('path_goes_here/output_file.csv')


if __name__ == "__main__":
	main()
