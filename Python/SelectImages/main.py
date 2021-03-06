import pandas as pd
import openpyxl
#import odfpy
import glob
import os
#import pillow
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import csv

def read_ods(fname):
    df= pd.read_excel(fname, engine="odf")
    df = df.fillna('')
    return df

def read_excel(fname):
    df= pd.read_excel(fname, sheet_name='Created_AllImageMetadata')
    df = df.fillna('')
    return df

def get_jpg_files(path):
    my_path = path
    # Get List of all images
    files = glob.glob(my_path + '/**/*.jpg', recursive=True)
    return files

def add_text_to_image(src_image, dest_image, loc, Family,Genus,View,Location_0,Location_1,Location_2):
    # Open an Image
    print (src_image)
    img = Image.open(src_image)
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    # Custom font style and font size
    myFont = ImageFont.truetype('arial.ttf', 40)
    # Add Text to an image
    Inc_pos =70
    pos = 70
    I1.text((10, pos), loc, font=myFont, fill=(0, 0, 0))
    pos = pos + Inc_pos
    I1.text((10, pos), Family, font=myFont, fill=(0, 0, 0))
    if len(Genus) > 3:
        pos = pos + Inc_pos
        I1.text((10, pos), Genus, font=myFont, fill=(0, 0, 0))
    if len(View) > 3:
        pos = pos + Inc_pos
        I1.text((10, pos), View, font=myFont, fill=(0, 0, 0))
    if len(Location_0) > 3:
        pos = pos + Inc_pos
        I1.text((10, pos), Location_0, font=myFont, fill=(0, 0, 0))
    if len(Location_1) > 3:
        pos = pos + Inc_pos
        I1.text((10, pos), Location_1, font=myFont, fill=(0, 0, 0))
    if len(Location_2) > 3:
        pos = pos + Inc_pos
        I1.text((10, pos), Location_2, font=myFont, fill=(0, 0, 0))
    # Display edited image
    #img.show()
    # Save the edited image
    img.save(dest_image)


def main():
    viewSet = {
        "amphid",
        "basal knob",
        "cephalic setae",
        "esophagus",
        "guiding ring",
        "lips",
        "spear",
        "stylet",
        "tooth",
        "anterior"
    }
    fname = "./../../Metadata/ManualEdits/Keep_AllImageMetadata.xlsx"
    df = read_excel(fname)
    nemSet = set()
    for i, row in df.iterrows():
        Slide = str(row['Slide']).strip()
        Nem = str(row['Nem']).strip()
        Family = str(row['Family']).strip()
        View = str(row['View']).strip()
        if len(Family) < 3:
            Family = 'Unidentified'
        element = (Slide,Nem,Family)
        nemSet.add(element)
        Genus = str(row['Genus']).strip()
        View = str(row['View']).strip()
        Nem = str(row['Nem']).strip()
        Moved_Image_Name = str(row['Moved_Image_Name']).strip()
        Src_Image = str(row['Image']).strip()
        rstr = '\\'
        Moved_Image_Name = Src_Image.replace(rstr,'_')
        rstr = r'/'
        Moved_Image_Name = Moved_Image_Name.replace(rstr, '_')
        print ('Moved_Image_Name')
        print (Moved_Image_Name)
        Mag = str(row['Mag']).strip()
        if Mag != '100x':
            continue
        if View not in viewSet:
            continue
        if Family == 'nan':
            Family = 'Unidentified'
        #print(Family)
        src_image = './../../Slide/' + Src_Image
        dest_image = './../../../id_ogf_familes/' + Family
        if not os.path.exists(dest_image):
            os.makedirs(dest_image)
        dest_image = './../../../id_ogf_familes/' + Family + '/' + Moved_Image_Name
        print (dest_image)
        if len(Genus) < 3 :
            Genus = ''
        if len(View) < 3 :
            View = ''
        Location_0 = 'Old-Growth Mixed Conifer Forest'
        Location_1 = 'Southern Central British Columbia, Canada'
        Location_2 = 'West Kootenay Region'
        add_text_to_image(src_image, dest_image, Src_Image, Family,Genus,View, Location_0,Location_1,Location_2)

    famDict = dict()
    for i in nemSet:
        (Slide, Nem_0010, Family) =i
        famDict[Family] =0
    for i in nemSet:
        (Slide, Nem_0010, Family) =i
        famDict[Family] = famDict[Family] + 1
    header = ['Family', 'Count']
    with open('FamilyCount.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in famDict:
            data = [i, famDict[i]]
            writer.writerow(data)



    return

if __name__ == '__main__':
    directory = './../../../id_ogf_familes/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    main()


