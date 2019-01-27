import cv2
import sqlite3
import winsound
import smtplib


face_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_nose.xml')
mouth_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_mouth.xml')


def getProfile(id):
    connection = sqlite3.connect('faceBase.db')
    cmd = 'SELECT Id, Name, Post, Faculty, emailId FROM peopleInfo WHERE ID=' + str(id)
    cursor = connection.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    connection.close()
    return profile


def insert(profile):
    conn = sqlite3.connect('faceBase.db')
    conn.execute("INSERT INTO detectionInfo VALUES (?, ?, ?, ?, ?)", profile)
    conn.commit()
    conn.close()


def email():
    content = "Unauthorized person detected!!!!!"
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('beshreejit@gmail.com', 'project3455')
    mail.sendmail('donotreply@gmail.com', 'bshreejit@gmail.com', content)
    mail.close()
    return


sampleNum = 1
a = 1
gId = 1
Id = 0
b = 0
# p = 1
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("trainingData.yml")
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX = 3
fontScale = 0.8
fontColor = (255, 55, 255)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (84, 255, 205), 5)
        Id, conf = rec.predict(gray[y:y + h, x:x + w])
        # If(p == 1)
        print("Conf value:", conf)
            # p   =   p  +  1
        if(conf < 60):
            profile = getProfile(Id)
            if (profile != None):
                cv2.putText(img, "Unique ID:" + str(profile[0]), (x, y + h + 30), font, fontScale,
                            fontColor)  # Draw the Text
                cv2.putText(img, str(profile[1]), (x, y + h + 60), font, fontScale, fontColor)
                cv2.putText(img, str(profile[2]), (x, y + h + 90), font, fontScale, fontColor)
                cv2.putText(img, str(profile[3]), (x, y + h + 120), font, fontScale, fontColor)
                cv2.putText(img, str(profile[4]), (x, y + h + 150), font, fontScale, fontColor)
                cv2.putText(img, "Conf Value:" + str(conf), (x, y + h + 180), font, fontScale, fontColor)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 0), 2)
                nose = nose_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in nose:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (150, 255, 50), 2)
                mouth = mouth_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in mouth:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                if (Id != 0):
                    if(gId == 1):
                        insert(profile)
                        gId = gId + 1

        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)
            font = cv2.FONT_HERSHEY_COMPLEX = 3
            fontScale = 0.8
            fontColor = (0, 0, 0)
            winsound.Beep(1000, 80)
            cv2.putText(img, "UNRECOGNIZABLE", (x, y + h + 30), font, fontScale, fontColor)  # Draw the Text
            cv2.putText(img, "Conf Value:" + str(conf), (x, y + h + 60), font, fontScale, fontColor)
            a = a + 1
            if a > 10:
                b = b + 1
                if a < 12:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                    for (x1, y1, w1, h1) in faces:
                        cv2.imwrite("Unknown/Unknown." + str(sampleNum) + "." + str(b) + ".jpg", gray[y:y + h, x:x + w])
                        cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (84, 255, 205), 2)
                        roi_gray = gray[y:y + h, x:x + w]
                        roi_color = img[y:y + h, x:x + w]
                        #email()

    cv2.imshow('Detector', img)
    cv2.moveWindow('Detector', 400, 85)


    #cv2.resizeWindow('Detector', 700, 500)
    if cv2.waitKey(10) == ord('q'):
        break

cam.release()  #shuts the camera off
cv2.destroyAllWindows()  #dsstroys the window
