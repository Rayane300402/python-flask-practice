''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "Missing query parameter: ?textToAnalyze=your+text", 400

    result = sentiment_analyzer(text_to_analyze)

    if "error" in result:
        return f"Upstream error from Watson service:\n{result['error']}", 502

    label = result["label"]
    score = result["score"]
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
