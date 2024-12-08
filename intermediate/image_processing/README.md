# 圖片壓縮模組說明文件
## 簡介
這個模組提供了一個強大且靈活的圖片壓縮解決方案，能夠在保持可接受的圖片品質的同時，將圖片檔案大小壓縮到指定範圍內。它採用了兩階段壓縮策略：首先透過調整圖片品質來壓縮，如果還不夠，則會進一步縮減圖片尺寸。

## 目錄結構：
```
intermediate/
├── image_processing/
│   ├── __init__.py
│   ├── image_compressor.py    # 圖片壓縮程式碼
│   ├── examples/             # 使用範例
│   │   ├── sample_images/    # 測試用圖片
│   │   └── compress_demo.py  # 示範程式
│   └── README.md            # 模組說明文件
```
## 主要特點
- 自動調整圖片品質
- 智能尺寸縮放
- 詳細的壓縮過程記錄
- 完整的錯誤處理機制
- 可自定義的壓縮參數
## 安裝需求
### 必要套件
1. Python 3.6 或以上版本
2. Pillow (PIL) 套件
### 安裝步驟
```bash
# 安裝 Pillow 套件
pip install Pillow

# 如果需要升級 pip
python -m pip install --upgrade pip
```
## 使用說明
### 基本使用
```python
from image_processing.image_compressor import compress_image

# 基本使用
final_size, info = compress_image(
    input_path='original.jpg',
    output_path='compressed.jpg'
)
print(f"壓縮後大小：{final_size:.2f}MB")
```
### 進階使用
可以自定義更多參數來控制壓縮過程：
```python
# 進階使用，設定自定義參數
final_size, info = compress_image(
    input_path='original.jpg',
    output_path='compressed.jpg',
    max_size_mb=2.0,        # 設定最大檔案大小為 2MB
    min_quality=30,         # 設定最低品質為 30
    min_dimension=800,      # 設定最小尺寸為 800 像素
    initial_quality=90      # 設定初始壓縮品質為 90
)

# 印出詳細的壓縮資訊
print(f"原始大小：{info['original_size_mb']:.2f}MB")
print(f"最終大小：{final_size:.2f}MB")
print(f"壓縮步驟數：{len(info['compression_steps'])}")
```
### 參數說明
| 參數名稱  | 類型 | 預設值 | 說明 |
| -------- | ---- | ------ | --- |
| input_path | str | 必填 | 輸入圖片的路徑 |
| output_path | str | 必填 | 輸出圖片的路徑 |
| max_size_mb | float | 1.0 | 目標檔案大小（MB）|
| min_quality | int | 20 | 最低可接受的圖片品質（1-100）|
| min_dimension | int | 500 | 最小可接受的圖片尺寸（像素）|
| initial_quality | int | 95 | 初始壓縮品質（1-100）|

### 回傳值說明
函式會回傳一個元組，包含兩個元素：
1. 最終檔案大小（float，單位為 MB）
2. 詳細的處理資訊（dictionary）

處理資訊字典包含：
- original_size_mb：原始檔案大小
- original_dimensions：原始圖片尺寸
- final_quality：最終品質設定
- final_dimensions：最終圖片尺寸
- compression_steps：壓縮過程的詳細步驟

### 常見問題與解決方案
1. 找不到輸入檔案：出現 "找不到輸入檔案" 錯誤
- 確認檔案路徑是否正確
- 檢查檔案名稱大小寫
- 使用絕對路徑而非相對路徑
2. 無法達到目標大小：出現 "無法達到目標大小" 錯誤
- 調高 max_size_mb 參數
- 降低 min_quality 參數
- 降低 min_dimension 參數
3. 圖片品質不佳：壓縮後的圖片品質不理想
- 提高 min_quality 參數
- 提高 initial_quality 參數
- 適當調整 max_size_mb 參數
### 進階技巧
#### 批次處理多個檔案
```python
import os

def batch_compress(input_dir, output_dir, **kwargs):
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                final_size, info = compress_image(input_path, output_path, **kwargs)
                print(f"已處理 {filename}: {final_size:.2f}MB")
            except Exception as e:
                print(f"處理 {filename} 時發生錯誤: {str(e)}")
```
#### 壓縮進度追蹤
```python
final_size, info = compress_image(input_path, output_path)
for step in info['compression_steps']:
    if step['action'] == 'quality_reduction':
        print(f"品質調整至 {step['quality']}, 檔案大小: {step['size_mb']:.2f}MB")
    else:
        print(f"尺寸調整至 {step['dimensions']}, 檔案大小: {step['size_mb']:.2f}MB")
```

### 效能建議
1. 對於大量圖片處理：
- 考慮使用多執行緒處理
- 設定適當的初始品質值以減少嘗試次數
- 使用 RAM 磁碟來加速暫存檔案的讀寫
2. 對於高解析度圖片：
- 先評估是否需要保持原始解析度
- 考慮設定較大的 min_dimension 值
- 可能需要調整 max_size_mb 參數

### 未來目標
考慮添加的功能：
- 支援更多圖片格式
- 添加進度回調功能
- 支援批次處理多個檔案
- 添加更多的圖片優化選項
- 添加更多圖片處理功能（如圖片旋轉、濾鏡效果等）
- 開發簡單的圖形使用者介面
- 加入批次處理功能
- 整合到更大的專案中
