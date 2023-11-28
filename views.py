from flask import Flask, make_response, render_template


def main():
    return render_template('main.html')


def information():
    response = make_response('Hello world my dear 10 variant', 200)
    return response
