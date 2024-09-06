# import cv2
# import face_recognition

# img = cv2.imread("Messi1.webp")
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)[0]

# img2 = cv2.imread("images/Messi.webp")
# rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# result = face_recognition.compare_faces([img_encoding], img_encoding2)
# print("Result: ", result)

# cv2.imshow("Img", img)
# cv2.imshow("Img 2", img2)
# cv2.waitKey(0)

import cv2
import face_recognition
import os

# Define image paths (update these paths as needed)
image_path1 = "/absolute/path/to/Messi1.jpg"
image_path2 = "/absolute/path/to/images/Messi.jpg"

def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: {image_path} not found or failed to load.")
    return img

def get_face_encoding(image):
    if image is None:
        return None
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_encodings = face_recognition.face_encodings(rgb_img)
    if len(img_encodings) == 0:
        print("Error: No faces found in image.")
        return None
    return img_encodings[0]

# Print current working directory and file paths
print("Current working directory:", os.getcwd())
print("Path to image 1:", image_path1)
print("Path to image 2:", image_path2)

# Load and process the first image
img1 = load_image(image_path1)
encoding1 = get_face_encoding(img1)

# Load and process the second image
img2 = load_image(image_path2)
encoding2 = get_face_encoding(img2)

# Compare faces if both encodings are available
if encoding1 is not None and encoding2 is not None:
    result = face_recognition.compare_faces([encoding1], encoding2)
    print("Result: ", result)

    # Display the images
    if img1 is not None:
        cv2.imshow("Img", img1)
    if img2 is not None:
        cv2.imshow("Img 2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
