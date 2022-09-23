---
tags: ML APP_Text to image
---

# ML APP_Text to image
## How to use app
1.於cmd輸入python app.py即會顯示輸入畫面

2.於輸入框輸入文字則會產生對應的圖片,由於GPU內存不夠故使用colab進行Demo

## File Description
* app.py-使用本機端機器開ML APP進行訓練,
* authtoken.py-由於引入外部Hugging Face的Stable Diffusion Model,故需要輸入個人token的權限
* Stable Diffusion.ipynb:因為考量到cuda memory,故使用colab進行訊練

##Demo