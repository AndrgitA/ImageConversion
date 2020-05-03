import zipfile
import os

from PIL import Image, ImageDraw, ImageFont, ImageFile
from io import BytesIO
from datetime import datetime
import hashlib 
class Conversion:
    """
        Класс преобразования изображений
    """
    def __init__(self):
        self.allowedFormats = set(['png', 'jpg', 'jpeg'])
        self.outputFormats = {
            "png": "PNG",
            "jpg": "JPEG",
            "jpeg": "JPEG"
        }
        
        pathDir = os.path.dirname(os.path.realpath(__file__))

        self.folderUploads = os.path.normpath(pathDir + "/../uploads/")
        self.rootDir = os.path.normpath(pathDir + "/../../../")
        self.fontDir = os.path.join(self.rootDir, "frontend/src/assets/fonts/")

    def run(self, file, options):
        """
            Производит преобразования в зависимости от опций над файлами изображений в архиве
        """
        isZipFile = zipfile.is_zipfile(file)
                
        if isZipFile:
            outFile = hashlib.md5(bytes(str(datetime.now()), "utf-8")).hexdigest()

            zFile = zipfile.ZipFile(file, 'r')
            outputFileName = outFile + ".zip"
            zOutFile = zipfile.ZipFile(os.path.join(self.folderUploads, outputFileName), 'w')

            count = 0
            countConversion = 0

            for imageInfo in zFile.filelist:
                filename = imageInfo.filename
                count = count + 1
                if self._allowedFormat(filename):
                    countConversion = countConversion + 1
                    fileImage = zFile.open(imageInfo.filename)

                    image = Image.open(fileImage)

                    for option in options:
                        image = self._conversion(image, option)

                    image = image.convert("RGB")

                    imageOutFile = BytesIO()
                    image.save(imageOutFile, self.outputFormats[filename.rsplit('.', 1)[1]].upper())
                    zOutFile.writestr(filename, imageOutFile.getvalue())

            return {
                "count": count,
                "countConversion": countConversion,
                "file": "/uploads/" + outputFileName
            }

        return None
    
    def _conversion(self, image, option):
        tmpImage = image

        mode = option['mode'] if 'mode' in option else None
        
        #Оттенок серого
        if mode == "shade_gray":
            tmpImage = tmpImage.convert("LA")

        #изменение размера до указанного
        elif mode == "resize":
            width = option["w"] if "w" in option else tmpImage.width
            height = option["h"] if "h" in option else tmpImage.height
            tmpImage = tmpImage.resize((width, height))

        #надпись образец на каждом изображении
        elif mode == 'sample':
            fontSize = 20
            txt = "Образец"
            strWidth = fontSize * len(txt)
            n = int(tmpImage.width / strWidth) + 1
            m = 3

            f = ImageFont.truetype(os.path.join(self.fontDir, "suisse_bold.ttf"), fontSize)
            d = ImageDraw.Draw(tmpImage)

            for i in range(n):
                for j in range(m):
                    d.text((i * strWidth, j * int(tmpImage.height / 3)), "Образец", font = f, fill = 255)

        #изменение в n раз
        elif mode == 'scale':
            value = option["value"] if "value" in option else 1
            width = tmpImage.width
            height = tmpImage.height
            tmpImage = tmpImage.resize((int(width * value), int(height * value)))

        return tmpImage

    def _allowedFormat(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in self.allowedFormats