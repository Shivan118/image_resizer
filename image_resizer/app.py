from flask import Flask, render_template, request, redirect, url_for, send_file
from image_resizer.utils import resize_image, image_to_base64
import io
import base64  # Make sure this import is included
from PIL import Image

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            file = request.files.get('file')
            if file:
                original_image_data = file.read()
                original_image_base64 = base64.b64encode(original_image_data).decode('utf-8')
                image = Image.open(io.BytesIO(original_image_data))
                width = int(request.form.get('width', image.width))
                height = int(request.form.get('height', image.height))
                resized_image = resize_image(image, width, height)
                resized_image_base64 = image_to_base64(resized_image)
                return render_template(
                    'index.html',
                    original_image=original_image_base64,
                    resized_image=resized_image_base64,
                    width=width,
                    height=height,
                    show_resized=True
                )
        return render_template('index.html', show_resized=False)

    @app.route('/download')
    def download():
        image = request.args.get('image')
        if image:
            buffered = io.BytesIO(base64.b64decode(image))
            buffered.seek(0)
            return send_file(
                buffered,
                as_attachment=True,
                download_name="resized_image.png",
                mimetype="image/png"
            )
        return redirect(url_for('index'))

    return app

def main():
    app = create_app()
    app.run(debug=True)

if __name__ == '__main__':
    main()
