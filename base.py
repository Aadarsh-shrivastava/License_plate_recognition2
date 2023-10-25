from ultralytics import YOLO
import cv2
from sort.sort import*

from utils import *


def get_license_plate_data(file):
    results={}
    auto_trackers=Sort()
    #loading models
    objectModel=YOLO('./yolov8n.pt')
    license_plate_detector=YOLO('./license_plate_detector.pt')

    #loading video
    cap=cv2.VideoCapture(file)


    #vehicles list with class Id
    vehicles=[2,3,5,7]

    #reading frames
    frameNumber=-1
    ret= True
    while ret :
        frameNumber+=1
        ret,frame=cap.read()
        
        if ret:# and frameNumber<100:
            results[frameNumber] = {}
            #detect vehicles
            detections=objectModel(frame)[0]
            allVehiclesInFrame=[]
            for detection in detections.boxes.data.tolist():
                x1,y1,x2,y2,score,class_id=detection
                if int(class_id) in vehicles:
                    allVehiclesInFrame.append([x1,y1,x2,y2,score,class_id])
                   
            
            
            #tracking vehicles
            try:
                tracking_id=auto_trackers.update(np.asarray(allVehiclesInFrame))
            except:
                continue
          
            # detect license plate
            license_plates=license_plate_detector(frame)[0]
            for license_plate in license_plates.boxes.data.tolist():
                x1,y1,x2,y2, score,class_id=license_plate
                area_of_the_boundingbox=abs(x1-x2)*abs(y1-y2)
                if(area_of_the_boundingbox<3000):
                    break
                xv1,yv1,xv2,yv2,car_id=get_vehicle(license_plate,tracking_id)
                
                img=frame[int(y1):int(y2),int(x1):int(x2), : ]
                img=cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
                img=cv2.bilateralFilter(img,16,6,6)
                img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                _,img=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
                
            

        
                license_plate_text,license_plate_text_score,reading_time=read_license_plate_text(img)

                if license_plate_text is not None:
                    results[frameNumber][car_id]={'car':{'bbox':[xv1,yv1,xv2,yv2]},
                                                'license_plate':{'bbox':[x1,y1,x2,y2],
                                                                'text':license_plate_text,
                                                                'bbox_score':score,
                                                                'text_score':license_plate_text_score,
                                                                'current_time':reading_time}}




    r={}

    for i in results:
        for key,val in results[i].items():
            if r.get(key) is None or r[key]['text_score']<val['license_plate']['text_score']:
                r[key]=val['license_plate']

    unique_dict={}
    for key, value in r.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    # for i in r:
    #     print(i,'--',r[i]['text'])
    # write_csv(results,'./test.csv')
    return unique_dict