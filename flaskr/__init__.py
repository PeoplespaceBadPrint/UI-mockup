from flask import Flask, render_template, request, make_response, jsonify, Response
from cam import VideoCamera
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def hello():
    return render_template('about.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_snapshot(camera):
    frame = camera.get_frame()
    yield (frame)

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot.jpg')
def snapshot():
    return Response(gen_snapshot(VideoCamera()),
                    mimetype='image/jpg')

# example for ajax
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=8080)
