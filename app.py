import tkinter as tk
import json
import os
from tkinter import messagebox

#メインウィンドウの設定
root = tk.Tk()
root.title("Todo アプリ Ver.B")
root.geometry("400x500")

#タスクリスト（メモリ上で管理）
task_list = []

SAVE_FILE = "tasks.json"

def save_tasks():
    data = [listbox.get(i) for i in range(listbox.size())]
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        #PythonのデータをJSON形式でファイルに書き込む
        json.dump(data, f, ensure_ascii=False)

def load_tasks():
    if not os.path.exists(SAVE_FILE):
        return
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        for task in data:
            listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("注意", "タスクを入力してください")
        return
    task_list.append(task)
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("注意", "削除するタスクを選択してください")
        return
    index = selected[0]
    listbox.delete(index)
    task_list.pop(index)
    save_tasks()

def complete_task():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    current = listbox.get(index)
    if not current.startswith("✓ "):
        listbox.delete(index)
        listbox.insert(index, "✓ " + current)
    save_tasks()

#タイトルラベル
label = tk.Label(root, text="Todo アプリ", font=("Arial", 18, "bold"))
label.pack(pady=10)

#入力欄とボタン
frame = tk.Frame(root)
frame.pack(pady=5)
entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)
add_button = tk.Button(frame, text="追加", command=add_task)
add_button.pack(side=tk.LEFT)

#タスク一覧
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=10)

#操作ボタン
button_frame = tk.Frame(root)
button_frame.pack(pady=5)
tk.Button(button_frame, text="完了", command=complete_task).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="削除", command=delete_task).pack(side=tk.LEFT, padx=5)

#アプリを起動する
load_tasks()
root.mainloop()

