inventory = {
    "꿀꽈배기": 10,
    "매운새우깡": 3,
    "오징어집": 0,
    "프링글스": 5
}

#stock ( 재고 : 스퉉)
for item,stock in inventory.items():
    if stock == 0:
        print(f"🔴 {item} 재고가 없습니다!")
    elif stock < 5:
        print(f"⚠️ {item} 재고가 부족합니다! (현재 {stock}개 남음)")
    else:
        print(f"✅ {item} 재고 충분! (현재 {stock}개)")