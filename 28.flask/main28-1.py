from flask import Flask

app = Flask(__name__)

@app.route('/') #웹 디렉토리 설정
def hello():
    return "Backend Web Server!!"
def main():
    app.run(debug=True, port=80)    
if __name__ == '__main__':
    main()