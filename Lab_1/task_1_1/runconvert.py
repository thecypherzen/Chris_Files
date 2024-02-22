from convertupper import capitalise

capitalise('declaration.txt')

# open reversed file and reshuffle
with open("encrypted_declaration.txt", 'r+') as revfile:
	content = revfile.read()

	## reverse content using reverse() mthd
	content = list(content)
	content.reverse()
	content.append('\n')
	content = "".join(content)

	## translate content with translate() mthd
	trans_table = content.maketrans("AEIOUDSTK", "%^yZpx&B$")
	content = content.translate(trans_table)

	## write encrypted string to file
	revfile.seek(0)
	revfile.write(content)
