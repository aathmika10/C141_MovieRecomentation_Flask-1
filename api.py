from flask import Flask,jsonify,request
import csv

allMovies=[]
with open("movies.csv")as f:
    csvreader=csv.reader(f)
    data=list(csvreader)
    allMovies=data[1:]

likedMovies=[]
disLikedMovies=[]
notWatchedMovies=[]

app=Flask(__name__)

@app.route("/get-movie")
def getMovie():
    return jsonify({
        "data":allMovies[0],
        "status":"success"
    })

@app.route("/liked-movie",methods=["POST"])
def likedMovie():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-movie",methods=["POST"])
def dislikedMovie():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    disLikedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/notwatched-movie",methods=["POST"])
def notWatchedMovie():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    notWatchedMovies.append(movie)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()