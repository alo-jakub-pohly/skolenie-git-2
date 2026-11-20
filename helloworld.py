import io

def hello_world():
    output = io.StringIO()
    output.write("Hello World!")
    return output.getvalue()

if __name__ == "__main__":
    print(hello_world())
