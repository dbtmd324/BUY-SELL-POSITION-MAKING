import os
import glob
from PIL import Image
import splitfolders

# 0. data 폴더 및 하위 디렉토리 생성
if not os.path.exists('dataset'):
    os.makedirs('data')
    os.makedirs('dataset')
    os.makedirs('./dataset/train/up_up')
    os.makedirs('./dataset/train/up_down')
    os.makedirs('./dataset/train/down_up')
    os.makedirs('./dataset/train/down_down')
    os.makedirs('./dataset/train/sideways')
    os.makedirs('./dataset/test/up_up')
    os.makedirs('./dataset/test/up_down')
    os.makedirs('./dataset/test/down_up')
    os.makedirs('./dataset/test/down_down')
    os.makedirs('./dataset/test/sideways')

i = 0
folders_path = "C:/Users/user/PycharmProjects/DaishinAPI/code_snippet/images_3"
folders_data = glob.glob(os.path.join(folders_path, "*"))

for folder in folders_data:
    folder_name = os.path.basename(folder)[:7] # 원본 내 종목 폴더 이름
    print('원본 종목 폴더 경로: ', folder)
    print('원본 종목 이름: ', folder_name)

    folder_data = glob.glob(os.path.join(folder, "*"))

    # 1. 원본 종목 폴더 trainset, testset 1차 구분
    splitfolders.ratio(folder, output=f'data/{folder_name}', seed=42, ratio=(0.8, 0.1, 0.1))

    # 2. data 조건문 접근하기
    # trainset, testset 2차 구분
    labels_path = glob.glob(os.path.join(f'.\\data\\{folder_name}', "*")) # data 폴더 내 train, test 접근
    # print(labels_path)

    label_path_train = labels_path[0]
    label_path_test = labels_path[1]

    label_name_train = os.path.basename(label_path_train)[-5:]  # train
    label_name_test = os.path.basename(label_path_test)[-3:]  # test(폴더명은 val로 되어있음)
    # print(label_name_train)
    # print(label_name_test)

    label_path_train = glob.glob(os.path.join(label_path_train, "*")) # train 경로
    label_path_test = glob.glob(os.path.join(label_path_test, "*"))  # test 경로(폴더명은 val로 되어있음)
    # print(label_path_train)
    # print(label_path_test)

    # 3. 이미지를 각각 dataset으로 옮겨주기
    if label_name_train == 'train': # train 폴더인 경우
        for label in label_path_train: # 5개 라벨 접근
            print("라벨 경로: ", label)
            file_name_label = os.path.basename(label)
            print('라벨 명: ', file_name_label)

            images = glob.glob(os.path.join(label, "*.png")) # 이미지들 경로

            for image in images:
                image_name = os.path.basename(image) # 이미지 명
                print('이미지 명: ', image_name)

                img = Image.open(image)
                img.save(f'./dataset/train/{file_name_label}/{image_name}', 'png') # 이미지 dataset으로 이동
                print('train 이동 완료')

    if label_name_test == 'val': # val 폴더인 경우
        for label in label_path_train: # 5개 라벨 접근
            print("라벨 경로: ", label)
            file_name_label = os.path.basename(label)
            print('라벨 명: ', file_name_label)

            images = glob.glob(os.path.join(label, "*.png")) # 이미지들 경로

            # 3. 이미지를 각각 dataset으로 옮겨주기
            for image in images:
                image_name = os.path.basename(image) # 이미지 명
                print('이미지 명: ', image_name)

                img = Image.open(image)
                img.save(f'./dataset/test/{file_name_label}/{image_name}', 'png') # 이미지 dataset으로 이동
                print('test 이동 완료')

    i += 1
    print(f'------------------------------{i}번째 종목 이동 완료------------------------------')






