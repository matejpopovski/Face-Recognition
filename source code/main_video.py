# import cv2
# from simple_facerec import SimpleFacerec

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(2)


# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

# import cv2
# from simple_facerec import SimpleFacerec

# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(0)  # Try index 0 if 2 doesn't work

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Failed to capture image.")
#         continue

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

#     cv2.imshow("Frame", frame)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
try:
    sfr.load_encoding_images("images/")
    print("Encoding images loaded successfully.")
except Exception as e:
    print(f"Error loading encoding images: {e}")

# Load Camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera, change if necessary

if not cap.isOpened():
    print("Error: Camera could not be opened.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        continue

    # Detect Faces
    try:
        face_locations, face_names = sfr.detect_known_faces(frame)
    except Exception as e:
        print(f"Error during face detection: {e}")
        continue

    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
