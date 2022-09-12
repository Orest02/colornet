## Update: 8th Jan, 2022
## this file is supposed to give you a general idea on how to
## use the pre-trained model for colorizing B&W images. This
## file still needs development.

import PIL
import torch
from matplotlib import pyplot as plt
from torchvision import transforms

from models import MainModel, build_res_unet
from utils import lab_to_rgb, rgb_to_l

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    net_G = build_res_unet(n_input=1, n_output=2, size=256)
    net_G.load_state_dict(torch.load("artifacts/res18-unet.pt", map_location=device))
    model = MainModel(net_G=net_G)
    # You first need to download the final_model_weights.pt file from my drive
    # using the command: gdown --id 1lR6DcS4m5InSbZ5y59zkH2mHt_4RQ2KV

    model.load_state_dict(
        torch.load(
            "artifacts/GAN.pt",
            map_location=device
        )
    )
    path = "input/3895858.jpg"
    img = PIL.Image.open(path)

    img = PIL.ImageOps.grayscale(img)

    trs = transforms.Compose([
        transforms.Resize((256, 256), PIL.Image.BICUBIC),
        transforms.ToTensor()
    ])

    img = trs(img)
    print(type(img))
    # to make it between -1 and 1
    img = img[:1] * 2. - 1.
    model.eval()
    with torch.no_grad():
        preds = model.net_G(img.unsqueeze(0).to(device))
    colorized = lab_to_rgb(img.unsqueeze(0), preds.cpu())[0]
    plt.imshow(colorized)
    plt.show()
