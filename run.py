from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="192.168.68.78")
