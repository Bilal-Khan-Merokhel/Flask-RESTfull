from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field can not be blank')
    parser.add_argument('store_id', type=int, required=True, help='Every item needs a store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"Message": "Item Now Found"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name.lower()):
            return {'message': F'An Item with name {name.lower()} already exists' }, 400
        data = Item.parser.parse_args()
        item = ItemModel(name.lower(), **data)
        try:
            item.save_to_db()
        except:
            return {"Message": "An Error Occured inserting the item"}, 500
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item  = ItemModel.find_by_name(name.lower())
        if item:
            item.delete_from_db()
        return {'message': F'Item {name.lower()} Deleted'}, 202

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name.lower())

        if item is None:
            item = ItemModel(name.lower(), **data)
        else:
            item.price = data['price'] #**data
        item.save_to_db()
        return item.json()


class ItemList(Resource):

    def get(self):
        return {'Items': [item.json() for item in ItemModel.query.all()]}
