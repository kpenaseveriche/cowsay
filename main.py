import sys

def main(args):
	'''
	Prints the drawing of a cow saying anything.
	'''
	message = ' '.join(args)
	print (
		f' ___________\n'
		f'< {message} >\n'
		f' -----------\n'
		f'        \\   ^__^\n'
		f'         \\  (oo)\\_______\n'
		f'            (__)\\       )\\/\\\n'
		f'                ||----w |\n'
		f'                ||     ||\n'
	)


if __name__ == "__main__":
	main(sys.argv[1:])
