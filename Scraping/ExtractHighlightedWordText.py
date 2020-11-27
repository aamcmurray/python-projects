import docx
import difflib as dl
import docx2txt as dcx2 
from docx2python import docx2python as dcx2p

# Function to find matches between original text and combined highlighted portions of text.
def matchsubstring(m_gener,n_orig): 
   seqMatch = dl.SequenceMatcher(None,m_gener,n_orig) 
   match = seqMatch.get_matching_blocks()
   value=seqMatch.ratio()
   if len(match)!=0: 
      return match, value
   else: 
      return 

# Function to generate plain text for comparison later
def original(path):
	ot=dcx2.process(path)
	return ot

# adapted code from Shreyas Karnik, (https://gist.github.com/shreyaskarnik/1982168), designed to read highlighted text portions
def highlighted_portions(path): 
	# initialise a list to fill with highlighted portions of text
	listed=[]
	# get the text for finding highlighted portions
	document = docx.Document(path)
	words=document._element.xpath('//w:r')
	# Find highlighted portions
	WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
	tag_rPr = WPML_URI + 'rPr'
	tag_highlight = WPML_URI + 'highlight'
	tag_val = WPML_URI + 'val'
	tag_t = WPML_URI + 't'
	for word in words:
		for rPr in word.findall(tag_rPr):
			high = rPr.findall(tag_highlight)
			for hi in high:
				if hi.get(tag_val) == 'yellow':
					listed.append(word.find(tag_t).text)
	return listed

# displays the plain text 
def print_original_text(ot):
	print('\n','-----------------------','\n','Complete Original Text:','\n','-----------------------')
	print(ot)

# produces a concatenated string, comprised of the list of highlighted portions
def raw_highlighted(listed):
	n=str()
	for i in range(0, len(listed)):
		n+=listed[i]
	return n

# attempts to pull highlighted portions together
def reconstruction(n,ot):
	print('\n','-----------------------','\n','Highlighted portions - Reconstruction:','\n','-----------------------')
	matched, ratio=matchsubstring(n,ot)
	for i in range(0, len(matched)):
		yield (n[(matched[i].a):(matched[i].a+matched[i].size)])

def printed(h):
	for i in range(0, len(h)):
		print(h[i])

path_input='C:/Users/User/Location/Test.docx'
original_text=original(path_input)
portions=highlighted_portions(path_input)
print_original_text(original_text)
new=raw_highlighted(portions)
highlighted=list(reconstruction(new,original_text))
printed(highlighted)
