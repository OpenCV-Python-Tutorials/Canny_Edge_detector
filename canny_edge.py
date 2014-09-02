import cv2
img_name = raw_input("Enter the filename:")
img = cv2.imread(img_name,0)
def canny_edge_detect_min(minVal):
    edges = cv2.Canny(img,minVal,maxVal)
    cv2.imshow('input',img)
    cv2.imshow('Output',edges)
def canny_edge_detect_max(maxVal):
    edges = cv2.Canny(img,minVal,maxVal)
    cv2.imshow('input',img)
    cv2.imshow('Output',edges)
   
cv2.namedWindow('input',cv2.WINDOW_NORMAL)
maxVal = 200
minVal = 100
cv2.createTrackbar('maxVal:','input',maxVal,255,canny_edge_detect_max)
cv2.createTrackbar('minVal:','input',minVal,255,canny_edge_detect_min)
maxVal = cv2.getTrackbarPos('maxVal:','input')
minVal = cv2.getTrackbarPos('minVal:','input')
canny_edge_detect_min(minVal)
canny_edge_detect_max(maxVal)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
