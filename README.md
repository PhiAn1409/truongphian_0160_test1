# truongphian_0160_test1
truongphian_0160_test1

# Bài tập Git: chương trình Python đơn giản

Mục tiêu: cung cấp một chương trình Python nhỏ để bạn thực hành các thao tác Git cơ bản (clone, branch, commit, merge, resolve conflict, tag).

Thư mục chính:
- `src/` - chứa mã nguồn chương trình đơn giản.

Hướng dẫn nhanh để làm bài tập Git (gợi ý các bước):

1. Clone repository này về máy của bạn.
2. Tạo branch mới để làm bài: `git checkout -b ten-nhanh-cua-ban`.
3. Chạy chương trình:

```powershell
python src/main.py
```

4. Thay đổi một thông điệp trong `src/utils.py` (ví dụ sửa lời chào), sau đó commit thay đổi:

```powershell
git add src/utils.py
git commit -m "Sửa lời chào trong utils"
```

5. Tạo pull request (hoặc merge) vào nhánh chính. Để thực hành xung đột (conflict):
	- Tạo một branch khác (ví dụ `branch-conflict`) và thay đổi cùng dòng trong `src/utils.py`, commit và push.
	- Quay lại branch chính, cũng thay đổi cùng dòng khác theo cách khác, commit.
	- Thực hiện merge để thấy xung đột và học cách resolve.

6. Tạo tag cho phiên bản: `git tag -a v1.0 -m "Phiên bản 1.0"` và push tag: `git push origin v1.0`.

Chúc bạn học tốt! Nếu cần thêm bài tập (ví dụ: tests, CI, hooks), hãy yêu cầu.
