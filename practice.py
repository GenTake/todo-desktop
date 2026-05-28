# 変数（データを入れる箱）
app_name = "Todoアプリ"
print(app_name)

# リスト（複数のデータをまとめて管理する）
tasks = ["買い物", "洗濯", "勉強"]
tasks.append("運動")  # リストに追加
print(tasks)

# 関数（処理をまとめて名前をつけたもの）
def add_task(task_list, new_task):
    task_list.append(new_task)
    return task_list

result = add_task(tasks, "読書")
print(result)
