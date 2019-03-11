##Singwa Cheng
##CS9163

from PIL import Image

def resizeImage(fileName):
    try:
        image = Image.open(fileName)
        print("Image loaded\n")
        #save original file extension for export
        ogFormat = '.'+fileName.split('.')[1]
    except IOError:
        print("Image not found, try again.\n")
        return error
    #get dimension
    width, height = image.size
    newSize = max(width, height)
    image = image.resize((newSize, newSize))
    image.save('resized'+ ogFormat)

def main():
    fileName = raw_input("Please enter the filename including the extension: ")
    resizeImage(fileName)

if __name__ == "__main__":
    main()
        
    