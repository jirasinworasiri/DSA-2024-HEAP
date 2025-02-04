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

# สร้าง Max Heap
max_heap = MaxHeap()
values = [5, 3, 8, 1, 2, 7, 6, 4]

# แทรกค่าทั้งหมดลงใน Heap
for val in values:
    max_heap.push(val)

# แสดงค่าใน Max Heap หลังจากเพิ่มค่าครบแล้ว
print("Max Heap:", max_heap.to_list())
