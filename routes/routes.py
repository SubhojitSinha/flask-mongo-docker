from flask import Blueprint
from controllers.test import hello_world,init_database,get_all,get_all_3,find_name,update_name,delete_doc,count_all,distint_by_field,insert_all,test_query
bp_routes = Blueprint('blueprint', __name__)

bp_routes.route('/', methods=['GET'])(hello_world)
bp_routes.route('/init-database', methods=['GET'])(init_database)
bp_routes.route('/get-all', methods=['GET'])(get_all)
bp_routes.route('/get-all-3', methods=['GET'])(get_all_3)
bp_routes.route('/find-name/<name>', methods=['GET'])(find_name)
bp_routes.route('/update-name/<id>/<name>', methods=['GET'])(update_name)
bp_routes.route('/delete/<id>', methods=['GET'])(delete_doc)
bp_routes.route('/count-all', methods=['GET'])(count_all)
bp_routes.route('/distinct/<field>', methods=['GET'])(distint_by_field)
bp_routes.route('/insert-all', methods=['GET'])(insert_all)
bp_routes.route('/test-query', methods=['GET'])(test_query)