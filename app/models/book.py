from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}"

    #to get one specific car (base on the primary key)
    # chosen_car = Car.query.get(car_id)


    # # if chosen_car is None:
    # #     retun jsonify({'msg': f'COuld not find the car with id {car_id}'}), 404
    # #before for loop
    # #filter by
    # # get method can only be use by primary key because the id is unique
    # # using name or other parameter can not be use by get method because it can be result many names
    # # return jsonsify({ "id": chosen_car.id, "driver":})
    # """using the postman, body is none and retrieve all the cars information. We can resue them from the database.
    # by checking with the name and id to retrieve the information"""
    # #using get request
    #add new column, u need to upgrade the migration
    #to edit the file and edit with raw body
    # @cars.bp.route("/car_id>", methods=["PUT"])
    # def replace_one_car(car_id):
    #     try:
    #         car_id = int(car_id)
    #     except ValueError:
    #         return jsonify({'msg': f'Invalid car id'})

    #     request_body = request.get_json()

    #     if "driver" not in request_body or "team" not in request_body or "mass_kg" not in request_body:
    #         return jsonify({'msg': f"request must include driver, team, and mass_kg"}), 400

    #     if chosen_car is NOne:
    #         return jsonify({'msg': f'Could not find car with id {car_id'}), 404

    #     chosen_car.driver = request_body['driver']
    #     chosen_car.team = request_body['team']
    #     chosen_car.mass_kg = request_body["mass_kg"]


    #     #use this commit to save data after we want to change or update
    #     db.session.comit()

    #     return jsonify({'msg': f"Successfully replaced car with id {car_id}"})


        #the decorator make response for us that we dont have to do it ourselves when we in our ROUTE with decorator
        # if we not in the decorator function that we need to make our response ourselves when we want to return something

    # @cars.bp.route("/car_id>", methods=["DELETE"])
    # def replace_one_car(car_id):
    #     try:
    #         car_id = int(car_id)
    #     except ValueError:
    #         return jsonify({'msg': f'Invalid car id'})

    #     chosen_car = Car.query.get(car_id)


    #     if chosen_car is None:
    #         return jsonify({'msg': f'COuld not find the car with id {car_id}'}), 404

    #     db.sesson.delete(chosen_car)
    #     db.session.commit()

    #     return jsonify({'msg': f'deleted car with id {car_id}'})
    #     #request body is None