def genCharVideo(self, filepath):
self.charVideo =[]
# 用opencv读取视频
cap = cv2.VideoCapture(filepath)
self.timeInterval = round(1/ cap.get(5),3)
nf = int(cap.get(7))
print('Generate char video, please wait...')
for i in pyprind.prog_bar(range(nf)):
# 转换颜色空间，第二个参数是转换类型，cv2.COLOR_BGR2GRAY表示从BGR↔Gray
rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
frame = self.convert(rawFrame, os.get_terminal_size(), fill=True)
self.charVideo.append(frame)
cap.release()
ascii_frame
ascii_char ="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 像素映射到字符
def pixelToChar(self, luminance):
return self.ascii_char[int(luminance /256* len(self.ascii_char))]
# 将普通帧转为 ASCII 字符帧
def convert(self, img, limitSize=-1, fill=False, wrap=False):
if limitSize !=-1and(img.shape[0]> limitSize[1]or img.shape[1]> 
    limitSize[0]):
    img = cv2.resize(img, limitSize, 
    interpolation=cv2.INTER_AREA)
    ascii_frame =''
    blank =''
if fill:
   blank +=' '*(limitSize[0]- img.shape[1])
if wrap:
   blank +='\n'
for i in range(img.shape[0]):
   for j in range(img.shape[1]):
      ascii_frame += self.pixelToChar(img[i, j])
      ascii_frame += blank
      return ascii_frame
	  # 创建线程
getchar = threading.Thread(target=getChar)
# 设置为守护线程
getchar.daemon =True
# 启动守护线程
getchar.start()
# 输出的字符画行数
rows = len(self.charVideo[0])// os.get_terminal_size()[0]
for frame in self.charVideo:
    # 接收到输入则退出循环
    if breakflag:
        break
    self.streamOut(frame)
    self.streamFlush()
    time.sleep(self.timeInterval)
    # 共 rows 行，光标上移 rows-1 行回到开始处
    self.streamOut('\033[{}A\r'.format(rows -1))
    # 光标下移 rows-1 行到最后一行，清空最后一行
    self.streamOut('\033[{}B\033[K'.format(rows -1))
    # 清空最后一帧的所有行（从倒数第二行起）
    for i in range(rows -1):
       # 光标上移一行
       self.streamOut('\033[1A')
       # 清空光标所在行
       self.streamOut('\r\033[K')
       if breakflag:
          self.streamOut('User interrupt!\n')
       else:
          self.streamOut('Finished!\n')