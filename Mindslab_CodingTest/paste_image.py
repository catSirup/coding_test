# 자른 이미지를 다시 연결해서 붙여주는 기능을 구현
# cut_image.py에서 자른 이미지를 가져다 씁니다.
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from common import column_number, row_number
from itertools import product

originImg = Image.open('./datas/original/sample.png')
originWidth, originHeight = originImg.size

# 자른 파일이 저장된 경로에서 이미지 경로 가져오기
path = './datas/cuted_images/'
file_list = os.listdir(path)
file_list = sorted(file_list)

# 가져온 이미지 경로로 이미지를 가져와서 저장 및 출력
sub_images = []
count = 1
for sub_image_path in file_list:
    if sub_image_path == '.DS_Store':
        continue

    sub_image = Image.open(path + sub_image_path)
    sub_images.append(sub_image)

    plt.subplot(row_number, column_number, count)
    plt.title('test_' + str(count) + '.png')
    plt.imshow(sub_image)
    count += 1

plt.tight_layout()
plt.show()

# 이미지를 체크해서 어떻게 돌아갔는지 확인하기 위해서
# 1. 각 이미지들에 대해 모두 mirroring, flipping, rotation을 시킨 이미지를 저장
# 2. 저장된 각 이미지들을 모두 붙여 합성된 이미지를 만듦
# 3. 최종적으로 합성된 이미지를 대상으로 edge 픽셀 체크
# 의 방식으로 진행될 예정

# 우선 이미지들을 모두 변환시켜 저장한다.
# 한 눈에 보기 쉽게 모두 출력합니다.
transformed_images = []
for image in sub_images:
    # 변형될 이미지를 담을 리스트
    transformed_image_list = []

    # 변환 안한 경우
    original_image = image
    plt.subplot(3, 3, 1)
    plt.title('original')
    plt.imshow(original_image)

    # 한 가지 변환을 했다고 가정할 경우
    mirroring_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    plt.subplot(3, 3, 2)
    plt.title('mirroring')
    plt.imshow(mirroring_image)

    flipping_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.subplot(3, 3, 3)
    plt.title('flipping')
    plt.imshow(flipping_image)

    width, height = image.size
    if width > height:
        tempImg = Image.new("RGB",(width, width))
    else:
        tempImg = Image.new("RGB",(height, height))

    tempImg.paste(image, box=(0, 0))
    tempImg = tempImg.rotate(-90)
    rotation_image = tempImg
    rotation_image = tempImg.crop((0, 0, height, width))

    plt.subplot(3, 3, 4)
    plt.title('rotation')
    plt.imshow(rotation_image)

    # 두 가지 이상의 변환을 했다고 가정할 경우
    # rotate가 제일 마지막 변환이므로 rotate가 들어간 변환은 로테이션된 이미지를 변형한다.
    # 1) 미러링과 플리핑
    mirror_and_flip_image = mirroring_image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.subplot(3, 3, 5)
    plt.title('mirror_and_flip')
    plt.imshow(mirror_and_flip_image)

    # 2) 로테이트 및 미러링
    rotate_and_mirror_image = rotation_image.transpose(Image.FLIP_LEFT_RIGHT)
    plt.subplot(3, 3, 6)
    plt.title('rotate_and_mirror')
    plt.imshow(rotate_and_mirror_image)

    # 3) 로테이트 및 플리핑
    rotate_and_flip_image = rotation_image.transpose(Image.FLIP_TOP_BOTTOM)
    plt.subplot(3, 3, 7)
    plt.title('rotate_and_flip')
    plt.imshow(rotate_and_flip_image)

    # 세 가지 모두 변환을 했다고 가정할 경우
    # 마찬가지로 로테이션을 먼저 해주고 나머지 작업을 진행한다.
    rotate_and_flip_and_mirror = rotate_and_flip_image.transpose(Image.FLIP_LEFT_RIGHT)
    plt.subplot(3, 3, 8)
    plt.title('rotate_and_flip_and_mirror')
    plt.imshow(rotate_and_flip_and_mirror)

    # Q. 변환 후 이미지가 width, height가 맞지 않으면 여기서 날려도 되지 않을까?
    # A. 내가 원하는 이미지가 rotation version이 아니라면 날려도 될 것 같다.
    
    # 모두 담는다.
    transformed_image_list.append(original_image)
    transformed_image_list.append(mirroring_image)
    transformed_image_list.append(flipping_image)
    transformed_image_list.append(rotation_image)
    transformed_image_list.append(mirror_and_flip_image)
    transformed_image_list.append(rotate_and_mirror_image)
    transformed_image_list.append(rotate_and_flip_image)
    transformed_image_list.append(rotate_and_flip_and_mirror)

    # 리스트에 담아준다.
    transformed_images.append(transformed_image_list)

    plt.tight_layout()
    plt.show()

# 저장된 각 이미지들을 합성해보자!
# 각 리스트 별로 하나씩 아이템을 가져와서 조합을 시도하자
# 조합을 이렇게 하면 나올 수 있는 정상적인 이미지는 원본 이미지밖에 없다.
temp_pasted_image = list(product(*transformed_images))
pasted_image_list = []

# 각 리스트별로 이미지 조합
# 2 by 2 이미지 기준으로 4096개의 이미지가 생성됨..
# 이 부분에서 n by m 도 가능하게 수정할 수 있다.
# 일단은 기능 구현을 위해 2 by 2 기준으로 작성
count = 0
for i in range(0, len(temp_pasted_image)):
    imglist = temp_pasted_image[i]
    # 이미지 생성 후 붙임
    pasted_image = Image.new("RGB",(originWidth, originHeight))
    pasted_image.paste(imglist[0], box=(0, 0))
    pasted_image.paste(imglist[1], box=(int(originWidth / 2), 0))
    pasted_image.paste(imglist[2], box=(0, int(originHeight / 2)))
    pasted_image.paste(imglist[3], box=(int(originWidth / 2), int(originHeight / 2)))
    
    # pasted_image.save('./datas/pasted_image/pasted_image_' + str(count) + '.png')
    # count += 1
    # 붙인 이미지 저장
    pasted_image_list.append(pasted_image)

# 이제 edge 별로 이 들이 자연스러운지 확인을 해야 한다.
# 원본 이미지, mirroring version, flipping version, rotation version
# edge 들을 계산해서
# 맞는 것 같다 싶으면 True, 아니면 False 반환
# img - 이미지
# check_width, check_height - 잘랐던 이미지 간격. 간격 앞뒤양옆으로 픽셀 컬러값 계산.
# 제일 높은 놈 값을 가져온다.
def check_correction(img):
    answer = True
    count = 0.0

    for i in range(0, img.size[1] - 1):
        temp1 = img.getpixel((int(originWidth / 2) + 1, i))
        temp2 = img.getpixel((int(originWidth / 2) - 1, i))
        if temp1 == (0, 0, 0) or temp2 == (0, 0, 0):
            continue

        sum = temp1[0] + temp1[1] + temp1[2] - temp2[0] - temp2[1] - temp2[2]
        if abs(sum) <= 20:
            count += 1.0

    for i in range(0, img.size[0] - 1):
        temp1 = img.getpixel((i, int(originHeight / 2) + 1))
        temp2 = img.getpixel((i, int(originHeight / 2) - 1))
        if temp1 == (0, 0, 0) or temp2 == (0, 0, 0):
            continue

        sum = temp1[0] + temp1[1] + temp1[2] - temp2[0] - temp2[1] - temp2[2]
        if abs(sum) <= 20:
            count += 1.0

    if (count / (img.size[1] + img.size[0])) * 100 < 80:
        answer = False
    
    else:
        print ((count / (img.size[1] + img.size[0])) * 100)

    return answer

# 모두 가져오기 위해 리스트 생성
selected_image_list = []

for img in pasted_image_list:
    #if check_correction_cheat(img) == True:
    if check_correction(img) == True:
        selected_image_list.append(img)
    else:
        continue

size = len(selected_image_list)
print("total size: " + str(size))
count = 0
for result_image in selected_image_list:
    plt.plot()
    plt.imshow(result_image)
    plt.show()

