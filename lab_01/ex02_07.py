print(" nhập các dòng văn bản (nhập 'done' để end):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    print("\nCác dòng đã nhập sau khi chuyển:")
    for line in lines:
        print(line.upper())