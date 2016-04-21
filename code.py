import cv2
import numpy as np

included_extensions = ['bmp']
filelist = [fn[:-9] for fn in os.listdir(xdirname) if any([fn.endswith(ext) for ext in included_extensions])]

for fname in filelist
	img = cv2.imread(fname)
	imgg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	surf = cv2.SURF()
	kp, descriptors = surf.detect(imgg,None,useProvidedKeypoints = False)

	samples = np.array(descriptors)
	responses = np.arange(len(kp),dtype = np.float32)