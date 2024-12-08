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

考慮添加的功能：
- 支援更多圖片格式
- 添加進度回調功能
- 支援批次處理多個檔案
- 添加更多的圖片優化選項
- 添加更多圖片處理功能（如圖片旋轉、濾鏡效果等）
- 開發簡單的圖形使用者介面
- 加入批次處理功能
- 整合到更大的專案中
