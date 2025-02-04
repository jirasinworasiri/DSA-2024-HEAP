import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, -val)  # ใช้ค่าลบเพื่อจำลอง Max Heap
    
    def pop(self):
        return -heapq.heappop(self.heap)  # แปลงค่ากลับเป็นบวก
    
    def peek(self):
        return -self.heap[0] if self.heap else None
    
    def to_list(self):
        return sorted([-val for val in self.heap], reverse=True)  # คืนค่าเป็นลิสต์ที่เรียงจากมากไปน้อย

def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2):  # ตรวจสอบเฉพาะโหนดภายในที่มีลูก
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

# สร้าง Max Heap
max_heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]

# แทรกค่าทั้งหมดลงใน Heap
for val in values:
    max_heap.push(val)

# แสดงค่าใน Max Heap หลังจากเพิ่มค่าครบแล้ว
heap_list = max_heap.to_list()
print("Max Heap:", heap_list)

# ลบค่าสูงสุด 3 ครั้ง และแสดงค่าหลังจากลบแต่ละครั้ง
for i in range(3):
    removed = max_heap.pop()
    heap_list = max_heap.to_list()
    print(f"หลังจากลบ {removed}: {heap_list}")

# ตรวจสอบว่าเป็น Max Heap หรือไม่
print("Is Max Heap?", is_max_heap(heap_list))
