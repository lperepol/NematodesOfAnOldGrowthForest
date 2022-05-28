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

def create_image_dataframe():
    df = pd.DataFrame(
        columns=
        [
        'Dir',
        'Comments',
        'Annotated',
        'Nem',
        'Image',
        'Y',
        'X',
        'Mag',
        'Family',
        'Genus',
        'View',
        'overall body length',
        'distance of vulva from anterior ',
        '% distance of vulva from anterior',
        'stylet or spear length (stomatostyle or odontostyle)',
        '% distance from anterior to median bulb relative to length of esophagus',
        '% distance of anterior phasmid from anterior of nematode in relation to body length',
        '% distance of dorsal esophageal gland opening from stylet knobs in relation to stylet length',
        '% distance of phasmid from anus in relation to length of tail',
        '% distance of posterior phasmid from anterior of nematode in relation to body length',
        '% length of anterior female gonad in relation to body length',
        '% length of male gonad relative to body length',
        '% length of posterior female gonad in relation to body length',
        '(distance of dorsal esophageal gland opening from stylet knobs x 100)/(length of stylet)',
        '(distance of phasmid(when not erratic) from anus x 100)/( length of tail)',
        'body length / distance from anterior to base of esophageal glands',
        'body length / distance from anterior to esophago-intestinal valve',
        'body length / greatest body diameter',
        'body length / tail length',
        'capitulum length in µm',
        'conus of stomatostyle/total stomatosyle length',
        'distance from anterior end to excretory pore in µm',
        'distance from base of stylet to median bulb valve/stylet length.',
        'distance from vulva to anus',
        'gubernaculurn length in µm',
        'number of body annules between anterior and excretory pore',
        'number of body annules between anus and tail tip',
        'number of body annules between vulva and anus',
        'number of body annules between vulva and tail tip',
        'number of specimens on which measurements are based',
        'portion of body from anus or cloaca to posterior terminus',
        'SE/L (measured in same units) expressed as %).',
        'spicule length in µm',
        'stylet extension (odontophore) length in µm',
        'stylet length / body diameter at base of stylet',
        'stylet length/body length (measured in same units as %).',
        'tail length / tail diameter at anus or cloaca',
        'total number of body annules',
        'Flickr URL'
    ]
    )
    return df

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
    create_image_dataframe = create_image_dataframe()
    for f in filelist:
        df = read_ods(f)
        df["Dir"] = f
        path = str(f).replace('Metadata.ods', '')
        jpg_files = get_jpg_files(path)
        for i, row in df.iterrows():
            col_001 = str(row['Dir']).strip()
            col_002 = str(row['Comments']).strip()
            col_003 = str(row['Annotated']).strip()
            col_004 = str(row['Nem']).strip()
            col_005 = str(row['Image']).strip()
            col_006 = str(row['Y']).strip()
            col_007 = str(row['X']).strip()
            col_001 = str(row['Mag']).strip()
            col_009 = str(row['Family']).strip()
            col_010 = str(row['Genus']).strip()
            col_011 = str(row['View']).strip()
            col_012 = str(row['overall body length']).strip()
            col_013 = str(row['distance of vulva from anterior ']).strip()
            col_014 = str(row['% distance of vulva from anterior']).strip()
            col_015 = str(row['stylet or spear length (stomatostyle or odontostyle)']).strip()
            col_016 = str(row['% distance from anterior to median bulb relative to length of esophagus']).strip()
            col_017 = str(row['% distance of anterior phasmid from anterior of nematode in relation to body length']).strip()
            col_018 = str(row['% distance of dorsal esophageal gland opening from stylet knobs in relation to stylet length']).strip()
            col_019 = str(row['% distance of phasmid from anus in relation to length of tail']).strip()
            col_021 = str(row['% distance of posterior phasmid from anterior of nematode in relation to body length']).strip()
            col_022 = str(row['% length of anterior female gonad in relation to body length']).strip()
            col_023 = str(row['% length of male gonad relative to body length']).strip()
            col_024 = str(row['% length of posterior female gonad in relation to body length']).strip()
            col_025 = str(row['(distance of dorsal esophageal gland opening from stylet knobs x 100)/(length of stylet)']).strip()
            col_026 = str(row['(distance of phasmid(when not erratic) from anus x 100)/( length of tail)']).strip()
            col_027 = str(row['body length / distance from anterior to base of esophageal glands']).strip()
            col_028 = str(row['body length / distance from anterior to esophago-intestinal valve']).strip()
            col_028 = str(row['body length / greatest body diameter']).strip()
            col_030 = str(row['body length / tail length']).strip()
            col_031 = str(row['capitulum length in µm']).strip()
            col_032 = str(row['conus of stomatostyle/total stomatosyle length']).strip()
            col_033 = str(row['distance from anterior end to excretory pore in µm']).strip()
            col_034 = str(row['distance from base of stylet to median bulb valve/stylet length.']).strip()
            col_035 = str(row['distance from vulva to anus']).strip()
            col_036 = str(row['gubernaculurn length in µm']).strip()
            col_037 = str(row['number of body annules between anterior and excretory pore']).strip()
            col_039 = str(row['number of body annules between anus and tail tip']).strip()
            col_040 = str(row['number of body annules between vulva and anus']).strip()
            col_041 = str(row['number of body annules between vulva and tail tip']).strip()
            col_042 = str(row['number of specimens on which measurements are based']).strip()
            col_043 = str(row['portion of body from anus or cloaca to posterior terminus']).strip()
            col_044 = str(row['SE/L (measured in same units) expressed as %).']).strip()
            col_045 = str(row['spicule length in µm']).strip()
            col_046 = str(row['stylet extension (odontophore) length in µm']).strip()
            col_047 = str(row['stylet length / body diameter at base of stylet']).strip()
            col_048 = str(row['stylet length/body length (measured in same units as %).']).strip()
            col_049 = str(row['tail length / tail diameter at anus or cloaca']).strip()
            col_050 = str(row['total number of body annules']).strip()
            col_051 = str(row['Flickr URL']).strip()

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
                dest_image = './../../Slide/ogf-0021/ogf_familes/' + Family
                if not os.path.exists(dest_image):
                    os.makedirs(dest_image)
                dest_image = './../../Slide/ogf-0021/ogf_familes/' + Family + '/' + str(count).zfill(5) + '.jpg'

                #src_image = str(j).strip().replace('\\\\', '/')
                add_text_to_image(src_image, dest_image, image_loc, Family,Genus,View)
                x = 1
                count = count +1

                #Insert A Row
                create_image_dataframe.loc[count] = ['name' + str(count)] + list(randint(10, size=2))

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


