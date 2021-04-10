#contrast method
# def contrast(self, option):
#		if option == 'UP':
#			gain = 1.25
#		elif option == 'DOWN':
#			gain = 0.8
#		self.image = cv2.addWeighted(self.image, gain, np.zeros(self.image.shape, self.image.dtype), 0, 0)
#		self.updateLabel(self.image)

# Brightness
# def brightness(self, option):
#		if option == 'UP':
#			bias = 20
#		elif option == 'DOWN':
#			bias = -20
#		self.image = cv2.addWeighted(self.image, 1, np.zeros(self.image.shape, self.image.dtype), 0, bias)
#		self.updateLabel(self.image)

# Openning the image
# def openImage(self, filename=None):
#    		if filename is None:	# if the filename was not passed as a parameter
#			try:
#				filename = filedialog.askopenfilename(initialdir='~/Pictures',title='Open image') #, filetypes=(("image files", "*.jpg"),("all files", "*.*")))
#			except(OSError, FileNotFoundError):
#				messagebox.showerror('Error','Unable to find or open file <filename>')
#			except Exception as error:
#				messagebox.showerror('Error','An error occurred: <error>')
#
#		if filename:	# if filename is not an empty string
#			self.image = cv2.imread(filename)
#			self.origImage = self.image.copy()
#			self.updateLabel(self.image)
