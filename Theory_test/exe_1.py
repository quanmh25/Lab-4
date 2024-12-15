

# Cách 1: Đệ quy
items = {
    'A': (3, 50),
    'B': (2, 40),
    'C': (1, 30)
}
n = len(items)
capacity = 5 

def knap_recursive(capacity, items, n):
    # Trường hợp cơ bản: không còn vật phẩm hoặc dung lượng ba lô đã đầy
    if n == 0 or capacity == 0:
        return 0
    
    # Lấy tên, trọng lượng và giá trị của vật phẩm thứ n-1
    item_name = list(items.keys())[n-1]
    weight, value = items[item_name]
    
    # Nếu trọng lượng của vật phẩm thứ n-1 lớn hơn dung lượng ba lô, bỏ qua nó
    if weight > capacity:
        return knap_recursive(capacity, items, n-1)
    
    # Tùy chọn 1: Chọn vật phẩm thứ n-1
    include_item = value + knap_recursive(capacity - weight, items, n-1)
    # Tùy chọn 2: Không chọn vật phẩm thứ n-1
    exclude_item = knap_recursive(capacity, items, n-1)
    
    # Trả về giá trị tối đa của hai tùy chọn
    return max(include_item, exclude_item)


# Cách 2: Quy hoạch động
def dynamicProg():
    s = [3, 2, 1]         # Space
    v = [50, 40, 30]      # Value
    m = 5                 # max_space

    dp = list([0]*(m+1) for _ in range(len(s)+1))
    for i in range(3):
        for j in range(m+1):
            dp[i+1][j] = dp[i][j]
            if j >= s[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j - s[i]] + v[i])

    print(dp[3][5])



if __name__ == '__main__':

    print(knap_recursive(capacity, items, n))
    for i in range(n):
        item_name = list(items.keys())[i]
        weight, value = items[item_name]
        print(item_name, weight, value)


    dynamicProg()