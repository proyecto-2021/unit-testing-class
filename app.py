from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'

    if test_config is not None:
        app.config.from_mapping(test_config)

    db.init_app(app)

    @app.route('/users', methods=['POST'])
    def add_user():
        user = User({'username': request.json['username'], 'email': request.json['email']})
        db.session.add(user)
        db.session.commit()
        stored_user = User.query.filter_by(username='admin').first()
        return jsonify({'id': stored_user.id, 'username': stored_user.username, 'email': stored_user.email})

    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)


# from app import db, create_app
# db.create_all(app=create_app())




def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

#
#@app.route('/shutdown', methods=['POST'])
#def shutdown():
#    shutdown_server()
#    return 'Server shutting down...'
#
#
#@app.route('/test')
#def test():
#    return jsonify({ "message": "pong!" })
#
#@app.route('/assignments', methods=['GET'])
#def product_index():
#    return jsonify({"assignments": assignments})
#
#
#@app.route('/assignments/<string:assignment_name>', methods=['GET'])
#def get_single_assignment_by_name(assignment_name):
#    foundAssignment = [assignment for assignment in assignments if assignment['name'] == assignment_name]
#    if (len(foundAssignment) > 0):
#        return jsonify({"assignment": foundAssignment})
#    return make_response(jsonify({"assignment": "Not Found"}), 404)
#
#last_id=-1
#@app.route('/assignments', methods=['POST'])
#def create_produt():
#    #print(request.json)
#    global last_id
#    last_id += 1
#    new_assignment = {
#        "id": last_id,
#        "name": request.json['name'],
#        "price": request.json['price'],
#        "description": request.json['description'],
#        "status": request.json['status']
#    }
#
#    foundAssignment = [assignment for assignment in assignments if assignment['name'] == request.json['name']]
#    if (len(foundAssignment) > 0):
#        return make_response(jsonify({"assignment": foundAssignment}), 409)
#
#    assignments.append(new_assignment)
#    return jsonify(new_assignment)
#
#@app.route('/assignments/<string:assignment_name>', methods=['PUT'])
#def update_produt(assignment_name):
#    #print(request.json)
#    foundAssignment = [assignment for assignment in assignments if assignment['name'] == assignment_name]
#
#    if (len(foundAssignment) > 0):
#        foundAssignment[0]['name'] = request.json['name']
#        return jsonify({"assignment": foundAssignment})
#    return make_response(jsonify({"assignment": "Not Found"}), 404)
#
#
#@app.route('/assignments/<string:assignment_name>', methods=['DELETE'])
#def delete_produt(assignment_name):
#    print(request.json)
#    foundAssignment = [assignment for assignment in assignments if assignment['name'] == assignment_name]
#
#    if (len(foundAssignment) > 0):
#        assignments.remove(foundAssignment[0])
#        return jsonify({"assignments": assignments})
#    return make_response(jsonify({"assignment": "Not Found"}), 404)
#
#'''
#@app.route('/assignments/<int:assignment_id>')
#def product_show(assignment_id):
#    # [product for product in products if product['id'] == assignment_id]
#    # if len()
#
#    foundAssignment = [assignment for assignment in assignments if assignment['id'] == assignment_id]
#
#    if (len(foundAssignment) > 0):
#        return jsonify({"assignment": foundAssignment})
#    return make_response(jsonify({"assignment": "Not Found"}), 404)
#'''
#
#
#if __name__ == '__main__':
#    app.run(debug=True, port=4000)