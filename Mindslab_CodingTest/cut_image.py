# 이미지를 자른 후 저장해주는 기능을 구현
# column_number 와 row_number를 지정해주면 c x r 의 개수로 잘라서 저장한다.
import random
import matplotlib.pyplot as plt
from PIL import Image
from common import column_number, row_number

# 원본 이미지를 가져와서 출력
image = Image.open('./datas/original/sample.png')
plt.title("Original Image")
plt.imshow(image)
plt.show()

# 이미지의 사이즈를 저장
width, height = image.size

# 자를 사이즈가 딱 맞지 않게 떨어진다면 크기를 임의로 조정한다.
width = width - (width % column_number)
height = height - (height % row_number)

# 잘리는 이미지당 넓이와 높이
seperated_width = int(width / column_number)
seperated_height = int(height / row_number)

# 이미지를 잘라서 저장 및 출력
count = 1   # 이미지 넘버링 용 카운트
for i in range(0, row_number):
    for j in range(0, column_number):
        plt.subplot(row_number, column_number, count)
        plt.title('test_' + str(count) + '.png')
        sub_image = image.crop((j * seperated_width, i * seperated_height, (j + 1) * seperated_width, (i + 1) * seperated_height))

        # random 값을 줘서 변환 여부 체크
        # 0 - false, 1 - true
        random_mirroing = random.randint(0, 1)
        random_flipping = random.randint(0, 1)
        random_rotation = random.randint(0, 1)

        print(random_mirroing, " ", random_flipping, " ", random_rotation)
        if random_mirroing == 1:
            # 좌우 반전 이미지로 변경. 
            sub_image = sub_image.transpose(Image.FLIP_LEFT_RIGHT)
        if random_flipping == 1:
            # 상하 반전 이미지로 변경.
            sub_image = sub_image.transpose(Image.FLIP_TOP_BOTTOM)
        if random_rotation == 1:
            # 90도 회전한 이미지로 변경.
            width, height = sub_image.size

            if width > height:
                tempImg = Image.new("RGB",(width, width))
            else:
                tempImg = Image.new("RGB",(height, height))

            tempImg.paste(sub_image, box=(0, 0))
            tempImg = tempImg.rotate(90)
            sub_image = tempImg
            sub_image = tempImg.crop((0, 0, height, width))
        plt.imshow(sub_image)
        fileName = './datas/cuted_images/test_' + str(count) + '.png'
        sub_image.save(fileName)
        count += 1

plt.tight_layout()
plt.show()