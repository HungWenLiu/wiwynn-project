# 使用輕量級 Python 3.9 映像檔
FROM python:3.9-slim

# 設定容器內的工作目錄
WORKDIR /app

# 複製依賴清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼到容器內
COPY . .

# 設定容器啟動指令 (使用 Port 8080 以配合 GCP Cloud Run 預設)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]