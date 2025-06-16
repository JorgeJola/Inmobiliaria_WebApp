from flask import Flask,Blueprint, render_template,request,redirect

main=Blueprint('main',__name__)

@main.route("/")
def main_interface():
    return render_template('loteo.html')

@main.route("/otros")
def otros():
    return render_template('otros.html')

@main.route("/contacto")
def contacto():
    return render_template('contacto.html')
