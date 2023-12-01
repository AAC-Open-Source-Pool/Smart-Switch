import cv2
import mediapipe as mp
import math
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# Initialize MediaPipe Pose

'''print("cv2", cv2.__version__)
print("mp", mp.__version__)
print("math",math.__version__)
print("time",time.__version__)
print("np",np.__version__)
print("matplotlib",matplotlib._get_version())'''







mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
global box, d
box, d, point_list = [], [], []
global firebaseConfig, firebase, database, data,flag,nat,bat
flag = 0
bat =0
global a1, b1
b1= 0
global end, led1,led2
end = 0
led1 = []
led2 = []
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAz9thDEv7--mATBZYy5KrM-O TriNwEeIQ",
  "authDomain": "smart-switch-bc1db.firebaseapp.com",
  "projectId": "smart-switch-bc1db",
  "databaseURL" : "https://smart-switch-bc1db-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "smart-switch-bc1db.appspot.com",
  "messagingSenderId": "952091589813",
  "appId": "1:952091589813:web:00c5d3bf7d47b391f952fc",
  "measurementId": "G-0XXNK5ECC5"
};

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()
data = {"Led1" : "off", "Led2" : "off"}

database.child("Users").set(data)




global b,a,n
direction_list =[]
n= 0
def draw(d1_x,d1_y,d2_x,d2_y, ):
    colour = (255, 255, 255)
    cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)),colour , 2)

def point(x,y,size):
        count = 0
        global r_x, r_y, r_size
        global direction, direction_1,duration
        direction_1 =0
        r_x, r_y, r_size = x , y, size
        if n==0:
            duration = 0
            prev =0
        else:
            pass
        global mid_point_x,mid_point_y,d1_x,d1_y,d2_x,d2_y
        mid_point_x = x
        mid_point_y= y
        mid_point= (mid_point_x,mid_point_y)
        size = size
        #f (0 < mid_point_x <640 and 0< mid_point_y <360) or (640 < mid_point_x < 1280 and 360< mid_point_y < 720):

        if (1280 - x1 > 0 and mid_point_x - x1 > 0) or (1280 - x1 < 0 and mid_point_x - x1 < 0):#right
            if (720 - y1 > 0 and mid_point_y - y1 < 0) or (720 - y1 < 0 and mid_point_y - y1 > 0):  # up
                #direction =2
                # line is x-y=mid_point_x-mid_point_y
                distance = size * math.sqrt(2)
                # let d1,d2 be diagonals
                # for d1 slope =1

                d1_x = mid_point_x + (distance / math.sqrt(2))
                d1_y = mid_point_y + (distance * (1 / math.sqrt(2)))
                # d1 = (d1_x, d1_y)
                # for d2 slope = 1

                d2_x = mid_point_x - (distance / math.sqrt(2))
                d2_y = mid_point_y - (distance * (1 / math.sqrt(2)))

                #print(1)
                # d2 = (d2_x, d2_y)
                # cv2.rectangle(frame, (int(d1_x),int(d1_y)), (int(d2_x),int(d2_y)), (255, 255, 255), 2)
            # if (640 < mid_point_x <1200 and 0< mid_point_y <360) or (0 < mid_point_x <640 and 360< mid_point_y <720):
            else:#down
                #direction =4
                # line is -x-y=mid_point_x-mid_point_y
                distance = size * math.sqrt(2)
                # let d1,d2 be diagonals
                # for d1 slope =-1

                d1_x = mid_point_x - (distance / math.sqrt(2))
                d1_y = mid_point_y + (distance * (1 / math.sqrt(2)))
                # d1 = (d1_x, d1_y)
                # for d2 slope = -1

                d2_x = mid_point_x + (distance / math.sqrt(2))
                d2_y = mid_point_y - (distance * (1) / math.sqrt(2))

        #if (640 < mid_point_x <1200 and 0< mid_point_y <360) or (0 < mid_point_x <640 and 360< mid_point_y <720):
        if (1280- x1 >0 and mid_point_x- x1<0) or (1280- x1 <0 and mid_point_x- x1>0 ) :#left
            if (720 - y1> 0 and mid_point_y - y1<0 ) or (720 - y1< 0 and mid_point_y - y1>0 ):# up
                #direction =1
                # line is -x-y=mid_point_x-mid_point_y
                distance = size * math.sqrt(2)
                # let d1,d2 be diagonals
                # for d1 slope =-1

                d1_x = mid_point_x - (distance / math.sqrt(2))
                d1_y = mid_point_y + (distance * (1 / math.sqrt(2)))
                # d1 = (d1_x, d1_y)
                # for d2 slope = -1

                d2_x = mid_point_x + (distance / math.sqrt(2))
                d2_y = mid_point_y - (distance * (1) / math.sqrt(2))
                #print(2)
            else:#down
                #direction =3
                # line is x-y=mid_point_x-mid_point_y
                distance = size * math.sqrt(2)
                # let d1,d2 be diagonals
                # for d1 slope =1

                d1_x = mid_point_x + (distance / math.sqrt(2))
                d1_y = mid_point_y + (distance * (1 / math.sqrt(2)))
                # d1 = (d1_x, d1_y)
                # for d2 slope = 1

                d2_x = mid_point_x - (distance / math.sqrt(2))
                d2_y = mid_point_y - (distance * (1 / math.sqrt(2)))
                #print(

#this is for box
        if (1280- x1 >0 and mid_point_x- x1<0) or (1280- x1 <0 and mid_point_x- x1>0 ): #left
            if (720 - y1> 0 and mid_point_y - y1<0 ) or (720 - y1< 0 and mid_point_y - y1>0 ):# up
                end=0
                if  math.atan2((d2_y - y1), (d2_x - x1))>rad > math.atan2((d1_y - y1), (d1_x - x1)):
                    direction_1 = 10
                    direction_list.append(direction_1)
                    start = time.time()
                    led1.append("yes")

                    if len(led1) == 1:

                        if(data["Led1"] == "off"):
                            print("Led1: on")
                            data["Led1"] = "on"
                            database.child("Users").update({"Led1" : "on"})
                        elif (data["Led1"] == "on"):
                            print("Led1: off")
                            data["Led1"] = "off"
                            database.child("Users").update({"Led1": "off"})
                   # cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)), (255, 255, 255), 2)
                    box.append(((d1_x + d2_x) // 2, (d1_y + d2_y) // 2))
                else:
                    led1.clear()
                    box.clear()
                    direction_1 =0
                    direction_list.clear()
                    duration =0
                    #print("NO")


            else:#down
                if math.atan2((d1_y - y1), (d1_x - x1)) < rad < math.atan2((d2_y - y1), (d2_x - x1)):
                   # cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)), (255, 255, 255), 2)
                    direction_1 = 10
                    direction_list.append(direction_1)
                    #print("yes")
                    box.append(((d1_x + d2_x) // 2, (d1_y + d2_y) // 2))

                else:
                    box.clear()
                    direction_1 =0
                    direction_list.clear()
                    duration =0
                    #print("NO")
        #if (640 < mid_point_x <1200 and 0< mid_point_y <360):
        if (1280 - x1 > 0 and mid_point_x - x1 > 0) or (1280 - x1 < 0 and mid_point_x - x1 < 0):#right
            if (720 - y1> 0 and mid_point_y - y1<0 ) or (720 - y1< 0 and mid_point_y - y1>0 ):# up
                if math.atan2((d1_y - y1), (d1_x - x1))> rad > math.atan2((d2_y - y1), (d2_x - x1)):
                    direction = 10
                    direction_list.append(direction_1)
                    #print("yes")
                    #cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)), (255, 255, 255), 2)
                    box.append(((d1_x + d2_x) // 2, (d1_y + d2_y) // 2))
                    led2.append("yes")
                    if len(led2) == 1:

                        if(data["Led2"] == "off"):
                            print("Led2: on")
                            data["Led2"] = "on"
                            database.child("Users").update({"Led2" : "on"})


                        elif(data["Led2"] == "on"):
                            print("Led2: off")
                            data["Led2"] = "off"
                            database.child("Users").update({"Led2": "off"})
                else:
                    led2.clear()
                    box.clear()
                    direction_1 =0
                    direction_list.clear()
                    duration =0
                    #print("NO")
            else:#down
                if  math.atan2((d2_y - y1), (d2_x - x1))<rad < math.atan2((d1_y - y1), (d1_x - x1)):
                    direction_1 = 10
                    direction_list.append(direction_1)
                    #print("yes")
                    #cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)), (255, 255, 255), 2)
                    box.append(((d1_x + d2_x) // 2, (d1_y + d2_y) // 2))

                else:

                    box.clear()
                    direction_1 =0
                    direction_list.clear()
                    duration =0
                    #print("NO")
        #else:
            #for i,j in range(len(box)):

        cv2.line(frame, (x1,y1), (int(d1_x),int(d1_y)), line_color, line_thickness)
        cv2.line(frame, (x1,y1), (int(d2_x),int(d2_y)), line_color, line_thickness)

        direction_list.append(direction_1)
        #print(count)
        if len(box) == 2:
            if duration >= 0:
                cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)), (255, 255, 255), 2)
            else:
                cv2.rectangle(frame, (int(d1_x), int(d1_y)), (int(d2_x), int(d2_y)), (0, 255, 255), 2)
        return direction_1

def slope(x1,y1,x2,y2):
    res = math.atan2((y2-y1),(x2-x1))
    return res
def covert(x):
    res = x*180/math.pi
    return res
prev_1 = 0
prev_2 = 0
while True:
    a= time.time()
    # Read frame from webcam
    ret, frame = cap.read()

    # Flip the frame horizontally for a mirror-like view
    frame = cv2.flip(frame, 1)

    # Convert the frame color space from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform pose estimation
    results = pose.process(frame_rgb)
    landmarks = results.pose_landmarks

    if landmarks is not None:

        # Get the coordinates of the left elbow and left wrist landmarks
        left_elbow = landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW]
        left_wrist = landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]

        # Calculate the coordinates in pixels
        image_height, image_width, _ = frame.shape
        left_elbow_x = int(left_elbow.x * image_width)
        left_elbow_y = int(left_elbow.y * image_height)
        left_wrist_x = int(left_wrist.x * image_width)
        left_wrist_y = int(left_wrist.y * image_height)

        # Draw a line connecting the left elbow and left wrist landmarks
        line_color = (0, 255, 0)  # Green color (in BGR format)
        line_thickness = 2

        if left_elbow or left_wrist is not None:
            x1, y1 = (left_elbow_x, left_elbow_y)
            x2, y2 = (left_wrist_x, left_wrist_y)
            frame_with_line = cv2.line(frame, (x1,y1), (x2,y2), line_color, line_thickness)
        else:
            x1, y1 = (0,0)
            x2, y2 = (0,100)
            frame_with_line= cv2.line(frame,(0,0),(0,100),line_color,line_thickness)
        rad = math.atan2(y2 - y1, x2 - x1)
        left_elbow = landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_shoulder_x = int(left_elbow.x * image_width)
        left_shoulder_y = int(left_elbow.y * image_height)
        xa, ya = (left_shoulder_x, left_shoulder_y)
        x3,y3 =700, 379
        x4,y4 =600,532
        #print(rad,math.atan2((y3 - ya), (x3 - xa)),math.atan2((y4 - ya), (x4 - xa)))

        pos_x_axis = cv2.line(frame, (x1,y1), (1280,y1), line_color, line_thickness)
        neg_x_axis = cv2.line(frame, (x1,y1), (0,y1), line_color, line_thickness)

        pos_y_axis = cv2.line(frame, (x1,y1), (x1,0), line_color, line_thickness)
        neg_y_axis = cv2.line(frame, (x1,y1), (x1,720), line_color, line_thickness)
        angle = -(math.atan((rad+slope(x1,y1,1280,y1))/(1-(rad*slope(x1,y1,1280,y1)))))
        #print(math.degrees(angle))
        point(240,300,40)#change values here(x,y,size)
        point(1200,300,40)
        '''direction_list[0]=  point(640,360,40)
        direction_list[1]=  point(700,300,40)'''

        #print(d1_x,d1_y,d2_x,d2_y)
        direction = point(1200,300,40)
        #direction =  point(r_x,r_y,r_size)
        b1 = time.time()
        difference = b1 - a
        prev =0
        if direction == prev:
            duration += difference
        else:
            duration = 0
        prev = direction
 
        direction_2 = point(240,300,40)
        #direction =  point(r_x,r_y,r_size)
        b2 = time.time()
        difference_2 = b2 - a
        if direction_2 == prev_2:
            duration += difference_2
        else:
            duration = 0
        prev_2 = direction_2



        '''print("hi")
        print(duration)
        print(direction)
        print(prev)
        print(len(box))'''




        #print("led 1 is off")

    # Display the frame with the line
    #print((640 - x1 > 0 and mid_point_x - x1 > 0))


    cv2.imshow("Pose Detection", frame)
    n= n+1

    if cv2.waitKey(1) & 0xFF == 27:
        break
n= n+1
#print(n)

# Release the webcam and close windows
#plt.imshow(frame)
#plt.show()
cap.release()
cv2.destroyAllWindows()