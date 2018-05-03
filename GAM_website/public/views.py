# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
import braintree

from GAM_website.extensions import login_manager
from GAM_website.public.forms import LoginForm
from GAM_website.user.forms import RegisterForm
from GAM_website.user.models import User
from GAM_website.utils import flash_errors

# =============================================================
# Test code added by Nate in order to attempt redirecting from
# 'https://green-again.org' to https://greenagainmadagascar.org
# =============================================================
#
# @app.before_request
# def before_request():
#    if request.url.startswith('http://green-again.org/'):
#        url = request.url.replace('http://green-again.org', 'https://greenagainmadagascar.org/', 1)
#        code = 301
#       return redirect(url, code=code)


blueprint = Blueprint('public', __name__, static_folder='../static')

@blueprint.route('/donate', methods=['GET'])
def index():
    return redirect(url_for('payments.donate'))

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    # form = LoginForm(request.form)
    client_token = braintree.ClientToken.generate()
    # Handle logging in
    # if request.method == 'POST':
    #     # return redirect(url_for('payments.create_checkout'))
    #     # flash('You are logged in.', 'success')
    #     if form.validate_on_submit():
    #         pass
    #     #     login_user(form.user)
    #     #     flash('You are logged in.', 'success')
    #     #     redirect_url = request.args.get('next') or url_for('user.members')
    #     #     return redirect(redirect_url)
    #     else:
    #         pass
            # flash_errors(form)
    return render_template('public/home.html', client_token=client_token)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)

@blueprint.route('/terms/')
def terms():
    """Terms + Privacy Page"""
    return render_template('public/terms.html')


# @blueprint.route('/about/')
# def about():
#     """About page."""
#     form = LoginForm(request.form)
#     return render_template('public/about.html', form=form)



# @blueprint.route('/donate/')
# def about():
#     """Donations"""
#     form = LoginForm(request.form)
#     return render_template('public/about.html', form=form)
