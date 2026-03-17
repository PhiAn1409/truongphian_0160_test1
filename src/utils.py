def greet(name: str) -> str:
    """Trả về chuỗi lời chào đơn giản."""
    name = name.strip() if name else "Bạn"
    return f"Xin chào, {name}! Chúc bạn làm bài tập Git thành công."


def add(a: float, b: float) -> float:
    """Trả về tổng hai số (hỗ trợ int/float)."""
    return a + b
