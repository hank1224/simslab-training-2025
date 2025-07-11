# 持久化 session 的範例程式

## 簡介

此程式為一簡易終端機計時器，會於每秒在同一行顯示已經過的時間，直到達到設定秒數或使用者按下 Ctrl+C 中斷。
並且使用 tmux 來持久化 session，確保即使中斷連線後，程式仍然在後台運行。

# 運行程式

### 1. 建立虛擬環境
```bash
uv venv
```

### 2. 載入當前資料夾內的虛擬環境：
```bash
source venv/bin/activate
```

### 3. 安裝必要套件
```bash
pip install -r requirements.txt
```

### 4. 運行範例

```bash
# 兩種都可以
uv run timer_3min.py
python3 timer_3min.py
```

# 關掉 Warp 視窗，模擬中斷連線

直接關閉 Warp 視窗，這時候你的程式就跟著 session 一起被關閉了。

連線回來後，執行階段也找不回來了。

# 使用 tmux 來持久化 session

### 1. 建立新的 tmux session
```bash
tmux new -s SESSION_NAME
```

### 2. 在 tmux session 中運行程式
```bash
source venv/bin/activate
python3 timer_3min.py
```

### 3. 模擬中斷連線

直接關閉視窗

### 4. 重新連線到 tmux session
```bash
tmux attach -t SESSION_NAME
```

### 5. 結束 tmux session
```bash
exit
```