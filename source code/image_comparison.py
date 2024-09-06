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

# Load first image
img = cv2.imread("Messi1.jpg")
if img is None:
    print("Error: Messi1.webp not found or failed to load.")
else:
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encodings = face_recognition.face_encodings(rgb_img)
    
    if len(img_encodings) == 0:
        print("Error: No faces found in Messi1.webp.")
    else:
        img_encoding = img_encodings[0]

        # Load second image
        img2 = cv2.imread("images/Messi.jpg")
        if img2 is None:
            print("Error: images/Messi.webp not found or failed to load.")
        else:
            rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            img_encodings2 = face_recognition.face_encodings(rgb_img2)
            
            if len(img_encodings2) == 0:
                print("Error: No faces found in images/Messi.webp.")
            else:
                img_encoding2 = img_encodings2[0]

                # Compare faces
                result = face_recognition.compare_faces([img_encoding], img_encoding2)
                print("Result: ", result)

                # Display the images
                cv2.imshow("Img", img)
                cv2.imshow("Img 2", img2)
                cv2.waitKey(0)
