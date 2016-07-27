try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
import codecs

def main():
	root = tk.Tk()
	# keep the window from showing
	root.withdraw()
	# read the clipboard
	c = root.clipboard_get()


	with open("data.csv", 'w') as f:
		f.write(codecs.BOM_UTF8)
		f.write(c.encode('utf-8'))

if __name__ == '__main__':
	main()

