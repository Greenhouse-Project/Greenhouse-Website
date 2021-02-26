from flask import render_template
from flask_login import login_required

from . import home

# Home route
@home.route('/')
def Home():
    return render_template('index.html', title='Home')
    
# # Front Room route
# @home.route('/front-room')
# def Front Room():
#     return render_template('TBD', title='Front Room')
    
# # Back Room route
# @home.route('/back-room')
# def Back Room():
#     return render_template('TBD', title='Back Room')
    
# # Outside route
# @home.route('/outside')
# def Outside():
#     return render_template('TBD', title='Outside')
    
# About route
@home.route('/about')
def About():
    return 'The About page is working'
#     return render_template('TBD', title='About')