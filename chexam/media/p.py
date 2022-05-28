from pdf2image import convert_from_path
import pytesseract
import  cv2
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def convertPDFToImg(pdfLoc):
    images = convert_from_path(pdfLoc)
    for i in range(len(images)):
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
def extractKey(data:str):
    key = ""
    for line in data.splitlines():
        line.replace(' ','')
        line = line.lower()
        if 'matricule' in line:
            i = line.index('matricule')+len('matricule')
            while i<len(line):
                start = True
                if line[i].isnumeric():
                    key+=line[i]
                    i+=1
                    start = False
                else:
                    if not start:
                        return int(key)
                    else:
                        i+=1
            return int(key)
def extractDetails(data):
    print(data.splitlines(True))
    dets = {"nom":"","prenom":"","groupe":""}
    for li in data.splitlines(True):
        line = li.lower()[:-1]
        print(line)
        for word in dets.keys():

            if word in line :
                i = line.index(word) + len(word)+1
                start = True
                while i < len(line):
                    if not line[i].isalpha():
                        if not start:
                            break
                        i+=1
                    else:
                        dets[word]+=line[i]
                        i+=1
                        start = False
            if word=="groupe" and dets["groupe"] !="":
                return dets
            print('s')
def treatImg(imgLoc):

    img = cv2.imread(imgLoc)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    hImg, wImg,r = img.shape

    data = pytesseract.image_to_string(img)
    print(data)
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b= b.split(" ")
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
        cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

    print(extractKey(data))
    print(extractDetails(data))
    cv2.imshow('Image',img)
    cv2.waitKey(0)

#convertPDFToImg('Tkejd.pdf')
treatImg("capture.png")