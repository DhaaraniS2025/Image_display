import cv2

image_path = r"C:\Users\Dhaarani S\Pictures\Report pics\IMG-20250714-WA0010.jpg"
image = cv2.imread(image_path)
if image is not None:
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")