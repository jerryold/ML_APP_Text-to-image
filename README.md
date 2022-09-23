---
tags: ML APP_Text to image
---

# ML APP_Text to image
## How to use app
1.於cmd輸入python app.py即會顯示輸入畫面

2.於輸入框輸入文字則會產生對應的圖片,由於GPU內存不夠故使用colab進行Demo
![ML APP](https://user-images.githubusercontent.com/12774427/191927476-3258c2f2-9321-47c1-9517-93cfed8bda2e.png)


## File Description
* app.py-使用本機端機器開ML APP進行訓練,
* authtoken.py-由於引入外部Hugging Face的Stable Diffusion Model,故需要輸入個人token的權限
* Stable Diffusion.ipynb:因為考量到cuda memory,故使用colab進行訊練

## Pretrained Model-Stable Diffusion v1-4 Model Card(https://huggingface.co/CompVis/stable-diffusion-v1-4)
The Stable-Diffusion-v1-4 checkpoint was initialized with the weights of the Stable-Diffusion-v1-2 checkpoint and subsequently fine-tuned on 225k steps at resolution 512x512 on "laion-aesthetics v2 5+", and it's a  text-to-image diffusion model capable of generating photo-realistic images given any text input.

## Hugging Face Token申請
https://huggingface.co/docs/hub/security-tokens

##Demo

https://user-images.githubusercontent.com/12774427/191927761-dd8c4dbe-fba6-45c1-8cf3-554b2d1dc792.mp4

