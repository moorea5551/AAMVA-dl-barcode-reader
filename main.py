import cv2
import zxingcpp
import numpy as np

def automatic_brightness_and_contrast(image, clip_hist_percent=1):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate grayscale histogram
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)
    
    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))
    
    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0
    
    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1
    
    # Locate right cut
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1
    
    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha
    
    '''
    # Calculate new histogram with desired range and show histogram 
    new_hist = cv2.calcHist([gray],[0],None,[256],[minimum_gray,maximum_gray])
    plt.plot(hist)
    plt.plot(new_hist)
    plt.xlim([0,256])
    plt.show()
    '''

    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return (auto_result, alpha, beta)

img = cv2.imread('IMG_5101.jpg')
cv2.imwrite('result.png', img)
auto_result, alpha, beta = automatic_brightness_and_contrast(img)

# print('alpha', alpha)
# print('beta', beta)
# cv2.imshow('auto_result', auto_result)
# cv2.waitKey()
# cv2.imwrite("result.png", result)
# cv2.imwrite("enhanced.png", enhanced_img)

s = zxingcpp.read_barcodes(auto_result, formats=zxingcpp.BarcodeFormat.PDF417, binarizer=zxingcpp.Binarizer.GlobalHistogram)
print(len(s))
for r in s:
    dlstring = r.text

    dlstringarray = dlstring.split('<LF>')
    dlstringarray = dlstringarray[2:]
    dlstringarray = [line.strip() for line in dlstringarray]

    for field in dlstringarray:

        fieldID = field[0:3]
        fieldValue = field[3:]

        if fieldID == 'DAC':
            print("First Name: ")
            print(fieldValue + "\n")
        elif fieldID == 'DAD':
            print('Middle Name: ')
            print(fieldValue + "\n")
        elif fieldID == 'DCS':
            print('Last Name:')
            print(fieldValue + "\n")
        # elif fieldID == 'DCD':
        #     print('Jurisdiction specific endorsement codes: ')
        # elif fieldID == 'DBA':
        #     print('Document Expiration date: ')
        # elif fieldID == 'DCS':
        #     print('Customer Family Name: ')
        # elif fieldID == 'DCT':
        #     print('Customer Given Name: ')
        # elif fieldID == 'DBD':
        #     print('Document Issue Date: ')
        # elif fieldID == 'DBB':
        #     print('Date of Birth: ')
        # elif fieldID == 'DBC':
        #     print('Sex: ')  # 1 for male, 2 for female
        # elif fieldID == 'DAY':
        #     print('Eye Color: ')
        # elif fieldID == 'DAU':
        #     print('Height: ')
        # elif fieldID == 'DAG':
        #     print('Address Line 1: ')
        # elif fieldID == 'DAI':
        #     print('City: ')
        # elif fieldID == 'DAJ':
        #     print('State: ')
        # elif fieldID == 'DAK':
        #     print('Postal Code: ')
        # elif fieldID == 'DAQ':
        #     print('Customer ID Number: ')
        # elif fieldID == 'DCF':
        #     print('Document Discriminator: ')
        # elif fieldID == 'DCG':
        #     print('Country Identification: ')
        # elif fieldID == 'DCK':
        #     print('Inventory control number: ')