from flask import Blueprint, flash, redirect, render_template, request, url_for

blueprint = Blueprint('payments', __name__, static_folder='../static')
