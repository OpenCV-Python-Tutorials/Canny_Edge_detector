import cv2

# Load a file within the same directory
img_name = raw_input("Enter the filename:")
img = cv2.imread(img_name,0)

# function to adjust the minVal
def canny_edge_detect_min(minVal):
    edges = cv2.Canny(img,minVal,maxVal)
    cv2.imshow('input',img)
    cv2.imshow('Output',edges)

# function to adjust the maxVal
def canny_edge_detect_max(maxVal):
    edges = cv2.Canny(img,minVal,maxVal)
    cv2.imshow('input',img)
    cv2.imshow('Output',edges)
   
# Creates a window with trackbars and input image
cv2.namedWindow('input',cv2.WINDOW_NORMAL)

# Set the initial trackbar position
maxVal = 200
minVal = 100

# Create trackbars in the image window
cv2.createTrackbar('maxVal:','input',maxVal,255,canny_edge_detect_max)
cv2.createTrackbar('minVal:','input',minVal,255,canny_edge_detect_min)

# Get trackbar values and pass it to the adjustment functions
maxVal = cv2.getTrackbarPos('maxVal:','input')
minVal = cv2.getTrackbarPos('minVal:','input')
canny_edge_detect_min(minVal)
canny_edge_detect_max(maxVal)

#Wait for ESC key
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
