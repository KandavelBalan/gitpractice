# trip_dtls = ('rapido','annanagar','metro','bike',55.00,'Completed')

# # print(trip_dtls)

# # print(trip_dtls[1])

# # print(trip_dtls.count('bike'))
# # print(trip_dtls.index(55.00))

# print(trip_dtls[2:])

# #sets


# hotel = ['chaminar','eam','mdb','ya.mohi']
# rest = set(hotel)

# print(rest)

#dictionary

trip = {
    "app": "rapido",
    "trip_id" : "R112233" ,
    "from" : "S.kolathur",
    "to" : "Tambaram",
    "fare" :  195.00,
    "status" : "Active",
    "driver_ass" : False,
    "trip_id" : "R112234"
}

# print(trip["from"])

# print(trip.get("from"))
# print(trip.get("From"))

# print(trip.keys())
# print(trip.values())

# for key, value in trip.items():
#     print(f'{key} : {value}')

# trip.update({"transport":"Auto"})

print(trip)

# trip.update({"transport":"bike"})

# print(trip)

# trip.pop("transport")

# print(trip)