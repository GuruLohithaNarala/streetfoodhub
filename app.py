from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB config (adjust this if you're using cloud MongoDB like MongoDB Atlas)
app.config["MONGO_URI"] = "mongodb://localhost:27017/streetfood"
mongo = PyMongo(app)

# Home page
@app.route('/')
def index():
    vendors = mongo.db.vendors.find()
    return render_template('index.html', vendors=vendors)

# Add vendor
@app.route('/add_vendor', methods=['POST'])
def add_vendor():
    vendor = {
        'name': request.form['name'],
        'location': request.form['location'],
        'speciality': request.form['speciality']
    }
    mongo.db.vendors.insert_one(vendor)
    flash('Vendor added successfully!')
    return redirect(url_for('index'))

# Delete vendor
@app.route('/delete_vendor/<id>')
def delete_vendor(id):
    mongo.db.vendors.delete_one({'_id': ObjectId(id)})
    flash('Vendor deleted successfully!')
    return redirect(url_for('index'))

# Update vendor
@app.route('/update_vendor/<id>', methods=['POST'])
def update_vendor(id):
    mongo.db.vendors.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'name': request.form['name'],
            'location': request.form['location'],
            'speciality': request.form['speciality']
        }}
    )
    flash('Vendor updated successfully!')
    return redirect(url_for('index'))

# Run the app (important for Render/Railway)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
