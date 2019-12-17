import os
import ips
from shutil import copyfile
from tkinter import *
from tkinter import filedialog

##################
# look at _MEIPASS, if it didn't doesn't exist just use the normal directory.
# literally just exists because of the icon.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

##################
# Patching process
# the main thing
# already made in mind when 0% and 100% versions are a thing.
def patch(version='./routeswap'):
	if not os.path.exists('./vanilla'):
		return 'foldermissing'

	print('Starting patching...')
	# try to create directories,
	for x in ['./patched', './patched/Dispos', './patched/Event']:
		try:
			os.mkdir(x)
		except:
			print('dir already created.')

	# check all files in ips folder to see if they exist in ./vanilla, then patch it
	try:
		for r, d, f in os.walk(version):
			for x in f:
				# create separate variables to not be confusing, then check if the file exists
				originalfile = r.replace(version, './vanilla') + '/' + x.replace('.ips', '')
				with open(originalfile, 'r'):
					print('File exists:', originalfile)

				ipsfile = r + '/' + x
				patchedfile = r.replace(version, './patched') + '/' + x.replace('ips', '')

				# copy file to new folder
				copyfile(originalfile, patchedfile)
				# patch it
				ips.patch(patchedfile, ipsfile)

	except:
		return 'filemissing'

	return 'success'

############
# Guit stuff
# Literally a window with just one button.
############
results = {
	'filemissing': 'A file is missing. Check the vanilla folder and try again.',
	'foldermissing': 'The \'vanilla\' folder is missing. Read the instructions and try again.',
	'success': 'Patch applied succefully!'
}

class verycoolgui:
	def __init__(self, root):
		self.root = root
		self.root.title('FE15 route swap patcher')

		self.text = 'Press the button below to start patching.'
		self.label = Label(self.root, text = self.text)
		self.label.pack()

		self.button = Button(self.root, text='Patch!', command=self.doit, height=2 , width=45)
		self.button.pack()
		self.root.iconbitmap(resource_path('icon.ico'))

	def doit(self):
		self.label['text'] = 'Patching...'
		self.label['text'] = results[patch()]


root = Tk()
gui = verycoolgui(root)
root.mainloop()