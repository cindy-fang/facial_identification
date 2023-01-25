import cv2
import sys
import os

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(70, 70),
    flags = cv2.CASCADE_SCALE_IMAGE
)

# Create a dictionary for saving every rectangle coordinates
rect_arr = {"x": [], "y": [], "w": [], "h": []}
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    #print("x",x, "y", y, "w", w, "h",h)
    rect_arr["x"].append(x)
    rect_arr["y"].append(y)
    rect_arr["w"].append(w)
    rect_arr["h"].append(h)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 300, 0), 1)

# Show found faces
cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Found {0} faces!".format(len(faces)))

# Create cropped images of every found faces and save to directory
# Set args variable to save image path to every cropped image/face
args = ""
for i in range(len(faces)):
    x1 = (rect_arr["x"][i])
    y1 = (rect_arr["y"][i])
    x2 = (rect_arr["x"][i]) + (rect_arr["w"][i])
    y2= (rect_arr["y"][i]) + (rect_arr["h"][i])
    crop_image = image[y1:y2, x1:x2]
    cv2.imshow("cropped" + str(i), crop_image)
    cv2.imwrite("cropped"+str(i)+".jpg", crop_image)
    args += "/Users/as/OneDrive/Documents/project/face_detector/cropped"+str(i)+".jpg "
    cv2.waitKey(0)

# Run celeb_recognition file, passing all found faces as arguments to be identified 
os.chdir("/Users/as/OneDrive/Documents/project/celeb_recognition")
os.system("python celeb_recognition.py " + args)

# Optional: run face_search file to google image search the original picture 
#os.system("python face_search.py " + imagePath) 