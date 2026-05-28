import tkinter as tk

#メインウィンドウの設定
root = tk.Tk()
root.title("Todo アプリ")
root.geometry("400x500")

#タイトルラベル
label = tk.Label(root, text="Todo アプリ", font=("Arial", 18, "bold"))
label.pack(pady=20)

#アプリを起動する
root.mainloop()

