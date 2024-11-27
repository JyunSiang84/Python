## A. 機器學習中「特徵」(Feature)的概念很重要：
### A1. 特徵的定義：
  - 是用來描述數據樣本的屬性或特性
  - 是模型學習的輸入變數
  - 決定了模型能學到什麼

### A2. 特徵的類型：
有些特徵很特別，我們也可稱為標籤labels。
```Python
# 數值型特徵
age = 25
height = 170.5
weight = 65.3

# 類別型特徵
gender = "female"
color = "red"

# 布林型特徵
is_student = True
has_car = False
```
### A3. 特徵工程的常見處理：
  - 標準化：當特徵尺度差異大時使用
  - One-Hot編碼：處理類別變數
  - 缺失值填充：處理不完整數據
  - 特徵選擇：減少特徵維度
  - 特徵組合：捕捉特徵間的關係
  - 時間特徵：處理時序數據
  - 文本處理：將文本轉換為數值特徵

```Pytho
from sklearn.preprocessing import StandardScaler

# 標準化數值特徵
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 類別特徵編碼
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
gender_encoded = encoder.fit_transform(['male', 'female', 'male'])
```

### A4. 特徵的重要性：
  - 影響模型性能
  - 決定模型的學習效果
  - 好的特徵可以簡化模型

### A5. 常見的特徵處理方法：
  - 特徵選擇：選擇最重要的特徵
  - 特徵縮放：將特徵值調整到相似範圍
  - 特徵組合：創建新的複合特徵
  - 特徵轉換：改變特徵的表示方式
實際例子：房價預測模型的特徵
```Pytho
house_features = {
    '面積': 100,  # 數值特徵
    '房間數': 3,  # 整數特徵
    '位置': '市中心',  # 類別特徵
    '有車位': True,  # 布林特徵
    '建築年份': 2010  # 時間特徵
}
```
### A6. 特徵工程的步驟：
  - 特徵提取：從原始數據中提取有用信息
  - 特徵處理：處理缺失值、異常值
  - 特徵轉換：將特徵轉換為模型可用的格式
  - 特徵創建：基於領域知識創建新特徵

## B. 機器學習的三種主要類型：
### B1.監督式學習 (Supervised Learning)：
  - 定義：透過已標記的數據來學習，需要標記數據，直接的評估指標
  - 輸入：特徵(X)和標籤(y)
  - 目標：學習特徵和標籤之間的關係，適合預測問題
  - 
#### B1-1. 分類 (Classification)：
  - 目標：預測類別（離散值）
  - 輸出：類別標籤或機率

常見分類算法：
```python
# 二元分類：預測是/否
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# 邏輯回歸
model = LogisticRegression()
# 預測顧客是否會流失
model.fit(customer_features, churn_labels)  # 1=流失, 0=留存

# 決策樹
model = DecisionTreeClassifier()
# 預測郵件是否為垃圾郵件
model.fit(email_features, spam_labels)  # 1=垃圾, 0=正常
```
評估指標：
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score

# 準確率
accuracy = accuracy_score(y_true, y_pred)
# 精確率
precision = precision_score(y_true, y_pred)
# 召回率
recall = recall_score(y_true, y_pred)
```
常見應用：
  - 預測離散類別。例如：垃圾郵件檢測、疾病診斷
  - 評估關注準確率、精確率、召回率

#### B1-2. 回歸 (Regression)：
  - 目標：預測數值（連續值）
  - 輸出：數值預測

常見回歸算法：
```python
# 線性回歸
from sklearn.linear_model import LinearRegression

model = LinearRegression()
# 預測房屋價格
model.fit(house_features, prices)

# 隨機森林回歸
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
# 預測股票價格
model.fit(stock_features, stock_prices)
```

評估指標：
```python
from sklearn.metrics import mean_squared_error, r2_score

# 均方誤差
mse = mean_squared_error(y_true, y_pred)
# R平方值
r2 = r2_score(y_true, y_pred)
```

```python
# 分類問題示例
from sklearn.linear_model import LogisticRegression
# 訓練模型預測顧客是否會購買產品
model = LogisticRegression()
model.fit(customer_features, purchase_history)

# 回歸問題示例
from sklearn.linear_model import LinearRegression
# 訓練模型預測房屋價格
model = LinearRegression()
model.fit(house_features, house_prices)
```

常見應用：
  - 預測連續數值。例如：房價預測、溫度預測、預測股價
  - 評估關注誤差大小、擬合程度。例如：垃圾郵件分類

### B2. 非監督式學習 (Unsupervised Learning)：
  - 定義：從未標記的數據中發現模式，不需要標記數據，評估較困難
  - 輸入：只有特徵(X)，沒有標籤
  - 目標：發現數據中的隱藏結構，適合探索性分析
    
另外討論非監督式學習評估較困難的原因有以下幾點：
1. 缺乏標準答案：
  - 沒有真實標籤作為參考
  - 無法直接計算準確率
```python
# 監督式學習可以這樣評估
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)

# 非監督式學習沒有y_true來比較
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X)  # 只有預測結果，沒有標準答案
```

2. 評估指標的主觀性：
  - 分群結果好壞難以定義
  - 不同應用場景有不同標準
```python
# 常用的評估方法：輪廓係數(Silhouette Score)
from sklearn.metrics import silhouette_score
score = silhouette_score(X, clusters)
# 但這個分數只反映分群的緊密度，不一定符合業務需求
```

3. 結果的多樣性：
  - 同樣的數據可能有多種合理的分群方式
  - 不同的參數設定會得到不同結果

```python
# 例如：K-means的K值選擇
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    # 哪個k值最好？往往沒有標準答案
```
    
4. 評估方法的限制：
  - 內部評估指標（如緊密度）
  - 外部評估指標（需要部分標記數據）
  - 兩種方法都有其侷限性

6. 實際例子 {顧客分群問題}：
```python
# 假設我們將顧客分為三群
kmeans = KMeans(n_clusters=3)
customer_segments = kmeans.fit_predict(customer_data)

# 評估困難點：
# 1. 3群是否合適？
# 2. 每群的特徵是否有業務意義？
# 3. 分群結果是否實用？
```

7. 常用的評估方法：
```python
from sklearn.metrics import davies_bouldin_score, calinski_harabasz_score

# Davies-Bouldin指標
db_score = davies_bouldin_score(X, clusters)

# Calinski-Harabasz指標
ch_score = calinski_harabasz_score(X, clusters)

# 但這些指標都只能提供參考，不能完全反映分群品質
```

8. 驗證方法：
  - 業務專家評估
  - 抽樣檢查
  - 交叉驗證
  - A/B測試

常見應用：客戶分群、異常檢測
```python
# 分群示例
from sklearn.cluster import KMeans
# 將顧客分群
kmeans = KMeans(n_clusters=3)
customer_segments = kmeans.fit_predict(customer_data)

# 降維示例
from sklearn.decomposition import PCA
# 降低特徵維度
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(high_dim_data)
```

### B3.強化學習 (Reinforcement Learning)：
  - 定義：透過與環境互動來學習最佳策略，需要互動環境
  - 輸入：環境狀態和動作的獎勵，透過試錯學習
  - 目標：最大化長期獎勵，適合連續決策問題

常見應用：遊戲AI、機器人控制
```python
# 簡單的Q-learning示例
def q_learning(state, action, reward, next_state):
    old_value = q_table[state, action]
    next_max = np.max(q_table[next_state])
    
    # Q-learning公式
    new_value = (1 - learning_rate) * old_value + \
                learning_rate * (reward + discount_factor * next_max)
    q_table[state, action] = new_value
```
