from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)