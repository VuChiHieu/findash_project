# FinDash — Financial Dashboard with Chatbot

Dashboard phân tích tài chính (CAPM, APT, Efficient Frontier, Monte Carlo...) kèm
Chatbot hỗ trợ, xây dựng bằng Streamlit.

> 📌 Repo: https://github.com/VuChiHieu/findash_project

---

## Cấu trúc project

```
findash_project/
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

---

## Hướng dẫn cài đặt và chạy — từng bước

Hướng dẫn này viết cho cả người **chưa từng dùng Git/lập trình bao giờ**, cứ làm
theo đúng thứ tự là chạy được.

### Yêu cầu trước khi bắt đầu

Bạn cần cài sẵn 2 phần mềm sau (nếu chưa có):

1. **Python** (bản 3.9 trở lên) — tải tại https://www.python.org/downloads/
   - Khi cài trên Windows, nhớ tick vào ô **"Add Python to PATH"** ở màn hình đầu tiên
     của trình cài đặt, nếu không các lệnh `python`, `pip` ở bước sau sẽ báo lỗi
     "not recognized".
2. **Git** — tải tại https://git-scm.com/downloads (cứ bấm Next liên tục theo mặc định
   là được).

Cài xong, mở lại terminal (Command Prompt / PowerShell / Terminal) rồi gõ thử 2 lệnh
sau để kiểm tra đã cài thành công chưa:

```bash
python --version
git --version
```

Nếu mỗi lệnh đều hiện ra một số phiên bản (ví dụ `Python 3.11.4`, `git version 2.42.0`)
là ổn, sang bước tiếp theo.

### Bước 1: Tải project về máy (clone)

Mở terminal, di chuyển tới thư mục bạn muốn chứa project, ví dụ Desktop:

```bash
# Windows (Command Prompt hoặc PowerShell):
cd Desktop

# macOS / Linux:
cd ~/Desktop
```

Sau đó gõ lệnh sau để tải project về:

```bash
git clone https://github.com/VuChiHieu/findash_project.git
```

Lệnh này sẽ tạo ra một thư mục tên `findash_project` ngay tại vị trí bạn đang đứng,
chứa toàn bộ code của project.

> 💡 Không quen dùng terminal? Bạn có thể vào thẳng
> https://github.com/VuChiHieu/findash_project → bấm nút xanh **`<> Code`** →
> **Download ZIP** → giải nén ra là dùng được, không cần lệnh `git clone` ở trên.
> Cách này đơn giản hơn nhưng sau này muốn cập nhật bản mới thì phải tải ZIP lại
> từ đầu, còn dùng `git clone` thì chỉ cần gõ `git pull` (xem cuối bài).

### Bước 2: Di chuyển vào thư mục project

```bash
cd findash_project
```

Lưu ý: **mọi lệnh ở các bước sau đều phải chạy khi đang đứng trong thư mục
`findash_project`** này (đừng `cd` ra ngoài nữa). Bạn có thể kiểm tra đã vào đúng
thư mục chưa bằng lệnh `ls` (macOS/Linux) hoặc `dir` (Windows) — sẽ thấy file
`app.py` và `requirements.txt` hiện ra.

### Bước 3: Tạo môi trường ảo Python (virtual environment)

Vẫn đang trong thư mục `findash_project`, chạy:

```bash
python -m venv venv
```

Lệnh này tạo ra một thư mục con tên `venv` (chứa Python riêng cho project, không
ảnh hưởng tới Python hệ thống). Đây là bước chỉ cần làm **một lần duy nhất**.

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

> ⚠️ Nếu dùng PowerShell mà báo lỗi liên quan "execution policy", gõ lệnh sau rồi
> thử kích hoạt lại:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

### Bước 5: Cài các thư viện cần thiết

Vẫn trong thư mục `findash_project` và đã kích hoạt `venv` (thấy `(venv)` ở đầu dòng):

```bash
pip install -r requirements.txt
```

Đợi cài xong (có thể mất vài phút tuỳ tốc độ mạng). Đây cũng là bước chỉ cần làm
một lần (trừ khi xoá `venv` đi làm lại).

### Bước 6: Cấu hình API key cho Chatbot (bắt buộc nếu muốn dùng tab Chatbot)

1. Đăng ký / đăng nhập tại https://console.anthropic.com và tạo một API key.
2. Trong thư mục `findash_project`, vào thư mục con `.streamlit` (thư mục này có
   dấu chấm ở đầu nên có thể bị ẩn — trên macOS/Linux dùng `ls -a` để thấy, trên
   Windows bật **"Show hidden files"** trong File Explorer).
3. Copy file `.streamlit/secrets.toml.example` thành file mới tên
   `.streamlit/secrets.toml` (bỏ đuôi `.example`).
4. Mở `.streamlit/secrets.toml` bằng trình soạn thảo text bất kỳ (Notepad, VS Code...),
   sửa dòng:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
   thay `sk-ant-...` bằng API key thật của bạn.

Nếu bỏ qua bước này, tab Chatbot vẫn dùng được — nó sẽ hiện ô nhập API key ngay
trên giao diện web, chỉ dùng cho phiên làm việc hiện tại (không lưu lại).

### Bước 7: Chạy ứng dụng

Vẫn đứng trong thư mục `findash_project`, đã kích hoạt `venv`:

```bash
streamlit run app.py
```

Trình duyệt sẽ tự mở ra địa chỉ `http://localhost:8501` với dashboard. Nếu lần đầu
chạy Streamlit hỏi email, cứ bấm **Enter** để bỏ qua, không ảnh hưởng gì.

Muốn tắt app: quay lại terminal, bấm `Ctrl + C`.

---

## Các lần chạy sau

Mỗi lần mở lại project (sau khi tắt terminal), bạn **không cần làm lại Bước 1, 3, 5**
(clone, tạo venv, cài thư viện) — chỉ cần:

```bash
cd đường-dẫn-tới/findash_project
source venv/bin/activate      # Windows: venv\Scripts\activate.bat (CMD) hoặc venv\Scripts\Activate.ps1 (PowerShell)
streamlit run app.py
```

## Cập nhật project khi có bản mới

Nếu bạn clone bằng `git clone` (không phải tải ZIP), muốn lấy phiên bản mới nhất
từ repo, đứng trong thư mục `findash_project` và chạy:

```bash
git pull
pip install -r requirements.txt
```

(lệnh `pip install` lại phòng khi có thư viện mới được thêm vào).

---

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

## Xử lý lỗi thường gặp

| Lỗi | Cách khắc phục |
|---|---|
| `git` hoặc `python` không được nhận diện ("not recognized") | Cài lại Python/Git, nhớ tick "Add to PATH" khi cài Python trên Windows |
| `streamlit: command not found` | Kiểm tra đã kích hoạt `venv` chưa (có chữ `(venv)` ở đầu dòng lệnh chưa) |
| Lỗi khi kích hoạt venv trên PowerShell | Chạy `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` rồi thử lại |
| Tab Chatbot không hoạt động | Kiểm tra lại `.streamlit/secrets.toml` đã điền đúng `ANTHROPIC_API_KEY` chưa, hoặc nhập key trực tiếp trên giao diện web |
| `pip install` báo lỗi/treo lâu | Kiểm tra kết nối mạng, hoặc thử lại lệnh `pip install -r requirements.txt` |