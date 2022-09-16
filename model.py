def model_pred():
    import os
    import random
    import PIL.Image
    import torch
    import torch.nn as nn
    from torchvision import models,transforms
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model = models.resnet50()
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 10)
    model.to(device)
    model.load_state_dict(torch.load("C:\\Users\\omerf\\OneDrive\\Desktop\\Staj çalışmalarım\\Ömer\\Driver state\\model-driver",  map_location=device))
    model.eval()
    path_test = "C:\\Users\\omerf\\OneDrive\\Desktop\\Staj çalışmalarım\\Ömer\\Driver state\\kamera_foto"
    list_img_test = [img for img in os.listdir(path_test) if not img.startswith(".")]
    list_img_test.sort()
    from torchvision import models,transforms,datasets
    transform = transforms.Compose([transforms.Resize((400, 400)),
                            transforms.RandomRotation(10),
                            transforms.ToTensor(),
                            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                            ])
    class_dict = {0 : "safe driving",
                1 : "texting - right",
                2 : "talking on the phone - right",
                3 : "texting - left",
                4 : "talking on the phone - left",
                5 : "operating the radio",
                6 : "drinking",
                7 : "reaching behind",
                8 : "hair and makeup",
                9 : "talking to passenger"}
    file = random.choice(list_img_test)
    im_path = os.path.join(path_test,file)

    with PIL.Image.open(im_path) as im:
        im = transform(im)
        im = im.unsqueeze(0)
        output = model(im)
        proba = nn.Softmax(dim=1)(output)
        proba = [round(float(elem),4) for elem in proba[0]]
        print(proba)
        print("Predicted class:",class_dict[proba.index(max(proba))])
        print("Confidence:",max(proba))
        proba2 = proba.copy()
        proba2[proba2.index(max(proba2))] = 0.
        print("2nd answer:",class_dict[proba2.index(max(proba2))])
        print("Confidence:",max(proba2))
        return f'{class_dict[proba.index(max(proba))]}'