from PIL import Image, ImageDraw, ImageFont, ImageColor
def add_num(img):
    #创建一个Draw对象
    draw = ImageDraw.Draw(img)
    #创建一个Font
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)
    fillcolor = ImageColor.colormap.get('red')
    width , height = img.size
    draw.text((width-30,0),'12',font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('D:\chen.jpg')
    add_num(image)
