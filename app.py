from asyncio.windows_utils import pipe
from email.mime import image
import tkinter as tk
from turtle import width
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

#Create the app
app=tk.Tk()
app.geometry("532x632")
app.title("Text to image")
ctk.set_appearance_mode("dark")

#文字輸入框設定
inputspace= ctk.CTkEntry(height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white") 
inputspace.place(x=10, y=10)

lmain = ctk.CTkLabel(height=512, width=512)
lmain.place(x=10, y=110)

# modelid="CompVis/stable-diffusion-v1-1"
# device="cuda"
# pipe=StableDiffusionPipeline.from_pretrained(modelid,torch_dtype=torch.float16, revision="fp16", use_auth_token=auth_token)

# pipe.to(device)


# def generate():
#     with autocast(device):
#         image=pipe(inputspace.get(),guidance_scale=8.5)["sample"][0]
#     img=ImageTk.PhotoImage(image)
#     image.save("generatedimage.png")
#     lmain.configure(image=img)
    

trigger = ctk.CTkButton(height=40, width=120, text_font=("Arial", 20), text_color="white", fg_color="brown") 
trigger.configure(text="Generate") 
trigger.place(x=206, y=60) 


app.mainloop()
