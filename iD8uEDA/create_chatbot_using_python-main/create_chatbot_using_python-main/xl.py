import pickle
import numpy as np
import h5py

# Tải lại mô hình phân loại (đảm bảo bạn đã lưu mô hình vào tệp model.pkl)
import h5py

# Tải lại mô hình phân loại từ tệp chatbot_model.h5
with open("chatbot_model.h5", "rb") as model_file:
    model = pickle.load(model_file)

#with open("chatbot_model.h5", "rb") as model_file:
#    model = pickle.load(model_file)

# Đọc dữ liệu từ tệp văn bản hoặc từ nguồn dữ liệu của bạn
# Ví dụ: Đọc từ tệp data.txt
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

# Dự đoán tag cho các mẫu văn bản
predicted_tags = model.predict(data)

# Tạo nội dung cho các tag dựa trên dự đoán
for i, tag in enumerate(predicted_tags):
    # Tùy chỉnh phản hồi hoặc nội dung tương ứng với tag
    # Ví dụ: Nếu tag là "greeting", bạn có thể trả lời bằng một câu chào hỏi tương ứng
    print(f"Phản hồi cho mẫu {i+1} thuộc tag {tag}:")
    # Tùy chỉnh phản hồi hoặc nội dung tương ứng với tag
import pickle
import json

# Tải lại mô hình phân loại (đảm bảo bạn đã lưu mô hình vào tệp chatbot_model.h5)
with open("chatbot_model.h5", "rb") as model_file:
    model = pickle.load(model_file)

# Đọc dữ liệu từ tệp văn bản hoặc từ nguồn dữ liệu của bạn
# Ví dụ: Đọc từ tệp data.txt
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

# Dự đoán tag cho các mẫu văn bản
predicted_tags = model.predict(data)

# Tạo dữ liệu cho các tag
output_data = []
for i, tag in enumerate(predicted_tags):
    output_data.append({
        "tag": tag,
        "patterns": [data[i].strip()],
        "responses": ["Your custom response here"],
        "context": ["general"]
    })

# Lưu vào tệp JSON
with open("intents.json", "w", encoding="utf-8") as json_file:
    json.dump(output_data, json_file, ensure_ascii=False, indent=4)

print("Dữ liệu đã được lưu vào tệp intents.json")

