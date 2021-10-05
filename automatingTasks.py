import cv2 
import dropbox 
import time
import random
startTime = time.time()

def automateTask():
    number = random.randit(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "Pictures" + str(number) + ".jpeg"
        cv2.imwrite(imageName,frame)
        startTime = time.time()
        result = False 
    return imageName
    print("Picture Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFile(imageName):
    accessToken = ""
    file = imageName 
    file_from = file 
    file_to =  "/Pictures/" + imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.writeeMode.overWrite)
        print("Files Uploaded")
def main():
    while(True):
        if((time.time() - startTime) >= 10):
            name = automateTask
            uploadFile(name)
main()