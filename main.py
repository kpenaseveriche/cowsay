import sys

def main(args):
	'''
	Prints the drawing of a cow saying anything.
	'''
	message = ' '.join(args)
	line1=(len(message)+2)*"-"
	line2=(len(message)+2)*"_"
	print (
		f' {line2} \n'
		f'< {message} >\n'
		f' {line1} \n'
		f'        \\   ^__^\n'
		f'         \\  (oo)\\_______\n'
		f'            (__)\\       )\\/\\\n'
		f'                ||----w |\n'
		f'                ||     ||\n'
	)


if __name__ == "__main__":
	main(sys.argv[1:])
