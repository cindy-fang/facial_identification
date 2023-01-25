import os
import sys
from os.path import expanduser
from PIL import Image
import requests
import cv2
import numpy as np
from IPython.display import display
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

home = expanduser("~")
celeb_ann_destination = os.path.join(home,'/Users/as/OneDrive/Documents/project/celeb_recognition/celeb_index.ann')
celeb_mapping_destination = os.path.join(home,'/Users/as/OneDrive/Documents/project/celeb_recognition/celeb_mapping.json')

# provide path to image for prediction (url)
#url = 'https://6.viki.io/image/755126efed4042a9900fdc8d788ff9a6/dummy.jpeg?s=900x600&e=t' # provide image url here
#img = cv2.cvtColor(np.array(Image.open(requests.get(url, stream=True).raw)), cv2.COLOR_BGR2RGB)

from celeb_utils.celeb_utils import get_celeb_prediction
def celeb_predict(img):
	pred, img = get_celeb_prediction(img)
	if pred is not None:
		os.makedirs('celeb_output', exist_ok=True)
		out_im_path = 'celeb_output/image_output.jpg'
		cv2.imwrite(out_im_path, img)
		print("Output image saved at {}".format(out_im_path))
		print("Found celebrities:")
		for c in pred:
			if c["celeb_name"].lower() !="unknown":
				print(c["celeb_name"])
				celeb = c["celeb_name"]
		print("\nOverall output:\n",pred)
	else:
		print("No faces detected in the image")

#accepting multiple pictures (faces) from face_detect
for i in range(1,len(sys.argv)):
	print(sys.argv[i])
	picture = cv2.cvtColor(np.array(Image.open(sys.argv[i])), cv2.COLOR_BGR2RGB)
	celeb_predict(picture)
	im = cv2.imread(sys.argv[i])
	cv2.imshow("found celeb", im)
	cv2.waitKey(0)
