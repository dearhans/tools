import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# 定义颜色和表情的映射
color_emoji_map = {
    "红色": "😢",
    "黄色": "😄",
    "绿色": "😐"
}

# 定义底图模板
base_images = {
    "红色": "red_template.png",
    "黄色": "yellow_template.png",
    "绿色": "green_template.png"
}

def save_record():
    date = date_entry.get()
    mood = mood_entry.get()
    color = color_var.get()
    emoji = color_emoji_map[color]
    image_path = image_label.cget("text")

    # 这里可以添加保存记录到文件或数据库的代码
    print(f"日期: {date}")
    print(f"心情: {mood} {emoji}")
    print(f"配图: {image_path}")

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image_label.config(text=file_path)
        try:
            img = Image.open(file_path)
            img.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(img)
            image_display.config(image=photo)
            image_display.image = photo
        except Exception as e:
            print(f"无法打开图片: {e}")

# 创建主窗口
root = tk.Tk()
root.title("记录生命中的感动")

# 日期输入
date_label = tk.Label(root, text="日期:")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

# 心情输入
mood_label = tk.Label(root, text="一句话心情:")
mood_label.pack()
mood_entry = tk.Entry(root)
mood_entry.pack()

# 颜色选择
color_var = tk.StringVar(root)
color_var.set("黄色")  # 默认选择黄色
color_menu = tk.OptionMenu(root, color_var, "红色", "黄色", "绿色")
color_menu.pack()

# 选择图片
image_button = tk.Button(root, text="选择配图", command=select_image)
image_button.pack()
image_label = tk.Label(root, text="未选择图片")
image_label.pack()
image_display = tk.Label(root)
image_display.pack()

# 保存记录
save_button = tk.Button(root, text="保存记录", command=save_record)
save_button.pack()

# 运行主循环
root.mainloop()
