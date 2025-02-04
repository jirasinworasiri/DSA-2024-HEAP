import heapq
from datetime import datetime

class Patient:
    def __init__(self, queue_number, priority):
        self.queue_number = queue_number
        self.priority = priority  # ระดับความรุนแรง 1-5 (1 = ฉุกเฉินมาก)
        self.arrival_time = datetime.now()
    
    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

class ERQueue:
    def __init__(self):
        self.queue = []  # Min Heap เพื่อให้ผู้ป่วยที่มี priority ต่ำ (อาการหนัก) ได้รับการรักษาก่อน
        self.queue_counter = 1
    
    def add_patient(self, priority):
        patient = Patient(self.queue_counter, priority)
        heapq.heappush(self.queue, patient)
        self.queue_counter += 1
        print(f"เพิ่มผู้ป่วย คิวเลขที่ {patient.queue_number}, ระดับความรุนแรง {patient.priority}")
    
    def treat_next_patient(self):
        if self.queue:
            patient = heapq.heappop(self.queue)
            wait_time = datetime.now() - patient.arrival_time
            print(f"รักษาผู้ป่วย คิวเลขที่ {patient.queue_number}, ระดับความรุนแรง {patient.priority}, เวลารอ {wait_time.seconds} วินาที")
            return patient
        print("ไม่มีผู้ป่วยในคิว")
        return None

    def display_queue(self):
        if not self.queue:
            print("ไม่มีผู้ป่วยในคิว")
            return
        print("\nรายการคิวที่รอ:")
        temp_queue = sorted(self.queue, key=lambda p: (p.priority, p.arrival_time))
        for patient in temp_queue:
            print(f"คิวเลขที่ {patient.queue_number}, ระดับความรุนแรง {patient.priority}")
        print("-" * 30)

# ตัวอย่างการใช้งาน
def demo_er_queue():
    er = ERQueue()
    
    # เพิ่มผู้ป่วยเข้าคิว
    patients = [
        (1),  # หัวใจวาย
        (3),  # ปวดท้อง
        (2)   # กระดูกหัก
    ]
    
    for priority in patients:
        er.add_patient(priority)
    
    print("\nแสดงลำดับคิว:")
    er.display_queue()
    
    # จำลองการรักษาผู้ป่วย
    print("\nเริ่มรักษาผู้ป่วย:")
    for _ in range(len(patients)):
        er.treat_next_patient()

if __name__ == "__main__":
    demo_er_queue()
