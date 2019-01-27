import cv2
import sqlite3
import smtplib


#cascade classifier objects

face_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_nose.xml')
mouth_cascade = cv2.CascadeClassifier('./classifiers/haarcascade_mouth.xml')
cam = cv2.VideoCapture(0)  # video capture object


def insertOrUpdate (Id, Name, Post, Faculty, emailId):
    connection = sqlite3.connect('faceBase.db')
    cmd = 'SELECT * FROM peopleInfo WHERE ID=' + str(Id)
    cursor = connection.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd = "UPDATE peopleInfo SET Name="+str(Name)+"WHERE Id="+(Id)
        cmd2 = "UPDATE peopleInfo SET Post=" + str(Post) + "WHERE ID=" + (Id)
        cmd3 = "UPDATE peopleInfo SET Faculty=" + str(Faculty) + "WHERE ID=" + (Id)
        cmd4 = "UPDATE peopleInfo SET emailId=" + str(emailId) + "WHERE ID=" + (Id)
    else:
        cmd = "INSERT INTO peopleInfo(Id,Name,Post,Faculty,emailId) Values ("+str(Id)+","+str(Name)+","+str(Post)+","+str(Faculty)+","+str(emailId)+")"
        cmd2 = ""
        cmd3 = ""
        cmd4 = ""
    connection.execute(cmd)
    connection.execute(cmd2)
    connection.execute(cmd3)
    connection.execute(cmd4)
    connection.commit()
    connection.close()


# EMAIL
def email():
    content = "YOU HAVE BEEN SUCCESSFULLY AUTHORIZED WITHIN THE PERIMETER!!!!"
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('beshreejit@gmail.com', 'project3455')
    mail.sendmail('donotreply@gmail.com', Email, content)
    mail.close()


Id = input('Enter user id: ')
Name = input('Enter the name: ')
Post = input('Enter the post: ')
Faculty = input('Enter the faculty: ')
Email = input('Enter the email: ')
insertOrUpdate(Id, Name, Post, Faculty, Email)
email()


sampleNum = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User."+str(Id)+"."+str(sampleNum)+".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (84, 255, 205), 2)
        cv2.waitKey(1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 0), 2)
        nose = nose_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in nose:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        mouth = mouth_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in mouth:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('DATA SET GENERATOR', img)

    # k = cv2.waitKey(1) & 0xFF
    # if k == 27:
    #     break
    #
    # if(sampleNum >= 20):
    #     break

    # wait for 100 milliseconds
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break if the sample number is more than 20
    elif sampleNum > 20:
        break

cam.release()
cv2.destroyAllWindows()
