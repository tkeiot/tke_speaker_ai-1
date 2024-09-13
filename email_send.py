import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open('/home/pi/Emo_Pi4/api_email.json', 'r') as file:
    email_data = json.load(file)

send_email = [(xyz['sender_email'])for xyz in email_data]
app_pass = [(xyz['app_password'])for xyz in email_data]
recei_email = [(xyz['receiver_email'])for xyz in email_data]

send_email = send_email[0] 
app_pass = app_pass[0]
recei_email = recei_email[0]

sender_email = send_email   # Emai gửi
app_password = app_pass  # Mật khẩu ứng dụng app password 
receiver_email = recei_email # Email nhận

# Thông tin người gửi và người nhận
#sender_email = "chatrobotrux@gmail.com"   # Emai gửi
#app_password = "yoqz ltym shqx ugpw"  # Mật khẩu ứng dụng app password 
#receiver_email = "ngoctung2008@gmail.com" # Email nhận

def send_email():
    
    # Tạo nội dung email
    subject = "Cập nhật: Test Email"
    body = "Đây là nội dung của email được gửi từ Python với bảo mật mới nhất."

    # Tạo đối tượng MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Thêm nội dung vào email
    message.attach(MIMEText(body, "plain"))
    # Kết nối với máy chủ SMTP và gửi email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Kích hoạt bảo mật TLS
            server.login(sender_email, app_password)  # Đăng nhập bằng mật khẩu ứng dụng
            server.sendmail(sender_email, receiver_email, message.as_string())  # Gửi email
            print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Không thể gửi email. Lỗi: {e}")


'''
1. Mật khẩu ứng dụng (App Password):

App Password là một mã xác thực dùng một lần được tạo từ tài khoản Google của bạn
để tăng cường bảo mật. Bạn có thể tạo App Password trong trang quản lý tài khoản Google
dưới phần "Security" (Bảo mật).

2. Xác thực OAuth2:

Ngoài việc sử dụng mật khẩu ứng dụng, bạn cũng có thể triển khai xác thực OAuth2 nếu bạn
cần tích hợp sâu hơn và bảo mật cao hơn. OAuth2 yêu cầu một quy trình thiết lập phức tạp
hơn, phù hợp khi phát triển ứng dụng quy mô lớn.

3. Các bước thiết lập App Password:
Truy cập vào Tài khoản Google của bạn.
Chọn Security (Bảo mật) từ menu bên trái.
Dưới mục Signing in to Google (Đăng nhập vào Google),
bật 2-Step Verification (Xác minh 2 bước) nếu chưa bật.
Sau đó, bạn sẽ thấy tùy chọn App passwords (Mật khẩu ứng dụng) xuất hiện.
Tạo một App Password mới cho ứng dụng gửi email của bạn.

'''

