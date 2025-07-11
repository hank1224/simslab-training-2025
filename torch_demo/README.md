# 線性回歸範例 (PyTorch)

## 簡介

此範例程式示範如何使用 PyTorch 實作簡單線性回歸模型，包含資料準備、參數初始化、訓練流程及模型參數恢復。

## 程式結構

* `main()` 函式包含以下步驟：

  1. **資料生成**：合成線性資料 y = 2 x + 1 + noise
  2. **參數初始化**：隨機產生 w，b 初始為 0
  3. **優化器設定**：使用 `torch.optim.SGD`
  4. **訓練迴圈**：50 個 Epoch，並每 10 Epoch 印出一次 loss
  5. **結果輸出**：顯示經訓練後的 w, b

## 安裝方式

### 1. 建立虛擬環境
```bash
uv venv
```

### 2. 載入當前資料夾內的虛擬環境：
```bash
source venv/bin/activate
```

### 3. 安裝符合這臺電腦的 pytorch：

[官網安裝](https://pytorch.org/get-started/locally/)

```bash
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

### 4. 運行範例

```bash
# 兩種都可以
uv run linear_regression_torch.py
python3 linear_regression_torch.py
```

### 5. 結束使用，退出虛擬環境

```bash
deactivate
```