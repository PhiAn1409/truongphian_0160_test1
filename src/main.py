from __future__ import annotations

from utils import greet, add


def main() -> None:
    print("Chương trình đơn giản để luyện tập Git\n")
    try:
        name = input("Nhập tên của bạn: ")
    except EOFError:
        name = ""

    print(greet(name))

    try:
        a_text = input("Số thứ nhất: ")
        b_text = input("Số thứ hai: ")
        a = float(a_text)
        b = float(b_text)
        print(f"Tổng: {add(a, b)}")
    except ValueError:
        print("Giá trị không hợp lệ, hãy nhập số.")


if __name__ == "__main__":
    main()
