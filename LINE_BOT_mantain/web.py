from flask import Flask,render_template,send_from_directory,request, jsonify
from flask import *

import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/flex_button_msg',methods=['POST','GET'])
def flex_botton_msg():
    return render_template("1_flex_button_msg.html")

@app.route('/youtube_video',methods=['POST','GET'])
def youtube_video():
    return render_template("2_youtube_video.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400
    file = request.files["file"]
    
    if file.filename == "":
        return "No selected file", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file_name = file.filename.split('.')[0]
    file.save(file_path)

    # 解析 Excel
    df = pd.read_excel(file_path)

    if file_name == "flex_button_msg":
        json_data = {
            row["關鍵字"]: {
                "template": file_name,
                "altText": row["altText"],
                "contents_text": row["contents_text"],
                "footer": row["footer"].split(",")  # 轉換為列表
            }
            for _, row in df.iterrows()
        }
    elif file_name == "youtube_video":
        json_data = {
            row["關鍵字"]: {
                "template": file_name,
                "altText": row["altText"],
                "video_img_url": row["video_img_url"],
                "video_uri": row["video_uri"],
                "FlexBox":{
                    "Main_text": row["Main_text"],
                    "Sub_text": row["Sub_text"]
                }
            }
            for _, row in df.iterrows()
        }

    # 存 JSON 檔案
    json_filename = file.filename.replace(".xlsx", ".json")
    json_path = os.path.join("reponses", json_filename)
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    return "success"


if __name__=='__main__':
    app.run(debug=True, use_reloader=False)