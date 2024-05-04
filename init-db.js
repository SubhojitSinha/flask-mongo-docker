db = db.getSiblingDB("animal_db");
db.animal_tb.drop();
db.animal_tb.insertMany(
    { id:1, name: "lion", type: 'wild' },
    { id:2, name: "cow",  type: 'domestic' },
    { id:3, name: "cat",  type: 'domestic' },
);