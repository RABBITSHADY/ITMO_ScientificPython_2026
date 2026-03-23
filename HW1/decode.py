import base64


def base64_to_image(txt_path, output_image):

    with open(txt_path, "r") as txt_file:
        b64_string = txt_file.read()

    img_data = base64.b64decode(b64_string)

    with open(output_image, "wb") as img_file:
        img_file.write(img_data)

    print(f"Success: {txt_path} restored to {output_image}")


if __name__ == "__main__":
    base64_to_image("remote_b64.txt", "remote_progress.png")