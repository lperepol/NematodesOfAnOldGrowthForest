import pandas as pd
#import odfpy
import glob
import os
#import pillow
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def read_ods(fname):
    df= pd.read_excel(fname, engine="odf")
    return df

def get_jpg_files(path):
    my_path = path
    # Get List of all images
    files = glob.glob(my_path + '/**/*.jpg', recursive=True)
    return files

def add_text_to_image(src_image, dest_image, loc, Family,Genus,View):
    # Open an Image
    img = Image.open(src_image)
# Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    # Custom font style and font size
    myFont = ImageFont.truetype('arial.ttf', 65)
    # Add Text to an image
    pos =70
    I1.text((10, pos), loc, font=myFont, fill=(0, 0, 0))
    pos = pos + pos
    I1.text((10, pos), Family, font=myFont, fill=(0, 0, 0))
    pos = pos + pos
    I1.text((10, pos), Genus, font=myFont, fill=(0, 0, 0))
    pos = pos + pos
    I1.text((10, pos), View, font=myFont, fill=(0, 0, 0))
    # Display edited image
    #img.show()
    # Save the edited image
    img.save(dest_image)


def main():
    filelist = [
        "./../../Slide/ogf-0001/Metadata.ods",
        "./../../Slide/ogf-0002/Metadata.ods",
        "./../../Slide/ogf-0003/Metadata.ods",
        "./../../Slide/ogf-0004/Metadata.ods",
        "./../../Slide/ogf-0005/Metadata.ods",
        "./../../Slide/ogf-0006/Metadata.ods",
        "./../../Slide/ogf-0007/Metadata.ods",
        "./../../Slide/ogf-0008/Metadata.ods",
        "./../../Slide/ogf-0009/Metadata.ods",
        "./../../Slide/ogf-0010/Metadata.ods",
        "./../../Slide/ogf-0011/Metadata.ods",
        "./../../Slide/ogf-0012/Metadata.ods",
        "./../../Slide/ogf-0013/Metadata.ods",
        "./../../Slide/ogf-0014/Metadata.ods",
        "./../../Slide/ogf-0015/Metadata.ods",
        "./../../Slide/ogf-0016/Metadata.ods",
        "./../../Slide/ogf-0017/Metadata.ods",
        "./../../Slide/ogf-0018/Metadata.ods",
        "./../../Slide/ogf-0019/Metadata.ods",
        "./../../Slide/ogf-0020/Metadata.ods",
        "./../../Slide/ogf-0021/Metadata.ods"
    ]
    df1 = pd.DataFrame()
    count=1
    for f in filelist:
        df = read_ods(f)
        df["Dir"] = f
        path = str(f).replace('Metadata.ods', '')
        jpg_files = get_jpg_files(path)
        for i, row in df.iterrows():

            #df.at[i, 'ifor'] = ifor_val
            Family = str(row['Family']).strip()
            Genus = str(row['Genus']).strip()
            View = str(row['View']).strip()
            Nem = str(row['Nem']).strip()
            #Nem = str(Nem).strip().replace('Nem_0','Nem_000')
            #Nem = str(Nem).strip().replace('Nem_1','Nem_001')
            Family = str(Family).strip()
            if Family == 'nan':
                Family = 'Unidentified'
            #print(Family)
            path2 = path  + Nem + ''
            jpg_files = get_jpg_files(path2)
            print (jpg_files)
            for j in jpg_files:
                image_loc = str(j).strip().replace('./../../Slide/','')
                src_image = j
                if "100x" not in image_loc:
                    continue
                dest_image = './../../Slide/ogf-0021/ogf_familes/' + Family
                if not os.path.exists(dest_image):
                    os.makedirs(dest_image)
                dest_image = './../../Slide/ogf-0021/ogf_familes/' + Family + '/' + str(count).zfill(5) + '.jpg'

                #src_image = str(j).strip().replace('\\\\', '/')
                add_text_to_image(src_image, dest_image, image_loc, Family,Genus,View)
                x = 1
                count = count +1


        #if df1.empty:
        #    df1 = df
        #else:
        #    df1 = pd.concat([df1, df])

    #df1.to_csv("./../../Slide/AppendedPositionFiles_OGF.csv",index=False )
    return

if __name__ == '__main__':
    directory = './../../Slide/ogf-0021/ogf_familes/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    main()


