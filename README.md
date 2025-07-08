# Game Caro 15x15 - Người vs Máy

## Giới thiệu
Đây là chương trình game Caro (Gomoku) 15x15 viết bằng Python sử dụng thư viện Tkinter để tạo giao diện đồ họa. Người chơi sẽ đấu với máy (AI). Giao diện trực quan, dễ sử dụng, có nút "Chơi lại" để bắt đầu ván mới.

## Tính năng
- Bàn cờ 15x15, giao diện đẹp, rõ ràng.
- Người chơi đi trước, đánh bằng chuột trái.
- Máy (AI) có chiến thuật cơ bản: ưu tiên thắng, chặn thắng, chọn nước gần quân người nhất.
- Thông báo khi thắng, thua hoặc hòa.
- Có nút "Chơi lại" để reset bàn cờ và bắt đầu ván mới.

## Cách sử dụng
1. **Yêu cầu:**
   - Đã cài Python 3.x (khuyến nghị 3.7 trở lên).
   - Không cần cài thêm thư viện ngoài (Tkinter có sẵn trong Python chuẩn).

2. **Chạy chương trình:**
   - Mở Command Prompt hoặc PowerShell.
   - Di chuyển đến thư mục chứa file `caro_game.py`:
     ```powershell
     cd d:\CARO
     ```
   - Chạy lệnh:
     ```powershell
     python caro_game.py
     ```
   - Giao diện game sẽ hiện ra, bạn click chuột trái để đánh cờ.

3. **Chơi lại:**
   - Nhấn nút "Chơi lại" để bắt đầu ván mới bất cứ lúc nào.

## Cấu trúc chương trình
- `caro_game.py`: Toàn bộ mã nguồn game, gồm giao diện, xử lý bàn cờ, AI và chức năng chơi lại.
- (Nếu chia module: `main.py`, `caro_board.py`, `bot.py`)

## Nguyên lý hoạt động
- Khi người chơi click vào ô trống, chương trình sẽ kiểm tra hợp lệ, vẽ quân đen và kiểm tra thắng/thua.
- Nếu chưa kết thúc, máy sẽ tự động đánh theo chiến thuật:
  1. Nếu có thể thắng, máy sẽ đi nước thắng.
  2. Nếu người chơi sắp thắng, máy sẽ chặn lại.
  3. Nếu không, máy chọn nước gần quân người nhất để tạo thế mạnh.
- Khi có người thắng hoặc hòa, sẽ hiện thông báo.
- Nút "Chơi lại" sẽ reset toàn bộ bàn cờ và trạng thái game.

## Đóng góp
Bạn có thể nâng cấp AI, giao diện hoặc chia nhỏ chương trình thành các module để dễ bảo trì hơn.

---
Mọi thắc mắc hoặc góp ý, vui lòng liên hệ tác giả hoặc để lại bình luận.
