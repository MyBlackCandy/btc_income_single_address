# BTC Income Bot (Single Address)

บอทสำหรับ Telegram ที่ใช้ตรวจสอบรายการธุรกรรมขาเข้าของ Bitcoin (BTC) สำหรับ address เดียวแบบเรียลไทม์ พร้อมแสดงมูลค่าเป็น USD

## คุณสมบัติ

- แจ้งเตือนธุรกรรม BTC ขาเข้าทุกครั้งที่พบรายการใหม่
- แสดง BTC, USD, TXID และผู้ส่ง
- ตรวจสอบทุก 10 วินาที

## วิธีใช้บน Railway

1. **สร้างโปรเจกต์ใหม่**
2. **อัปโหลดไฟล์จาก repo นี้ หรือใช้ GitHub**
3. **เพิ่ม Environment Variables ดังนี้:**

| Key           | ตัวอย่าง                                       |
|---------------|------------------------------------------------|
| `BOT_TOKEN`   | `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`     |
| `CHAT_ID`     | `-1001234567890` (หรือ ID ของคุณเอง)           |
| `BTC_ADDRESS` | `bc1qxyz...`                                    |

4. **ไฟล์เริ่มต้น**: ไม่มี Procfile ให้ตั้ง `Start Command` เป็น: python main.py


5. **Deploy แล้วดูผลลัพธ์ใน Telegram**

## ข้อควรระวัง

- ใช้ได้กับ address แบบ SegWit (`bc1...`) หรือ legacy ก็ได้
- ใช้ API จาก blockchain.info และ Binance
- หากต้องการติดตามหลาย address กรุณาใช้เวอร์ชัน multi-address

---

หากคุณต้องการไฟล์ `.zip` หรือ repository พร้อม deploy เพิ่มเติม แจ้งได้เลยครับ.
