import easyocr
import string
import re
from datetime import datetime

now = datetime.now()



def is_valid_indian_license_plate(text):
    # pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    if(text[:2] not in indian_state_license_codes ):
        return None
    if len(text) == 10:
        # return text

        if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
        (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
        (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
        (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
        (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
        (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
        (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
        (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
        (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()) and \
        (text[9] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[9] in dict_char_to_int.keys()) :
       
            return text

    if len(text) == 9:
        # return text

        if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
        (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
        (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
        (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
        (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
        (text[5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
        (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
        (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()) and \
        (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[9] in dict_char_to_int.keys()) :
       
            return text
    if len(text) == 9:
        # return text

        if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
        (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
        (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
        (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
        (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
        (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
        (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[6] in dict_char_to_int.keys()) and \
        (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[7] in dict_char_to_int.keys()) and \
        (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[8] in dict_char_to_int.keys()):
        
       
            return text+'1'

    else:
        return None

reader=easyocr.Reader(['en'],gpu=True)

indian_state_license_codes = [
    'AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JH', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TN', 'TG', 'TR', 'UP', 'UK', 'WB', 'AN', 'CH', 'DN', 'LD', 'DL', 'PY','TS'
]

dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5',
                    'T': '1',
                    'B': '8',
                    'D': '0',
                    'E': '8',
                    'L': '1',
                    'Q': '0',
                    'R': '8',
                    'U': '0',
                    'C': '0'                
                    }



dict_int_to_char = {v:k for k,v in dict_char_to_int.items()}


def get_vehicle(license_plate,vehicle_track_id):
    #write your code here
    x1,y1,x2,y2,score,class_id=license_plate

    for i in range(len(vehicle_track_id)):
        xv1,yv1,xv2,yv2,car_id=vehicle_track_id[i]
        
        if x1>xv1 and y1>yv1 and x2<xv2 and y2<yv2:
            return vehicle_track_id[i]

    return -1,-1,-1,-1,-1

def read_license_plate_text(licenese_plate):
    detections=reader.readtext(licenese_plate)
    text=''
    score=''
    fulltext=''
    for detection in detections:
        bbox,text,score=detection


        text=text.upper().replace(' ','')
        text=text.upper().replace('|','1')
        for i in range(len(text)):
           
            if i in [0,1,4,5] and text[i] in dict_int_to_char.keys():
                text=replaceAt(text,i,dict_int_to_char[text[i]])
            elif i not in [0,1,4,5] and text[i] in dict_char_to_int.keys():
                text=replaceAt(text,i,dict_char_to_int[text[i]])

        fulltext+=text
        
        if(is_valid_indian_license_plate(text)):
            current_time = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Current Time =", current_time)   
            return is_valid_indian_license_plate(fulltext),score,current_time
    # return fulltext,score
    return None,None,None

def replaceAt(text,index=0,replacement=''):
    return f'{text[:index]}{replacement}{text[index+1:]}'

def write_csv(results, output_path):
   
    with open(output_path, 'w') as f:
        f.write('{},{}\n'.format( 'car_id','license_number'))

        for frame_nmr in results.keys():
            for car_id in results[frame_nmr].keys():
                if 'car' in results[frame_nmr][car_id].keys() and \
                   'license_plate' in results[frame_nmr][car_id].keys() and \
                   'text' in results[frame_nmr][car_id]['license_plate'].keys():
                    f.write('{},{}\n'.format(car_id,results[frame_nmr][car_id]['license_plate']['text'],))
        f.close()



import csv

def read_data(file):
    with open(file, mode ='r')as file:
  
        csvFile = csv.reader(file)

        for lines in csvFile:
                print(lines)

