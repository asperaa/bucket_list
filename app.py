from flask import Flask
app=Flask(_name_)

@app.route("/")
def main():
    return "welcome"

if __name__=="__main()__":
    app.run()

