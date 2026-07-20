# FinDash — Financial Dashboard with Chatbot

## Cấu trúc project

```
findash/
├── app.py                      # entry point, chạy: streamlit run app.py
├── requirements.txt
├── data/
│   └── data_utils.py           # toàn bộ hàm lấy dữ liệu (yfinance)
├── analysis/
│   ├── capm.py                 # CAPM, APT, Efficient Frontier
│   └── monte_carlo.py          # Monte Carlo cho 1 mã và cả danh mục
├── tabs/
│   ├── tab_summary.py          # [1] Summary
│   ├── tab_chart.py            # [2] Chart
│   ├── tab_statistics.py       # [3] Statistics/Financials/Analysis
│   ├── tab_portfolio.py        # [4] Portfolio: CAPM/APT + Efficient Frontier + Monte Carlo danh mục
│   ├── tab_montecarlo.py       # [5] Monte Carlo Simulation (1 mã)
│   └── tab_chatbot.py          # Chatbot hỗ trợ
└── .streamlit/
    └── secrets.toml.example    # đổi tên thành secrets.toml, điền API key
```

## Hướng dẫn cài đặt và chạy — từng bước

### Bước 1: Giải nén project

Giải nén file `findash_project.zip` vào một thư mục bất kỳ trên máy, ví dụ giải nén
ra thư mục có tên `findash`. Sau bước này bạn sẽ có một thư mục `findash` chứa toàn
bộ cấu trúc file ở trên.

### Bước 2: Mở terminal / command prompt và di chuyển vào thư mục project

```bash
cd đường-dẫn-tới/findash
```

Ví dụ nếu bạn giải nén ra Desktop:

- **Windows:** `cd C:\Users\TênBạn\Desktop\findash`
- **macOS/Linux:** `cd ~/Desktop/findash`

Lưu ý: mọi lệnh ở các bước sau đều phải chạy **khi đang đứng trong thư mục `findash`**
này (tức là sau khi `cd` vào rồi, đừng `cd` ra ngoài nữa). Bạn có thể kiểm tra đã vào
đúng thư mục chưa bằng lệnh `ls` (macOS/Linux) hoặc `dir` (Windows) — sẽ thấy file
`app.py` và `requirements.txt` hiện ra.

### Bước 3: Tạo môi trường ảo Python (virtual environment)

Vẫn đang trong thư mục `findash`, chạy:

```bash
python -m venv venv
```

Lệnh này tạo ra một thư mục con tên `venv` bên trong `findash` (thư mục này chứa
Python riêng cho project, không ảnh hưởng tới Python hệ thống).

### Bước 4: Kích hoạt (activate) môi trường ảo

```bash
# macOS / Linux:
source venv/bin/activate

# Windows (Command Prompt):
venv\Scripts\activate.bat

# Windows (PowerShell):
venv\Scripts\Activate.ps1
```

Sau khi kích hoạt thành công, bạn sẽ thấy chữ `(venv)` xuất hiện ở đầu dòng lệnh.
Từ giờ mọi lệnh `pip`/`python`/`streamlit` sẽ dùng đúng môi trường này.

### Bước 5: Cài các thư viện cần thiết

Vẫn trong thư mục `findash` và đã kích hoạt `venv`:

```bash
pip install -r requirements.txt
```

Đợi cài xong (có thể mất vài phút tuỳ tốc độ mạng).

### Bước 6: Cấu hình API key cho Chatbot (bắt buộc nếu muốn dùng tab Chatbot)

1. Đăng ký / đăng nhập tại https://console.anthropic.com và tạo một API key.
2. Trong thư mục `findash`, vào thư mục con `.streamlit` (thư mục này có dấu chấm
   ở đầu nên có thể bị ẩn — trên macOS/Linux dùng `ls -a` để thấy, trên Windows bật
   "Show hidden files" trong File Explorer).
3. Copy file `.streamlit/secrets.toml.example` thành file mới tên
   `.streamlit/secrets.toml` (bỏ đuôi `.example`).
4. Mở `.streamlit/secrets.toml` bằng trình soạn thảo text bất kỳ, sửa dòng:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
   thay `sk-ant-...` bằng API key thật của bạn.

Nếu bỏ qua bước này, tab Chatbot vẫn dùng được — nó sẽ hiện ô nhập API key ngay
trên giao diện web, chỉ dùng cho phiên làm việc hiện tại (không lưu lại).

### Bước 7: Chạy ứng dụng

Vẫn đứng trong thư mục `findash`, đã kích hoạt `venv`:

```bash
streamlit run app.py
```

Trình duyệt sẽ tự mở ra địa chỉ `http://localhost:8501` với dashboard.

### Các lần chạy sau

Mỗi lần mở lại project (sau khi tắt terminal), bạn chỉ cần lặp lại Bước 2, Bước 4,
Bước 7 (không cần tạo lại `venv` hay `pip install` lại, trừ khi bạn xoá thư mục
`venv` hoặc đổi máy):

```bash
cd đường-dẫn-tới/findash
source venv/bin/activate      # Windows: venv\Scripts\activate.bat
streamlit run app.py
```

## Ghi chú quan trọng

- Toàn bộ dữ liệu lấy qua `yfinance` (KHÔNG dùng `yahoo_fin` vì thư viện này đã
  ngừng hoạt động do Yahoo Finance đổi cấu trúc trang).
- Danh sách mã S&P 500 được scrape từ Wikipedia, có cache 1 ngày để tránh gọi lại
  liên tục. Nếu lỗi mạng, sẽ tự dùng danh sách fallback nhỏ.
- Nếu muốn hỗ trợ cổ phiếu Việt Nam (HOSE/HNX), Yahoo Finance hỗ trợ rất hạn chế —
  nên cân nhắc bổ sung thư viện `vnstock` làm nguồn dữ liệu thứ hai cho các mã VN.
- Phần CAPM/APT dùng `statsmodels.OLS`. APT có UI riêng trong `tab_portfolio.py`
  (section "5. APT"), cho chọn nhân tố (thị trường, lãi suất, dầu, vàng, USD index).
- Monte Carlo có 2 phiên bản, cả 2 đều đã có UI: 1 mã (`tab_montecarlo.py`, giữ
  logic gốc từ code mẫu) và cả danh mục (section "6. Monte Carlo Simulation cho
  Danh mục" trong `tab_portfolio.py`, dùng phân rã Cholesky để giữ tương quan
  giữa các mã).
- Các giá trị bị thiếu (`None`) từ `yfinance` được tự động hiển thị là "N/A" thay
  vì làm vỡ giao diện (xem hàm `fmt_value()` và `is_valid_ticker_info()` trong
  `data/data_utils.py`).

## Các công thức tài chính đã cài đặt

Xem chi tiết công thức và giải thích trong file báo cáo `FinDash_Bao_Cao_Cong_Thuc.docx`
đi kèm. Tóm tắt nhanh: CAPM, APT đa nhân tố, Sharpe Ratio, Efficient Frontier
(mô phỏng Monte Carlo trọng số ngẫu nhiên), Monte Carlo dự báo giá (random walk),
Value at Risk (VaR).
