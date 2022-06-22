
#pip3 install opencv-python
import cv2
import os


def main():

    image_folder = 'Y:/NematodeMicrographsOfTheWestKootenays/NematodeCompare/Indentifying/Dorylaimida-Lips/Jpg_video'
    video_name = 'Dorylaimida-Lips-Compare.avi'

    image_folder = 'Y:/NematodeMicrographsOfTheWestKootenays/NematodeCompare/Criconematidae/Lips/Jpg_video'
    video_name = 'Criconematidae-Lips-Compare.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

