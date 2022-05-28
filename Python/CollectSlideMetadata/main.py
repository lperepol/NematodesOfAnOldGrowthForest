import pandas as pd
#import odfpy  #To Install

def read_ods(fname):
    df= pd.read_excel(fname, engine="odf")
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

    for f in filelist:
        df = read_ods(f)
        df["Dir"] = f

        if df1.empty:
            df1 = df
        else:
            df1 = pd.concat([df1, df])
    outFile = './../../Metadata/AppendedSlideMetadata.csv'
    df1.to_csv(outFile,index=False )
    return

if __name__ == '__main__':
    main()


