from flask import Blueprint
from controllers.test import *
bp_routes = Blueprint('blueprint', __name__)

bp_routes.route('/', methods=['GET'])(hello_world)
bp_routes.route('/insert-test', methods=['GET'])(insert_test)
bp_routes.route('/get-all', methods=['GET'])(find_all)
bp_routes.route('/get-all-3', methods=['GET'])(get_all_3)
bp_routes.route('/find-name/<name>', methods=['GET'])(find_name)
bp_routes.route('/update-name/<id>/<name>', methods=['GET'])(update_name)
bp_routes.route('/delete/<id>', methods=['GET'])(delete_doc)
bp_routes.route('/count-all', methods=['GET'])(count_all)
bp_routes.route('/distinct/<field>', methods=['GET'])(distint_by_field)
bp_routes.route('/insert-all', methods=['GET'])(insert_all)
bp_routes.route('/test-query', methods=['GET'])(test_query)
bp_routes.route('/test-q', methods=['GET'])(test_q)

bp_routes.route('/insert-test-thread', methods=['GET'])(insert_test_thread)
bp_routes.route('/update-test-thread', methods=['GET'])(update_test_thread)
bp_routes.route('/delete-test-thread', methods=['GET'])(delete_test_thread)