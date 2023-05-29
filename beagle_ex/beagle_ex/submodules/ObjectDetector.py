import roboidai as ai
cam = ai.Camera('usb0')

dt = ai.ObjectDetector(multi = True, lang='en')
dt.download_model()
dt.load_model()
count = 0
while True:
    image = cam.read()
    if dt.detect(image):
        image = dt.draw_result(image)
        labels = dt.get_label()
        print(dt.get_label())    
        cam.show(image)

    if cam.check_key() == 'esc': break
    
    
